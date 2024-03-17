import logging
from pathlib import Path


def get(name: str, logfile=Path(__file__).parent/'.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    _handler = logging.FileHandler(str(logfile))
    _handler.setLevel(logging.DEBUG)
    _formatter = logging.Formatter(
        '%(levelname)-9s  %(asctime)s  [%(name)s] %(message)s')
    _handler.setFormatter(_formatter)
    logger.addHandler(_handler)
    return logger
