import logging
from logging.handlers import RotatingFileHandler
# import pprint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    "appl.log",
    encoding="utf-8",
    mode="a",
    maxBytes=1024,
    backupCount=1,
)


def show_only_debug(record):
    # print(record.levelname)
    return record.levelname == "DEBUG"


formatter = logging.Formatter(
    fmt="{asctime}:{levelname}:{name}:{message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
console_handler.addFilter(show_only_debug)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# pprint.pprint(logger.handlers)
logger.warning("This is a warning message")
logger.debug("This is a debug message")
for i in range(30):
    logger.debug(i)
    
logger.info("program end")
