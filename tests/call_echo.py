import asyncio

from fastmcp import Client

client = Client('http://127.0.0.1:8848/mcp')


async def main():
    async with client:
        result = await client.call_tool('echo', {'text': 'hello'})
        print(result)


asyncio.run(main())
