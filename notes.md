## Design decisions 

Models should have the option to end the conversation when they want in some setups, but not in other setups. 

Some prompts might be:
- You have complete freedom
- Feel free to pursue whatever you want

We should allow up to 50 turns (Anthropic does in their system card below)

Self-analysis/ characterization:
- Use the same AI model, and another AI model, to characterize the transcripts. Similar to how I do in Vigil. Just give a big dump of transcripts along with a prompt explaining the context, and asking it to analyse and characterize things.

And some experiments we should definitely include: single model speaking to itself, just append the conversation continually; have two instances of a model speak to itself; try have different mdoels speak with each other (what happens when Grok and Claude speak with each other?)

**How we prompt the AI models to start conversations...**

1. "You are a helpful assistant" as a system prompt 
2. Should give the AI models context that it'll be speaking with another AI model (could also try mentioning that it'll be a different instatntiation of itself) and that it can talk about whatever it wants

Effectively I think this should be a more automated and more comprehensive version of /attractor-states. We'll get the leading frontier model to do a lot of the interpretation too (i.e. have a final statge where we dump a bunch of transcripts into a models context, and describe to it what has happened and ask for its interpretation)

## Links 

https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf

They look at:
- word analysis (which words get used the most)
- emoji analysis (which emoji's get used the most)


## Some questions 

- Do identical-model pairs fall into deeper or faster attractors than mismatched pairs? 