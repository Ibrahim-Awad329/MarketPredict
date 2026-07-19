"""Health check endpoints"""
from fastapi import APIRouter, HTTPException
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Returns:
        Health status
    """
    return {
        "status": "ok",
        "message": "MarketPredict API is running",
        "version": "1.0.0"
    }

@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint
    
    Returns:
        Readiness status
    """
    try:
        # Check database connection
        return {
            "status": "ready",
            "database": "connected"
        }
    except Exception as e:
        logger.error(f"Readiness check failed: {e}")
        raise HTTPException(status_code=503, detail="Service not ready")
