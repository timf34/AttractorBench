#!/usr/bin/env python3
"""
Fetch SAE feature explanations and metadata from Neuronpedia.

Example usage:
    python -m assistant_axis_experiments.state_space.neuronpedia_lookup llama3.3-70b-it 50-resid-post-gf 0 1 2

This will fetch features 0, 1, 2 from the Goodfire Llama-3.3-70B-Instruct SAE (layer 50).

Optional: Set NEURONPEDIA_API_KEY environment variable (currently read but not required for public endpoints).
"""

import sys
import os
import json
import urllib.request
import urllib.error
from pathlib import Path


def load_env_file(env_path: str = ".env") -> dict:
    """Load environment variables from a .env file."""
    env_vars = {}
    if os.path.exists(env_path):
        try:
            with open(env_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        # Remove surrounding quotes if present
                        value = value.strip('"\'')
                        env_vars[key.strip()] = value
        except Exception as e:
            print(f"Warning: Failed to load .env file: {e}", file=sys.stderr)
    return env_vars


def fetch_feature(
    model_id: str, source_id: str, feature_index: int, api_key: str = None
) -> dict:
    """
    Fetch a single feature from Neuronpedia API.

    Args:
        model_id: Model identifier (e.g., "llama3.3-70b-it")
        source_id: SAE source/layer identifier (e.g., "50-resid-post-gf")
        feature_index: Feature index to fetch
        api_key: Optional API key (may be required for private content)

    Returns:
        Dictionary containing feature data including explanations and activations
    """
    url = f"https://neuronpedia.org/api/feature/{model_id}/{source_id}/{feature_index}"

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; neuronpedia-lookup/1.0)"
    }

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(
                f"Feature not found: {model_id}/{source_id}/{feature_index}. "
                "Check that model_id and source_id are correct."
            )
        elif e.code == 500:
            raise ValueError(
                f"Server error for {model_id}/{source_id}/{feature_index}. "
                "The model or source ID may be incorrect."
            )
        else:
            raise
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error fetching feature: {e.reason}")


def format_tokens(token_list: list, value_list: list = None, max_tokens: int = 10) -> str:
    """Format a list of tokens, optionally with their values."""
    if not token_list:
        return "(none)"

    formatted_tokens = []
    for i, token in enumerate(token_list[:max_tokens]):
        # Clean up token representation
        token_display = token.replace("\n", "\\n").replace("\t", "\\t")

        if value_list and i < len(value_list):
            formatted_tokens.append(f"{token_display} ({value_list[i]:.4f})")
        else:
            formatted_tokens.append(token_display)

    return ", ".join(formatted_tokens)


def print_feature_info(
    model_id: str, source_id: str, feature_index: int, feature_data: dict
) -> None:
    """Print formatted feature information."""
    print(f"\n{'='*70}")
    print(f"Feature: {feature_index} ({model_id} / {source_id})")
    print(f"{'='*70}")

    # Print main explanation if available
    explanations = feature_data.get("explanations", [])
    if explanations:
        explanation = explanations[0]
        print(f"Explanation: {explanation.get('description', '(none)')}")
    else:
        print("Explanation: (none)")

    # Print max activation
    max_act = feature_data.get("maxActApprox")
    if max_act is not None:
        print(f"Max Activation: {max_act:.4f}")

    # Print top activating tokens (pos_str)
    pos_str = feature_data.get("pos_str", [])
    pos_val = feature_data.get("pos_values", [])
    if pos_str:
        print(f"Top Activating Tokens: {format_tokens(pos_str, pos_val)}")

    # Print top negative tokens (neg_str)
    neg_str = feature_data.get("neg_str", [])
    neg_val = feature_data.get("neg_values", [])
    if neg_str:
        print(f"Top Negative Tokens:   {format_tokens(neg_str, neg_val)}")

    # Print sparsity
    frac_nonzero = feature_data.get("frac_nonzero")
    if frac_nonzero is not None:
        print(f"Sparsity: {frac_nonzero:.4%} non-zero activations")

    # Print example activations
    activations = feature_data.get("activations", [])
    if activations:
        print(f"Example Activations: {len(activations)} examples")
        for i, activation in enumerate(activations[:2]):
            tokens = activation.get("tokens", [])
            values = activation.get("values", [])
            max_idx = activation.get("maxValueTokenIndex", -1)
            if tokens:
                token_str = ", ".join(tokens[:8])
                if max_idx >= 0 and max_idx < len(tokens):
                    max_val = activation.get("maxValue", 0)
                    print(
                        f"  Example {i}: max={max_val:.4f} at token '{tokens[max_idx]}' | "
                        f"tokens: {token_str}"
                    )
                else:
                    print(f"  Example {i}: tokens: {token_str}")


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 4:
        print(
            "Usage: python -m assistant_axis_experiments.state_space.neuronpedia_lookup "
            "<modelId> <sourceId> <index> [<index>...]",
            file=sys.stderr,
        )
        print("\nExample:", file=sys.stderr)
        print(
            "  python -m assistant_axis_experiments.state_space.neuronpedia_lookup "
            "llama3.3-70b-it 50-resid-post-gf 0 1 2",
            file=sys.stderr,
        )
        sys.exit(1)

    model_id = sys.argv[1]
    source_id = sys.argv[2]
    feature_indices = sys.argv[3:]

    # Try to parse indices as integers
    try:
        feature_indices = [int(idx) for idx in feature_indices]
    except ValueError:
        print(
            f"Error: Feature indices must be integers. Got: {sys.argv[3:]}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Load API key from environment or .env file
    api_key = os.getenv("NEURONPEDIA_API_KEY")
    if not api_key:
        env_vars = load_env_file()
        api_key = env_vars.get("NEURONPEDIA_API_KEY")

    # Fetch and print each feature
    failed_indices = []
    for feature_index in feature_indices:
        try:
            print(f"Fetching feature {feature_index}...", file=sys.stderr)
            feature_data = fetch_feature(model_id, source_id, feature_index, api_key)
            print_feature_info(model_id, source_id, feature_index, feature_data)
        except (ValueError, RuntimeError) as e:
            print(f"Error: {e}", file=sys.stderr)
            failed_indices.append(feature_index)

    if failed_indices:
        print(
            f"\nFailed to fetch {len(failed_indices)} feature(s): {failed_indices}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
