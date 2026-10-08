from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

# Load environment variables
load_dotenv()


# Create a calculator tool
@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


# Create LangChain agent with the calculator tool
agent = create_agent(
    model=model,
    tools=[multiply_numbers],
    system_prompt=(
        "You are a helpful mathematical assistant. "
        "Always use the multiply_numbers tool when the user asks "
        "for multiplication."
    )
)


# Send a request to the agent
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is 25 × 16?"
            }
        ]
    }
)


# Print the final response
print(result["messages"][-1].content[0]["text"])