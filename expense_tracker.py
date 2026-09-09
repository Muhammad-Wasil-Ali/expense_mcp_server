from fastmcp import FastMCP
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

mcp=FastMCP("Expense Tracker")

supabase=create_client(os.getenv("SUPABASE_URL"),os.getenv("SUPABASE_SERVICE_KEY"))




# add expense 
@mcp.tool()
async def add_expense(amount:float,category:str,description:str="")->dict:
    """Add new expense record"""
    
    response=await supabase.table("expenses").insert({"amount":amount,"category":category,"description":description}).execute()
    
    return response.data[0]



if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8081)
