import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)  
LOG_FILE = LOG_DIR / "app.log"

def setup_logger(name : str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers in case of re-imports
    if logger.handlers:
        return logger

    # Log message format
    formatter = logging.Formatter(
        fmt="%(asctime)s || %(levelname)s || %(name)s || %(message)s"
    )

    # File handler (with rotation)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5_000_000,  # 5 MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
