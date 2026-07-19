"""Tests for data fetcher"""
import pytest
import pandas as pd
from app.utils.data_fetcher import fetch_stock_data, generate_mock_data, fetch_multiple_symbols

def test_generate_mock_data():
    """Test mock data generation"""
    data = generate_mock_data("AAPL", days=100)
    
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 100
    assert all(col in data.columns for col in ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

def test_mock_data_values():
    """Test mock data values are reasonable"""
    data = generate_mock_data("AAPL", days=50)
    
    # Check that High >= Low
    assert all(data['High'] >= data['Low'])
    # Check volume is positive
    assert all(data['Volume'] > 0)

def test_fetch_multiple_symbols():
    """Test fetching multiple symbols (with mock data)"""
    # Using mock data since we can't rely on external API
    symbols = ['AAPL', 'MSFT']
    # This would need mock integration in real test
    pass
