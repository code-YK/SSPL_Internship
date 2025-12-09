from .state import Agentstate
from tools import WikiTool, DDGTool, ArxivTool, SummarizerTool, NotesTool
from services.llm import get_groq_llm

# Create instances of the tools
wiki = WikiTool()
ddg = DDGTool()
arxiv = ArxivTool()
summarizer = SummarizerTool()
notes = NotesTool()

# GENERAL NODE
def general_node(state: Agentstate) -> Agentstate:
    llm = get_groq_llm()
    
    prompt = (
        f"Respond naturally and helpfully to the following user message:\n\n"
        f"{state.user_inputs}"
    )
    
    response = llm.invoke(prompt)
    state.result = {
        "type": "general",
        "content": response.content
    }
    return state


# RESEARCH NODE
def research_node(state: Agentstate) -> Agentstate:
    
    query = state.user_inputs
    
    ddg_results = ddg.run(query)
    arxiv_results = arxiv.run(query)
    wiki_results = wiki.run(query)

    combined_text = (
        f"DDG Results:\n{ddg_results}\n\n"
        f"ArXiv Results:\n{arxiv_results}\n\n"
        f"Wikipedia Results:\n{wiki_results}"
    )
    
    summary = summarizer.run(combined_text)
    notes_text = notes.run(query, summary)

    state.result = {
        "type": "research",
        "summary": summary,
        "notes": notes_text,
        "raw": {
            "ddg": ddg_results,
            "arxiv": arxiv_results,
            "wiki": wiki_results
        }
    }
    return state

# WRITER NODE
def writer_node(state: Agentstate) -> Agentstate:
    llm = get_groq_llm()

    prompt = (
        f"You are a helpful assistant.\n"
        f"Write a clear and well-structured response for the following input:\n\n"
        f"{state.user_inputs}"
    )

    response = llm.invoke(prompt)
    
    state.result = {
        "type": "writer",
        "content": response.content
    }
    return state


# PLANNER NODE
def planner_node(state: Agentstate) -> Agentstate:
    llm = get_groq_llm()

    prompt = (
        f"Break down the following into steps and provide a simple schedule:\n\n"
        f"{state.user_inputs}"
    )

    response = llm.invoke(prompt)

    state.result = {
        "type": "planner",
        "content": response.content
    }
    return state
