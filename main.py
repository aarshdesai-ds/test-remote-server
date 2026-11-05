from fastmcp import FastMCP
import random
import json

mcp = FastMCP(name = "Simple Calculator Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def random_number(min_value:int = 1, max_value:int = 100) -> int:
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info() -> str:
    """Return server information."""
    info = {
        "name": mcp.name,
        "version": "1.0.0",
        "description": "A simple calculator server with random number generation.",
        "tools": [
            {
                "name": "add",
                "description": "Add two numbers.",
                "parameters": [
                    {"name": "a", "type": "float", "description": "First number."},
                    {"name": "b", "type": "float", "description": "Second number."}
                ],
                "return_type": "float"
            },
            {
                "name": "random_number",
                "description": "Generate a random number between min_value and max_value.",
                "parameters": [
                    {"name": "min_value", "type": "int", "description": "Minimum value (default 1)."},
                    {"name": "max_value", "type": "int", "description": "Maximum value (default 100)."}
                ],
                "return_type": "int"
            }
        ],
        "author": "Aarsh Desai"
    }
    return json.dumps(info, indent=4)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    