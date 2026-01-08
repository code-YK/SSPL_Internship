# 🌍 Trip & Event Planner

A smart, AI-powered chatbot built with **LangGraph** and **LangChain** that helps users plan trips with special events (birthdays, anniversaries, team-building activities, etc.). The system uses multiple specialized agents working collaboratively with human-in-the-loop validation at each stage.

## ✨ Features

- **🤖 Multi-Agent Architecture**: Specialized agents for Research, Planning, and Pricing
- **🔄 Human-in-the-Loop**: Interactive confirmation and modification at each stage
- **🧠 Conversational Memory**: Maintains context across the entire planning session
- **📊 Structured Output**: Uses Pydantic models for validated, type-safe data
- **🌐 Web Search Integration**: Real-time research using Tavily API
- **💰 Smart Budget Management**: Automatic cost calculation with buffer and risk analysis
- **📅 Intelligent Itinerary Planning**: Day-by-day scheduling with rest day suggestions

## 🏗️ Architecture

The system follows a state-graph workflow with conditional routing:

```
User Input → Intent Analysis → Research Agent → Review → Planner Agent → Review → Pricing Agent → Review → Final Output
                                      ↑______________|          ↑______________|         ↑______________|
```

### Core Agents

1. **Intent Agent**: Extracts and validates user requirements (destination, dates, budget, event type, group size)
2. **Research Agent**: 
   - Searches for destination information, attractions, and activities
   - Retrieves weather data for the travel period
   - Finds suitable event venues
   - Estimates travel and accommodation costs
3. **Planner Agent**: 
   - Creates day-by-day itinerary
   - Schedules the special event
   - Suggests rest days
   - Validates dates and constraints
4. **Pricing Agent**: 
   - Calculates total trip costs
   - Applies budget buffers (10% default)
   - Identifies budget risks
   - Provides cost breakdowns
5. **Review Nodes**: Human-in-the-loop checkpoints after each agent for approval/modification
6. **Final Presenter**: Formats the complete plan into user-friendly output

## 📁 Project Structure

```
Trip_Event_Planner/
├── main.py                      # Entry point
├── graph.py                     # LangGraph workflow definition
├── llm.py                       # LLM configuration
├── langgraph.json              # LangGraph configuration
├── requirements.txt             # Python dependencies
│
├── config/                      # Configuration & Settings
│   ├── __init__.py
│   ├── settings.py              # Pydantic settings (API keys, model configs)
│   ├── constants.py             # Application constants
│   └── logging_config.py        # Logging setup
│
├── nodes/                       # Agent Implementation
│   ├── intent.py                # Intent extraction agent
│   ├── research.py              # Research agent (web search)
│   ├── planner.py               # Itinerary planning agent
│   ├── pricing.py               # Budget & pricing agent
│   ├── review.py                # Human-in-the-loop review logic
│   └── final_presenter.py       # Output formatting agent
│
├── tools/                       # Agent-specific Tools
│   ├── research.py              # Search tools (Tavily integration)
│   ├── planner.py               # Date/schedule utilities
│   ├── pricing.py               # Cost calculation tools
│   └── research_cost.py         # Cost estimation tools
│
├── states/                      # State Management
│   ├── main_state.py            # Main graph state definition
│   └── schemas/                 # Pydantic Models
│       ├── intent.py            # User intent schema
│       ├── research.py          # Research output schema
│       ├── planner.py           # Itinerary schema
│       ├── pricing.py           # Pricing schema
│       ├── review.py            # Review schema
│       ├── final_output.py      # Final plan schema
│       ├── presentation.py      # User-friendly output schema
│       └── costs.py             # Cost-related schemas
│
├── utils/                       # Utilities
│   ├── prompts.py               # LLM prompts for each agent
│   └── reducers.py              # State reducers for memory management
│
├── notebooks/                   # Testing & Development
│   ├── 1_Testing_tools.ipynb   # Tool functionality tests
│   ├── 2_Testing_agents.ipynb  # Agent/node tests
│   └── 3_Graph_testing.ipynb   # End-to-end graph tests
│
└── logs/                        # Application logs
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Trip_Event_Planner
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   # LLM Configuration (Groq)
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_MODEL_NAME=llama-3.3-70b-versatile
   GROQ_TEMPERATURE=0.3
   GROQ_MAX_TOKENS=2048
   
   # Web Search (Tavily)
   TAVILY_API_KEY=your_tavily_api_key_here
   TAVILY_SEARCH_DEPTH=basic
   
   # LangSmith Tracing (Optional)
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   LANGCHAIN_PROJECT=trip-event-planner
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   
   # Application Settings
   DEBUG=true
   MAX_MESSAGE_WINDOW=12
   DEFAULT_BUDGET_BUFFER_PERCENT=10
   MAX_PLANNER_RETRIES=3
   ```

### API Keys

- **Groq API**: Get your free API key from [console.groq.com](https://console.groq.com)
- **Tavily API**: Get your API key from [tavily.com](https://tavily.com)
- **LangSmith** (Optional): For tracing and debugging - [smith.langchain.com](https://smith.langchain.com)

## 💻 Usage

### Running the Application

```bash
python main.py
```

### Example Interaction

```
=== Trip & Event Planner ===

Describe your trip or event plan:
> I want to plan a birthday trip to Goa for 4 people between January 10 and January 15 with a budget of 80k

[System analyzes intent...]

=== Research Results ===
Destination: Goa, India
Weather: Sunny, 21-32°C
Venues Found: 11 options including beachside resorts and restaurants
...

Approve research results? (yes/no): yes

[System creates itinerary...]

=== Itinerary ===
Day 1: Arrival and beach exploration
Day 2: Water sports and local markets
Day 3: Birthday celebration at beach resort
...

Approve itinerary? (yes/no): yes

[System calculates pricing...]

=== Budget Breakdown ===
Total Cost: ₹78,500 (within budget ✓)
...
```

## 🛠️ Development & Testing

### Testing Individual Tools

```bash
jupyter notebook notebooks/1_Testing_tools.ipynb
```

### Testing Agents

```bash
jupyter notebook notebooks/2_Testing_agents.ipynb
```

### End-to-End Graph Testing

```bash
jupyter notebook notebooks/3_Graph_testing.ipynb
```

## 📊 State Management

The system uses a typed state graph (`TripEventState`) that maintains:

- **Conversation History**: All messages between user and system
- **User Intent**: Extracted requirements (destination, dates, budget, etc.)
- **Research Results**: Destination info, weather, venues, cost estimates
- **Itinerary**: Day-by-day plan with activities and event scheduling
- **Pricing**: Detailed cost breakdown and budget analysis
- **Review States**: Approval status at each checkpoint
- **Final Output**: User-friendly formatted plan

## 🔧 Key Technologies

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Stateful multi-agent workflow orchestration
- **[LangChain](https://github.com/langchain-ai/langchain)**: LLM integration and tooling
- **[Groq](https://groq.com)**: Fast LLM inference (Llama 3.3 70B)
- **[Pydantic](https://docs.pydantic.dev)**: Data validation and settings management
- **[Tavily](https://tavily.com)**: AI-optimized web search API
- **[LangSmith](https://smith.langchain.com)**: Tracing and debugging (optional)

## 🎯 Features in Detail

### Human-in-the-Loop Reviews

After each major agent (Research, Planner, Pricing), the system:
1. Presents results in a structured format
2. Asks specific confirmation questions
3. Allows user to approve or request modifications
4. Loops back to the agent if changes are needed

### Memory Management

- Uses a rolling message window (configurable, default: 12 messages)
- Maintains structured state across all agents
- Custom reducers for message history optimization

### Budget Intelligence

- Automatic 10% buffer for contingencies
- Risk identification when approaching budget limits
- Detailed cost breakdowns by category
- Validation against user's stated budget

### Smart Planning

- Validates event day within trip duration
- Suggests rest days (typically after the event)
- Accommodates group size in venue selection
- Weather-aware activity suggestions

## 📝 Configuration

Edit `config/settings.py` or use environment variables to configure:

- **LLM Settings**: Model selection, temperature, token limits
- **Search Depth**: Basic or advanced Tavily searches
- **Budget Buffer**: Default percentage for cost estimates
- **Memory Window**: Number of messages to retain
- **Retry Limits**: Maximum planning attempts

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure virtual environment is activated and all dependencies are installed
2. **API Key Errors**: Verify `.env` file is in project root and contains valid keys
3. **Validation Errors**: Check that LLM output matches expected Pydantic schemas
4. **Search Failures**: Confirm Tavily API key is valid and has credits

### Logging

Logs are stored in the `logs/` directory. Check them for detailed debugging:
- Application logs show agent execution flow
- Error logs contain stack traces for failures

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional event types (weddings, corporate events)
- More sophisticated venue filtering
- Integration with booking APIs
- Multi-language support
- Enhanced cost prediction models

## 📄 License

[Specify your license here]

## 👥 Authors

[Your name/team information]

## 🙏 Acknowledgments

- Built as part of SSPL Internship Program
- Inspired by modern multi-agent AI systems
- Uses state-of-the-art open-source LLM frameworks

---

**Note**: This is a proof-of-concept system. For production use, add error handling, rate limiting, cost monitoring, and user authentication.
