"""Celery worker tasks"""
from celery import shared_task
import structlog
import logging
from app.utils.data_fetcher import fetch_stock_data
from app.ml.preprocessor import DataPreprocessor

logger = logging.getLogger(__name__)
log = structlog.get_logger()

@shared_task(bind=True, max_retries=3)
def fetch_stock_data_task(self, symbol: str, period: str = "1y"):
    """
    Background task to fetch stock data
    
    Args:
        symbol: Stock symbol to fetch
        period: Period to fetch
    
    Returns:
        Status message
    """
    try:
        log.info("Fetching stock data", symbol=symbol, period=period)
        data = fetch_stock_data(symbol, period=period)
        
        if data is not None:
            return {"status": "success", "symbol": symbol, "records": len(data)}
        else:
            return {"status": "failed", "symbol": symbol, "error": "No data fetched"}
    
    except Exception as exc:
        log.error("Error in fetch_stock_data_task", error=str(exc))
        self.retry(exc=exc, countdown=60)

@shared_task
def test_task(name: str) -> str:
    """
    Test task
    
    Args:
        name: Name parameter
    
    Returns:
        Status message
    """
    log.info("Test task started", name=name)
    return f"Hello {name}, task completed"
