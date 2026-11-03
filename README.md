# agentic-ai-lab

Small prototypes of agentic design patterns, built while reading
*Agentic Design Patterns*. All agents run locally on a small LLM via Ollama.

## Agents

| Agent | Pattern | What it does |
|---|---|---|
| `reflection_agent.py` | Reflection | Single pass: drafts an answer, critiques it, then revises using the critique. |
| `tool_agent.py` | Tool use | The model returns JSON choosing `calculate` or `answer`. Arithmetic is run by a safe AST-based calculator (`tools/calculator.py`), then the model explains the result. |
| `research_agent.py` | Planning (basic) | Single prompt that turns a question into a refined question, subquestions, methods, limitations, and a first step. No web search. |

`llm.py` is a thin wrapper around `ollama.chat`, so the model can be swapped in one place.

## Setup

1. Install [Ollama](https://ollama.com) and pull the model:
   `ollama pull llama3.2:1b`
2. Install dependencies: `pip install -r requirements.txt`
3. Run an agent from the repo root:
   ```
   python -m agents.reflection_agent
   python -m agents.tool_agent
   python -m agents.research_agent
   ```

## Model

- `llama3.2:1b` via Ollama (change `MODEL` in `agents/llm.py`).
- Results from a 1B model are limited, especially JSON formatting and
  self-critique. See `experiments.md`.

## Project structure

```
agents/   reflection_agent.py, tool_agent.py, research_agent.py, llm.py
tools/    calculator.py
experiments.md   experiment log
main.py
```

## Known limitations

- The reflection agent runs one critique-revise pass, with no stopping condition.
- The tool agent has one tool (calculator) and no retry if the model returns invalid JSON.
- The research agent does not search or cite anything; it only plans.
