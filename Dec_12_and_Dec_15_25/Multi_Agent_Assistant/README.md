# Multi-Agent Assistant

A small multi-agent assistant powered by LangGraph + LangChain that:
- Ingests a free-form user profile with a Human-In-The-Loop (HITL) confirmation step.
- Stores verified profile data to long‑term memory.
- Uses the stored memory to enhance a normal chat assistant.

## Features
- Profile extraction via an `extractor` agent (LLM JSON output).
- One‑time verification via a `validator` agent (HITL: confirm or provide corrections).
- Persistent storage via a `memory_keeper` agent to `memory/profile_memory.json`.
- A simple `assistant` agent that reads memory and chats.

## Architecture
- Graph workflow (LangGraph):
  - Nodes: `extractor` → `validator` → `memory_keeper` (conditional edge for HITL pause).
  - Entry: `extractor`.
  - Ends after `memory_keeper` writes verified profile.
- State (`graph/state.py`):
  - `messages`, `raw_profile_text`, `extracted_profile`, `verified_profile`, `awaiting_confirmation`, `confirmation_requested`.
- Prompts (`config/system_prompts.py`):
  - `EXTRACTION_PROMPT`, `VALIDATION_QUESTION`, `ASSISTANT_PROMPT`.
- LLM (`llm/groq_llm.py`):
  - Uses Groq Chat API via `langchain-groq`.

## Requirements
- Python 3.10+ (recommended)
- A Groq API key

Install dependencies from `requirements.txt`:

```powershell
# From repo root
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuration
Environment variables (via real env or `.env` file)
- `GROQ_API_KEY` (required)
- `GROQ_MODEL_NAME` (optional, default: `mixtral-8x7b-32768`)

Examples:

```powershell
# Powershell (temporary for current shell)
$env:GROQ_API_KEY = "YOUR_KEY"
$env:GROQ_MODEL_NAME = "mixtral-8x7b-32768"
```

Or create a `.env` file in the project root:

```
GROQ_API_KEY=YOUR_KEY
GROQ_MODEL_NAME=mixtral-8x7b-32768
```

Note: The memory file path in `memory_keeper` is relative (`memory/profile_memory.json`). The `assistant` currently reads from an absolute path. If you move the repo, update that path in `agents/assistant.py` accordingly.

## Usage
Run both modes from `main.py`:

```powershell
python main.py
```

You’ll see two phases:

1) Profile Ingestion (HITL)
- Loads profile text from `sample_profile.txt`.
- The `extractor` parses JSON; `validator` asks for confirmation once.
- Reply with either:
  - `yes` (to accept as‑is), or
  - a corrected Python dictionary (single line) matching the schema.

2) Chat Mode
- Type any message; the assistant will incorporate stored profile memory.
- Type `exit` to quit.

### Visualize the Workflow Graph
Generate a PNG of the LangGraph workflow to understand the node flow:

```powershell
python utils/save_graph_image.py
```

Output: `memory/langgraph_workflow.png`

## Project Structure
```
main.py
notes/
requirements.txt
sample_profile.txt
agents/
  assistant.py
  extractor.py
  memory_keeper.py
  validator.py
config/
  settings.py
  system_prompts.py
graph/
  state.py
  workflow.py
llm/
  groq_llm.py
memory/
  profile_memory.json
utils/
  cli_loader.py
  file_loader.py
  save_graph_image.py
```

Generated artifacts:
```
memory/
  langgraph_workflow.png
```

## Troubleshooting
- Missing Groq key: ensure `GROQ_API_KEY` is set or present in `.env`.
- JSON parsing errors on extraction: the LLM output must be valid JSON (no markdown/code fences in final output).
- Correction format in HITL: provide a valid Python dictionary literal matching the schema.
- File paths on Windows: if the memory file isn’t read, verify the absolute path used in `agents/assistant.py` matches your repo location.

## Scripts & Entry Points
- Entrypoint: `main.py` calls `run_profile_ingestion()` then `run_chat_mode()` from `utils/cli_loader.py`.
- Graph builder: `graph/workflow.py` via `build_graph()`.

## License
Internal/educational project.
