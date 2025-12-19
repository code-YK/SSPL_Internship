from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# YouTube Transcript Agent
youtube_agent = Agent(
    name="YouTube Transcript Agent",
    role="Extract transcript from YouTube videos",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YouTubeTools()],
    instructions=[
        "Extract the complete transcript from the given YouTube link.",
        "Do not summarize unless explicitly asked.",
        "If transcript is unavailable, clearly mention it."
    ],
    markdown=True,
)

# Team Agent (Orchestrator)
agent_team = Agent(
    team=[youtube_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=[
        "Return the YouTube transcript clearly.",
        "Preserve timestamps if available."
    ],
    markdown=True,
)

user_input = input("Please enter youtube link to extract transcript: ")
agent_team.print_response(
    f"Here is the YouTube link: {user_input}. Extract the transcript."
)
