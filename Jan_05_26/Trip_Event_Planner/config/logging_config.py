import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from config.settings import settings

# Log directory & file
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

def setup_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)

    log_level = logging.DEBUG if settings.debug else logging.INFO
    logger.setLevel(log_level)

    # Prevent duplicate handlers on re-import
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s || %(levelname)s || %(name)s || %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5_000_000,   # 5 MB
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # Attach handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Avoid double logging via root logger
    logger.propagate = False

    return logger
