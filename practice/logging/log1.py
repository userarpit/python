import logging
import sys
logger = logging.getLogger(__name__)


logging.basicConfig(
    filename="appl.log",
    encoding="utf-8",
    filemode="a",
    level=logging.DEBUG,
    format="{asctime}:{levelname}:{name}:{message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is an warning message")
index = 10
logging.critical(f"This is an critical message {index=}")

try:
    1 / 0
except ZeroDivisionError:
    logging.debug("An error occurred", exc_info=True)
    # logging.exception("An exception occurred")

logger.warning("This is a debug message")
