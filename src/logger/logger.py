import logging
from logging import StreamHandler

from logger.formatter import get_formatter


def init_logger(log_level: str):
    logger = logging.getLogger()
    logHandler = StreamHandler()

    logHandler.setFormatter(get_formatter())
    logger.addHandler(logHandler)
    logger.setLevel(log_level)

    return logger
