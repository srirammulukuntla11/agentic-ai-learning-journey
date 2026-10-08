from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()


# Define the state
class AgentState(TypedDict):
    user_input: str
    user_name: str
    response: str


# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


# Agent node
def agent_node(state: AgentState):
    prompt = f"""
User name: {state["user_name"]}

User request:
{state["user_input"]}

Answer the user's request and address the user by their name.
"""

    response = model.invoke(prompt)

    return {
        "response": response.content
    }


# Create the graph
builder = StateGraph(AgentState)

# Add agent node
builder.add_node("agent", agent_node)

# Connect START → agent
builder.add_edge(START, "agent")

# Connect agent → END
builder.add_edge("agent", END)

# Build the graph
graph = builder.compile()


# Run the graph
result = graph.invoke(
    {
        "user_input": "Explain artificial intelligence in one sentence.",
        "user_name": "Sriram",
        "response": ""
    }
)


# Print the final response
print(result["response"][0]["text"])