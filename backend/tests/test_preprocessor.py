"""Tests for data preprocessor"""
import pytest
import numpy as np
import pandas as pd
from app.ml.preprocessor import DataPreprocessor
from app.utils.data_fetcher import generate_mock_data

def test_preprocessor_initialization():
    """Test preprocessor initialization"""
    preprocessor = DataPreprocessor(lookback=60)
    assert preprocessor.lookback == 60
    assert preprocessor.scaler is not None

def test_prepare_data():
    """Test data preparation for LSTM"""
    # Generate mock data
    data = generate_mock_data(days=200)
    
    # Prepare data
    preprocessor = DataPreprocessor(lookback=60)
    X, y, scaler = preprocessor.prepare_data(data)
    
    # Check shapes
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 60  # lookback window
    assert X.shape[2] == 1   # single feature (Close price)
    assert len(X) == 200 - 60  # total - lookback

def test_inverse_transform():
    """Test inverse transform"""
    data = generate_mock_data(days=100)
    preprocessor = DataPreprocessor()
    X, y, scaler = preprocessor.prepare_data(data)
    
    # Transform and inverse transform
    original_values = data['Close'].values[-10:]
    inverse_values = preprocessor.inverse_transform(y[-10:])
    
    # Should be approximately equal
    assert inverse_values.shape[0] == 10
