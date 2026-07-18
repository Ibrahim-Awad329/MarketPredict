"""Utility to fetch stock data from Yahoo Finance"""
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import logging
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

def fetch_stock_data(
    symbol: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    period: str = "1y"
) -> Optional[pd.DataFrame]:
    """
    Fetch historical stock data from Yahoo Finance
    
    Args:
        symbol: Stock symbol (e.g., 'AAPL')
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        period: Period if dates not specified ('1y', '6mo', etc.)
    
    Returns:
        DataFrame with OHLCV data or None if error
    """
    try:
        ticker = yf.Ticker(symbol)
        
        if start_date and end_date:
            data = ticker.history(start=start_date, end=end_date)
        else:
            data = ticker.history(period=period)
        
        if data.empty:
            logger.warning(f"No data fetched for {symbol}")
            return None
        
        data = data.reset_index()
        logger.info(f"Fetched {len(data)} records for {symbol}")
        return data
    
    except Exception as e:
        logger.error(f"Error fetching data for {symbol}: {e}")
        return None

def fetch_multiple_symbols(symbols: list, period: str = "1y") -> dict:
    """
    Fetch data for multiple symbols
    
    Args:
        symbols: List of stock symbols
        period: Period to fetch
    
    Returns:
        Dictionary with symbol as key and DataFrame as value
    """
    data = {}
    for symbol in symbols:
        df = fetch_stock_data(symbol, period=period)
        if df is not None:
            data[symbol] = df
    return data

def generate_mock_data(symbol: str = "AAPL", days: int = 252) -> pd.DataFrame:
    """
    Generate mock stock data for testing
    
    Args:
        symbol: Stock symbol
        days: Number of days of data
    
    Returns:
        DataFrame with mock OHLCV data
    """
    import numpy as np
    
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    close = np.cumsum(np.random.randn(days)) + 100
    
    data = pd.DataFrame({
        'Date': dates,
        'Open': close + np.random.randn(days),
        'High': close + abs(np.random.randn(days)),
        'Low': close - abs(np.random.randn(days)),
        'Close': close,
        'Volume': np.random.randint(1000000, 5000000, days),
        'Adj Close': close
    })
    
    return data
