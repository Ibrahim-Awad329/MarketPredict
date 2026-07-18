"""Database models for MarketPredict"""
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from app.database.db import Base
from datetime import datetime

class StockData(Base):
    """Stock market data model"""
    __tablename__ = "stock_data"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), index=True, nullable=False)
    date = Column(DateTime, nullable=False)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Prediction(Base):
    """Model predictions"""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), index=True, nullable=False)
    prediction_date = Column(DateTime, nullable=False)
    predicted_price = Column(Float, nullable=False)
    confidence = Column(Float, nullable=True)
    actual_price = Column(Float, nullable=True)
    model_version = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class ModelMetadata(Base):
    """ML model metadata"""
    __tablename__ = "model_metadata"
    
    id = Column(Integer, primary_key=True, index=True)
    version = Column(String(50), unique=True, nullable=False)
    model_type = Column(String(50), nullable=False)
    accuracy = Column(Float, nullable=True)
    rmse = Column(Float, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
