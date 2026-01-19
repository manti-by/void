import logging.config

from settings import LOGGING


logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


def log_info(msg: str) -> str:
    logger.info(msg)
    return msg


if __name__ == "__main__":
    log_info("Hello world")
