from fastmcp import FastMCP
import random
mcp=FastMCP(name="Demo Server")

@mcp.tool()
def add_numbers(a:int,b:int):
    return a+b
@mcp.tool()
def roll_dice(n_dice:int=1):
    return [random.randint(1,6) for _ in range(n_dice)]


if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8081)