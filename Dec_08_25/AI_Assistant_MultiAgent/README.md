# AI Assistant MultiAgent

A smart workplace assistant built with LangChain and LangGraph that intelligently routes user queries to specialized agents based on the type of request.

## Overview

This multi-agent system uses an intelligent router to direct user queries to one of four specialized nodes:
- **General Node**: Handles general conversations and queries
- **Research Node**: Conducts comprehensive research using multiple sources (DuckDuckGo, ArXiv, Wikipedia)
- **Writer Node**: Creates well-structured written content (emails, drafts, messages)
- **Planner Node**: Breaks down tasks and creates schedules

## Features

- 🤖 **Intelligent Routing**: Automatically detects query intent and routes to the appropriate agent
- 🔍 **Multi-Source Research**: Aggregates information from DuckDuckGo, ArXiv, and Wikipedia
- ✍️ **Content Generation**: Assists with writing tasks
- 📋 **Task Planning**: Creates structured plans and schedules
- 💬 **Interactive Mode**: Continuous conversation interface
- 🧠 **Powered by Groq LLM**: Fast and efficient language model processing

## Project Structure

```
    AI_Assistant_MultiAgent/
    ├── main.py                 # Entry point - interactive assistant
    ├── requirements.txt        # Project dependencies
    ├── config/
    │   └── settings.py        # Configuration and environment variables
    ├── graph/
    │   ├── __init__.py
    │   ├── nodes.py           # Agent node implementations
    │   ├── router.py          # Query routing logic
    │   ├── state.py           # Agent state management
    │   └── workflow.py        # Pipeline orchestration
    ├── services/
    │   └── llm.py             # LLM service configuration
    ├── tools/
    │   ├── __init__.py
    │   ├── arxiv_tool.py      # ArXiv research tool
    │   ├── ddg_tool.py        # DuckDuckGo search tool
    │   ├── wiki_tool.py       # Wikipedia search tool
    │   ├── summarizer_tool.py # Content summarization
    │   └── notes_tool.py      # Note generation
    └── utils/
        └── print_helpers.py   # Output formatting utilities
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI_Assistant_MultiAgent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Run the interactive assistant:

```bash
python main.py
```

### Example Queries

**General Conversation:**
```
You >> Hello, how are you?
```

**Research:**
```
You >> Research the latest developments in quantum computing
```

**Writing:**
```
You >> Write an email to my team about the upcoming meeting
```

**Planning:**
```
You >> Plan a schedule for learning Python in 2 weeks
```

**Exit:**
```
You >> exit
```

## How It Works

1. **User Input**: User enters a query through the interactive interface
2. **Routing**: The router analyzes the query and determines the appropriate agent based on keywords
3. **Processing**: The selected node processes the query:
   - **Research Node**: Gathers data from multiple sources, summarizes findings, and generates notes
   - **Writer Node**: Uses LLM to generate well-structured content
   - **Planner Node**: Creates step-by-step plans and schedules
   - **General Node**: Provides natural conversational responses
4. **Output**: Results are formatted and displayed to the user

## Routing Logic

The system uses keyword-based routing:
- **Writer**: `write`, `draft`, `compose`, `email`, `message`
- **Research**: `research`, `latest`, `who`, `what`, `when`, `study`, `papers`
- **Planner**: `plan`, `schedule`, `todo`, `tasks`, `breakdown`
- **General**: Default for all other queries

## Dependencies

- `python-dotenv`: Environment variable management
- `langchain-community`: Community tools and utilities
- `langchain-core`: Core LangChain functionality
- `langchain-groq`: Groq LLM integration
- `langgraph`: Graph-based workflow orchestration
- `duckduckgo-search`: Web search capability
- `wikipedia`: Wikipedia API access
- `arxiv`: Academic paper search
- `requests`: HTTP library

## Configuration

All configuration is managed through `config/settings.py` and uses environment variables loaded from `.env`:

- `GROQ_API_KEY`: Required for LLM functionality

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Author
Yadav Kuldeep,
SSPL Internship Project - December 2025
