import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

SERVER_URL = 'http://127.0.0.1:7788/mcp'


async def list_tools():
    async with streamable_http_client(SERVER_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.list_tools()
            print(f'共 {len(result.tools)} 个工具:')
            print()
            for tool in result.tools:
                print(f'- {tool.name}: {tool.description}')


if __name__ == '__main__':
    asyncio.run(list_tools())
