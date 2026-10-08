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


            try:

                response = await asyncio.wait_for(
                    model.ainvoke(
                        f"""
You are an AI agent.

User request:
{user_request}

Available MCP tools:

1. calculate_sum(a, b)
2. get_students_by_course(course)
3. reverse_text(text)

Decide which MCP tool should be used for this request.

Return the tool name that should be used.
If the request does not require an MCP tool, say NONE.
"""
                    ),
                    timeout=30
                )

            except asyncio.TimeoutError:

                print("\nGemini request timed out.")
                return


            print("\nAgent Decision:")
            print(response.content)


            decision = str(response.content).lower()


            if "calculate_sum" in decision:

                numbers = [
                    int(number)
                    for number in re.findall(r"\d+", user_request)
                ]

                if len(numbers) >= 2:

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


            elif "get_students_by_course" in decision:

                course_match = re.search(
                    r"AI/ML|CSE|ECE",
                    user_request,
                    re.IGNORECASE
                )

                if course_match:

                    course = course_match.group()

                    result = await session.call_tool(
                        "get_students_by_course",
                        arguments={
                            "course": course
                        }
                    )

                    tool_result = result.content[0].text

                    print("\nMCP Tool Result:")
                    print(tool_result)


            elif "reverse_text" in decision:

                text_match = re.search(
                    r"reverse\s+(.+)",
                    user_request,
                    re.IGNORECASE
                )

                if text_match:

                    text = text_match.group(1)

                    result = await session.call_tool(
                        "reverse_text",
                        arguments={
                            "text": text
                        }
                    )

                    tool_result = result.content[0].text

                    print("\nMCP Tool Result:")
                    print(tool_result)


            else:

                print("\nNo MCP tool required.")


if __name__ == "__main__":
    asyncio.run(main())