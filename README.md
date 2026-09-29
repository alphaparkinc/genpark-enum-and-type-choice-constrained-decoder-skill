# genpark-enum-and-type-choice-constrained-decoder-skill

Action selection constraint filter mapping conversational agent responses to canonical API endpoints and tool names.

## Architecture

```mermaid
flowchart LR
    Output[Raw LLM Output] --> Matcher[Exact & Substring Choice Matcher]
    Whitelist[Allowed Tools/Enums Whitelist] --> Matcher
    Matcher --> CanonicalAction[Canonical Action Invocation]
```

## Features
- **Anti-Hallucination Guard**: Never permits non-whitelisted actions.
- **Pure Python**: 100% standard library.
