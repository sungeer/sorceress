import asyncio
from fastmcp import Client

client = Client('http://127.0.0.1:8848/mcp')


async def main():
    async with client:
        tools = await client.list_tools()
        print(tools)


asyncio.run(main())
