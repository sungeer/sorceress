import asyncio
import os

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

# README documents 7788 as the default dev port; override with MCP_SERVER_URL
# if your server runs elsewhere (e.g. behind gunicorn on a different port).
SERVER_URL = os.getenv('MCP_SERVER_URL', 'http://127.0.0.1:7788/mcp')


async def call_echo(text: str):
    async with streamable_http_client(SERVER_URL) as streams:
        read_stream, write_stream = streams[0], streams[1]
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool('echo', {'text': text})
            for item in result.content:
                print(item.text)


if __name__ == '__main__':
    asyncio.run(call_echo('Hello MCP'))
