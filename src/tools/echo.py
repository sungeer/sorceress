from loguru import logger

description = '原样返回输入文本，用于验证 MCP 链路是否打通'


async def echo(text: str) -> str:
    """原样返回输入文本，用于验证 MCP 链路是否打通"""
    logger.info('this is tool [echo]')
    return text
