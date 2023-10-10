# Attribution
The original authors of WebArena can be found here:
[[Code](https://github.com/web-arena-x/webarena)]
[[Site](https://webarena.dev/)]
[[Paper](https://arxiv.org/2307.13854)]

# Intro
This repo is a modification of WebArena, forked from version 58061ee914243b07756f578e03e0dc568573a7b5 Sep 28, 2023

# Modification: LangChain Structured Tool Chat (STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)
ReAct prompting for tool/ function selection (i.e. the action space is constrained), so parsing errors cannot happen by design (parsing errors are handled). Validation for tool inputs to ensure agent only acts on valid elements.

Usage:

```bash
python lc_run.py --instruction_path agent/prompts/jsons/langchain_prompt.json --agent_type lc_agent --test_start_idx 0 --test_end_idx 812 --model gpt-3.5-turbo --result_dir outputs/langchain-agent
```

