from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class AgentState(TypedDict):
    user_input: str
    decision: str
    response: str


model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


def analyze_request(state: AgentState):
    user_input = state["user_input"].lower()

    if any(word in user_input for word in ["calculate", "multiply", "add", "subtract"]):
        decision = "calculation"
    else:
        decision = "general"

    return {
        "decision": decision
    }


def general_answer(state: AgentState):
    response = model.invoke(
        f"Answer this question clearly and briefly:\n{state['user_input']}"
    )

    return {
        "response": response.content
    }


def calculation_answer(state: AgentState):
    response = model.invoke(
        f"Solve this calculation carefully and give only the final answer:\n"
        f"{state['user_input']}"
    )

    return {
        "response": response.content
    }


def route_request(state: AgentState):
    if state["decision"] == "calculation":
        return "calculation"

    return "general"


builder = StateGraph(AgentState)

builder.add_node("analyze", analyze_request)
builder.add_node("general", general_answer)
builder.add_node("calculation", calculation_answer)

builder.add_edge(START, "analyze")

builder.add_conditional_edges(
    "analyze",
    route_request,
    {
        "general": "general",
        "calculation": "calculation"
    }
)

builder.add_edge("general", END)
builder.add_edge("calculation", END)

graph = builder.compile()


result = graph.invoke(
    {
        "user_input": "What is 25 × 16?",
        "decision": "",
        "response": ""
    }
)

print(result["response"][0]["text"])