"""Data preprocessing for ML models"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from typing import Tuple, Optional
import logging

logger = logging.getLogger(__name__)

class DataPreprocessor:
    """Handle data preprocessing for time series"""
    
    def __init__(self, lookback: int = 60):
        self.lookback = lookback
        self.scaler = MinMaxScaler(feature_range=(0, 1))
    
    def prepare_data(self, df: pd.DataFrame, target_column: str = 'Close') -> Tuple[np.ndarray, np.ndarray, MinMaxScaler]:
        """
        Prepare data for LSTM model
        
        Args:
            df: DataFrame with stock data
            target_column: Column to predict
        
        Returns:
            Tuple of (X, y, scaler)
        """
        try:
            # Extract target data
            data = df[target_column].values.reshape(-1, 1)
            
            # Normalize data
            scaled_data = self.scaler.fit_transform(data)
            
            # Create sequences
            X, y = [], []
            for i in range(len(scaled_data) - self.lookback):
                X.append(scaled_data[i:i + self.lookback])
                y.append(scaled_data[i + self.lookback])
            
            X = np.array(X)
            y = np.array(y)
            
            logger.info(f"Data prepared: X shape {X.shape}, y shape {y.shape}")
            return X, y, self.scaler
        
        except Exception as e:
            logger.error(f"Error preparing data: {e}")
            raise
    
    def inverse_transform(self, data: np.ndarray) -> np.ndarray:
        """Inverse transform scaled predictions"""
        return self.scaler.inverse_transform(data)
