from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Tool Agent Server")


@mcp.tool()
def calculate_sum(a: int, b: int) -> str:
    """Add two numbers and return their sum."""
    result = a + b
    return f"The sum of {a} and {b} is {result}."


if __name__ == "__main__":
    mcp.run()