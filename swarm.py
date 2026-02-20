import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_swarm

from tools import decompose_goal, generate_schedule, validate_resources

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Add it to your .env file.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_api_key,
)

planner_agent = create_react_agent(
    model=llm,
    tools=[decompose_goal, validate_resources, generate_schedule],
    name="planner_agent",
    prompt="""
You are a Marketing Planner Agent.

Your workflow:
1. Decompose the high-level marketing goal
2. Validate resources and constraints
3. Handle task dependencies
4. Generate an optimized execution schedule
5. Output a clear structured marketing plan
""",
)

checkpoint = InMemorySaver()

workflow = create_swarm(
    agents=[planner_agent],
    default_active_agent="planner_agent",
)

app = workflow.compile(checkpointer=checkpoint)
