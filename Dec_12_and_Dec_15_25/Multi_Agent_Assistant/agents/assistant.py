import json
from langchain_core.messages import AIMessage
from llm.groq_llm import get_groq_llm
from config import ASSISTANT_PROMPT

llm = get_groq_llm()

MEMORY_FILE = "E:\\SSPL_Internship_Repo\\Dec_12_25\\Multi_Agent_Assistant\\memory\\profile_memory.json"

def assistant_agent(state):
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    except FileNotFoundError:
        memory = {}

    messages = state["messages"]

    system_prompt = ASSISTANT_PROMPT.format(memory=memory)

    response = llm.invoke(system_prompt + "\n" + messages[-1].content)

    return {
        "messages": [AIMessage(content=response.content)]
    }
