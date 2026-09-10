import asyncio
from fastmcp import FastMCP
from supabase import create_async_client, AsyncClient
from dotenv import load_dotenv
import os

load_dotenv()

mcp = FastMCP("Expense Tracker")

supabase: AsyncClient | None = None


async def init_supabase():
    global supabase
    supabase = await create_async_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_KEY")
    )


# add expense
@mcp.tool()
async def add_expense(amount: float, category: str, description: str = "") -> dict:
    """Add new expense record"""

    response = await supabase.table("expenses").insert({
        "amount": amount,
        "category": category,
        "description": description
    }).execute()

    return response.data[0]

app = mcp.http_app(path="/mcp")
