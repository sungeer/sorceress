import logging

logger = logging.getLogger(__name__)


async def echo(text: str) -> str:
    """原样返回输入文本，用于验证 MCP 链路是否打通

    Args:
        text: 任意输入文本，函数不做处理，原样返回
    """
    logger.info('this is tool [echo]')
    return text
