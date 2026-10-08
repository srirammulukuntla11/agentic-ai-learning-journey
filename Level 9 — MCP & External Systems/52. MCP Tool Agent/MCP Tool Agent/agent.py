import asyncio
import re

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


server_params = StdioServerParameters(
    command="python",
    args=["server.py"]
)


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            # Initialize MCP session
            await session.initialize()

            # Discover available MCP tools
            tools = await session.list_tools()

            print("Available MCP tools:")
            for tool in tools.tools:
                print("-", tool.name)

            # User request
            user_request = "What is the sum of 25 and 17?"

            # Ask Gemini to decide whether the MCP tool should be used
            response = await model.ainvoke(
                f"""
You are an AI agent.

User request:
{user_request}

Available MCP tool:
calculate_sum(a, b)

Decide whether the MCP tool should be used.

If it should be used, identify the two numbers that need to be added.
"""
            )

            print("\nAgent Decision:")
            print(response.content)

            # Extract numbers from the user request
            numbers = [
                int(number)
                for number in re.findall(r"\d+", user_request)
            ]

            # Check whether the agent decided to use the tool
            if "yes" in str(response.content).lower() and len(numbers) >= 2:

                # Call the MCP tool
                result = await session.call_tool(
                    "calculate_sum",
                    arguments={
                        "a": numbers[0],
                        "b": numbers[1]
                    }
                )

                tool_result = result.content[0].text

                print("\nMCP Tool Result:")
                print(tool_result)

                # Ask Gemini to generate the final answer
                print("\nFinal Agent Answer:")
                print(tool_result)


if __name__ == "__main__":
    asyncio.run(main())