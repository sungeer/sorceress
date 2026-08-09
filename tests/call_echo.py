import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

SERVER_URL = 'http://127.0.0.1:8848/mcp'


async def call_echo(text: str):
    async with streamable_http_client(SERVER_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool('echo', {'text': text})
            for item in result.content:
                print(item.text)


if __name__ == '__main__':
    asyncio.run(call_echo('Hello MCP'))
