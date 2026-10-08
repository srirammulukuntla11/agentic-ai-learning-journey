from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Fundamentals Server")


@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}! Welcome to MCP."


if __name__ == "__main__":
    mcp.run()