from fastmcp import FastMCP
from supabase import create_async_client, AsyncClient
import os

mcp = FastMCP("Expense Tracker")

supabase: AsyncClient | None = None


async def get_supabase() -> AsyncClient:
    global supabase

    if supabase is None:
        supabase = await create_async_client(
            os.environ["SUPABASE_URL"],
            os.environ["SUPABASE_SERVICE_KEY"],
        )

    return supabase


@mcp.tool()
async def add_expense(
    amount: float,
    category: str,
    description: str = ""
) -> dict:
    """Add new expense record"""

    client = await get_supabase()

    response = await client.table("expenses").insert({
        "amount": amount,
        "category": category,
        "description": description,
    }).execute()

    return response.data[0]


app = mcp.http_app(path="/mcp")