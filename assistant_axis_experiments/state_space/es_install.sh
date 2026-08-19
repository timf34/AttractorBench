#!/usr/bin/env bash
# Install EasySteer (vLLM fork overlay) into its own venv on the pod.
set -euo pipefail
cd /workspace
python3 -m venv /workspace/es_venv
source /workspace/es_venv/bin/activate
pip install -q -U pip
pip install -q vllm==0.26.0 gguf
rm -rf /workspace/EasySteer-vllm-v1
git clone -q --depth 1 https://github.com/ZJU-REAL/EasySteer-vllm-v1.git
VLLM_DIR=$(python -c "import vllm, os; print(os.path.dirname(vllm.__file__))")
rsync -a /workspace/EasySteer-vllm-v1/vllm/ "$VLLM_DIR"/
python -c "import vllm, torch; print('vllm', vllm.__version__, 'torch', torch.__version__, 'cuda', torch.cuda.is_available()); import vllm.steer_vectors; print('steer_vectors importable')"
echo ES_INSTALL_DONE
