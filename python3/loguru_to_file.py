from loguru import logger

logger.add(
    "log.txt",
    rotation="1 GB",
    level="TRACE",
    backtrace=True,
    diagnose=True,
    enqueue=True,  # Safe for multiprocessing/threading
)
