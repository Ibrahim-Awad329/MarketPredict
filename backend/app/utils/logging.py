"""Logging configuration"""
import logging
import structlog
from pythonjsonlogger import jsonlogger

def setup_logging():
    """Configure structured logging"""
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Setup root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Console handler with JSON formatter
    console_handler = logging.StreamHandler()
    json_formatter = jsonlogger.JsonFormatter()
    console_handler.setFormatter(json_formatter)
    root_logger.addHandler(console_handler)
