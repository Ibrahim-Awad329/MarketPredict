"""LSTM model for stock price prediction"""
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import logging
from typing import Tuple, Optional
import joblib
import os

logger = logging.getLogger(__name__)

# Try to import TensorFlow, but don't fail if not available
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense, Dropout
    from tensorflow.keras.optimizers import Adam
    TENSORFLOW_AVAILABLE = True
except ImportError:
    TENSORFLOW_AVAILABLE = False
    logger.warning("TensorFlow not available. Install it with: pip install tensorflow")

class LSTMPredictor:
    """LSTM model for time series prediction"""
    
    def __init__(self, lookback: int = 60):
        self.lookback = lookback
        self.model = None
        self.history = None
    
    def build_model(self, input_shape: Tuple[int, int]) -> Optional['LSTMPredictor']:
        """
        Build LSTM model
        
        Args:
            input_shape: Shape of input data (lookback, features)
        
        Returns:
            Self for chaining
        """
        if not TENSORFLOW_AVAILABLE:
            logger.warning("Cannot build LSTM model: TensorFlow not installed")
            return None
        
        try:
            self.model = Sequential([
                LSTM(50, activation='relu', input_shape=input_shape, return_sequences=True),
                Dropout(0.2),
                LSTM(50, activation='relu', return_sequences=True),
                Dropout(0.2),
                LSTM(25, activation='relu'),
                Dropout(0.2),
                Dense(1)
            ])
            
            self.model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
            logger.info(f"LSTM model built with shape {input_shape}")
            return self
        
        except Exception as e:
            logger.error(f"Error building LSTM model: {e}")
            raise
    
    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        epochs: int = 50,
        batch_size: int = 32,
        validation_split: float = 0.2
    ) -> dict:
        """
        Train the model
        
        Args:
            X_train: Training features
            y_train: Training labels
            epochs: Number of epochs
            batch_size: Batch size
            validation_split: Validation split ratio
        
        Returns:
            Training history
        """
        if self.model is None:
            logger.error("Model not built. Call build_model first.")
            return {}
        
        try:
            self.history = self.model.fit(
                X_train, y_train,
                epochs=epochs,
                batch_size=batch_size,
                validation_split=validation_split,
                verbose=1
            )
            logger.info("Model training completed")
            return self.history.history
        
        except Exception as e:
            logger.error(f"Error training model: {e}")
            raise
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions
        
        Args:
            X: Input features
        
        Returns:
            Predictions
        """
        if self.model is None:
            logger.error("Model not built")
            return np.array([])
        
        return self.model.predict(X)
    
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> dict:
        """
        Evaluate model
        
        Args:
            X_test: Test features
            y_test: Test labels
        
        Returns:
            Evaluation metrics
        """
        if self.model is None:
            logger.error("Model not built")
            return {}
        
        try:
            predictions = self.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            rmse = np.sqrt(mse)
            r2 = r2_score(y_test, predictions)
            
            metrics = {'mse': mse, 'rmse': rmse, 'r2': r2}
            logger.info(f"Model evaluation: {metrics}")
            return metrics
        
        except Exception as e:
            logger.error(f"Error evaluating model: {e}")
            return {}
    
    def save(self, filepath: str):
        """Save model to disk"""
        try:
            os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
            joblib.dump(self, filepath)
            logger.info(f"Model saved to {filepath}")
        except Exception as e:
            logger.error(f"Error saving model: {e}")
    
    @staticmethod
    def load(filepath: str) -> Optional['LSTMPredictor']:
        """Load model from disk"""
        try:
            model = joblib.load(filepath)
            logger.info(f"Model loaded from {filepath}")
            return model
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            return None
