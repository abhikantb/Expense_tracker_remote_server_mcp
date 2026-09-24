from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple calculator server")

#add two numbers
@mcp.tool()
def add(a:int, b:int) -> int:
    """Add two numbers.
    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b

# generate a random number    
@mcp.tool()
def random_number(min_value:int=1,max_value:int=100) -> int:
    '''Generate random number within  range.

    Args:
        min_value: Minimum value
        max_value: Maximum value
    
    Returns:
        A random number between min_value and max_value
    '''
    return random.randint(min_value, max_value)

# Resource: Server information
@mcp. resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)