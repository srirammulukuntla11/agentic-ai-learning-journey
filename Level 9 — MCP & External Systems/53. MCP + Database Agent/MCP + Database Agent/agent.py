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

            await session.initialize()

            tools = await session.list_tools()

            print("Available MCP tools:")

            for tool in tools.tools:
                print("-", tool.name)


            user_request = "Find all students in the AI/ML course."


            response = await model.ainvoke(
                f"""
You are an AI agent.

User request:
{user_request}

Available MCP tool:
get_students_by_course(course)

Decide whether the MCP database tool should be used.

If it should be used, identify the course name.
"""
            )


            print("\nAgent Decision:")
            print(response.content)


            course_match = re.search(
                r"AI/ML|CSE|ECE",
                user_request,
                re.IGNORECASE
            )


            if (
                "yes" in str(response.content).lower()
                and course_match
            ):

                course = course_match.group()

                result = await session.call_tool(
                    "get_students_by_course",
                    arguments={
                        "course": course
                    }
                )


                tool_result = result.content[0].text


                print("\nMCP Database Result:")
                print(tool_result)


if __name__ == "__main__":
    asyncio.run(main())