import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

# Create LangChain agent
agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a helpful AI assistant."
)

# Send a request to the agent
result = agent.invoke(
    {        "messages": [
            {
                "role": "user",
                "content": "What is 25 × 16?"
            }
        ]
    }
)

# Print the final response
print(result["messages"][-1].content[0]["text"])