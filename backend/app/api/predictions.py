"""Prediction endpoints"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.database.models import Prediction
from app.utils.data_fetcher import fetch_stock_data
from datetime import datetime, timedelta
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/predictions", tags=["predictions"])

@router.get("/stock/{symbol}")
async def get_stock_prediction(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Get stock price prediction for a symbol
    
    Args:
        symbol: Stock symbol (e.g., AAPL)
        db: Database session
    
    Returns:
        Prediction data
    """
    try:
        # Fetch recent predictions from database
        prediction = db.query(Prediction).filter(
            Prediction.symbol == symbol
        ).order_by(Prediction.created_at.desc()).first()
        
        if not prediction:
            raise HTTPException(status_code=404, detail=f"No predictions found for {symbol}")
        
        return {
            "symbol": prediction.symbol,
            "predicted_price": prediction.predicted_price,
            "confidence": prediction.confidence,
            "prediction_date": prediction.prediction_date,
            "model_version": prediction.model_version
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting prediction for {symbol}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/generate/{symbol}")
async def generate_prediction(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Generate a new prediction for a stock symbol
    
    Args:
        symbol: Stock symbol
        db: Database session
    
    Returns:
        Generated prediction
    """
    try:
        # Fetch stock data
        data = fetch_stock_data(symbol, period="1y")
        if data is None:
            raise HTTPException(status_code=400, detail=f"Could not fetch data for {symbol}")
        
        # TODO: Run prediction model
        # For now, return mock prediction
        mock_prediction = data['Close'].iloc[-1] * 1.05
        
        # Save to database
        prediction = Prediction(
            symbol=symbol,
            prediction_date=datetime.now() + timedelta(days=1),
            predicted_price=mock_prediction,
            confidence=0.85,
            model_version="v1.0.0"
        )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
        
        return {
            "status": "success",
            "symbol": symbol,
            "predicted_price": prediction.predicted_price,
            "confidence": prediction.confidence
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating prediction for {symbol}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
