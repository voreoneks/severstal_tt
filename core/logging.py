import sys

from loguru import logger as app_logger


app_logger.add(
    sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
)
