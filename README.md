# MarketPredict 📈

Stock Market Price Prediction using Machine Learning (LSTM Neural Networks)

## Features

- 🤖 **LSTM-based predictions** for stock prices
- 📊 **Real-time data fetching** from Yahoo Finance
- 🔄 **Celery background tasks** for async processing
- 📡 **FastAPI** REST endpoints
- 🗄️ **PostgreSQL** database for storing data
- ⚡ **Redis** for caching and Celery broker
- 🐳 **Docker** containerization
- ✅ **Comprehensive tests** with pytest

## Project Structure

```
backend/
├── app/
│   ├── api/                  # API endpoints
│   │   ├── health.py        # Health check endpoints
│   │   └── predictions.py   # Prediction endpoints
│   ├── core/                # Core configuration
│   │   ├── config.py        # Settings from .env
│   │   └── celery_app.py    # Celery configuration
│   ├── database/            # Database layer
│   │   ├── db.py            # Database connection
│   │   └── models.py        # SQLAlchemy models
│   ├── ml/                  # Machine Learning
│   │   ├── preprocessor.py  # Data preprocessing
│   │   └── lstm_model.py    # LSTM model implementation
│   ├── tasks/               # Background tasks
│   │   └── worker_tasks.py  # Celery tasks
│   ├── utils/               # Utilities
│   │   ├── logging.py       # Logging setup
│   │   └── data_fetcher.py  # Yahoo Finance data fetching
│   └── main.py              # FastAPI app entry point
├── tests/                    # Test suite
│   ├── test_api.py
│   ├── test_config.py
│   ├── test_data_fetcher.py
│   └── test_preprocessor.py
├── requirements.txt          # Python dependencies
└── conftest.py              # Pytest configuration

Docker files:
├── Dockerfile               # Container image
├── docker-compose.yml       # Multi-container setup
└── .env.example            # Environment template
```

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Or Python 3.11+ with pip

### Using Docker (Recommended)

1. **Clone and setup**
```bash
git clone https://github.com/Ibrahim-Awad329/MarketPredict.git
cd MarketPredict
cp .env.example .env
```

2. **Start services**
```bash
docker-compose up -d
```

3. **Access API**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Local Development

1. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Setup .env file**
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Run tests**
```bash
pytest
```

5. **Start API**
```bash
uvicorn app.main:app --reload
```

6. **Start Celery worker** (in another terminal)
```bash
celery -A app.core.celery_app worker -l info
```

## API Endpoints

### Health Check
```bash
GET /health
GET /ready
```

### Predictions
```bash
# Get latest prediction for a stock
GET /api/v1/predictions/stock/{symbol}

# Generate new prediction
POST /api/v1/predictions/generate/{symbol}
```

## Configuration

Edit `.env` file to configure:

```env
# Database
DATABASE_URL=postgresql://postgres:postgres@db:5432/marketpredict

# Redis
REDIS_URL=redis://redis:6379/0

# Security
SECRET_KEY=your-secret-key
ALGORITHM=HS256

# API Keys (optional)
PROXY_API_KEY=your-proxy-key
TWOCAPTCHA_API_KEY=your-2captcha-key

# Model paths
MODEL_PATH=/app/models/lstm_model.joblib
SCALER_PATH=/app/models/scaler.joblib
```

## Data Fetching

Data is automatically fetched from Yahoo Finance using `yfinance` library:

```python
from app.utils.data_fetcher import fetch_stock_data

# Fetch data
data = fetch_stock_data('AAPL', period='1y')

# Or generate mock data for testing
from app.utils.data_fetcher import generate_mock_data
mock_data = generate_mock_data('AAPL', days=252)
```

## ML Pipeline

### Data Preprocessing
```python
from app.ml.preprocessor import DataPreprocessor

preprocessor = DataPreprocessor(lookback=60)
X, y, scaler = preprocessor.prepare_data(df)
```

### LSTM Model
```python
from app.ml.lstm_model import LSTMPredictor

# Build and train model
model = LSTMPredictor(lookback=60)
model.build_model(input_shape=(60, 1))
history = model.train(X_train, y_train, epochs=50)

# Make predictions
predictions = model.predict(X_test)

# Evaluate
metrics = model.evaluate(X_test, y_test)

# Save/Load
model.save('/path/to/model.joblib')
loaded_model = LSTMPredictor.load('/path/to/model.joblib')
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_api.py

# Run with verbose output
pytest -v
```

## Deployment

### Render Deployment

1. **Create Render account** at https://render.com

2. **Connect GitHub repository**

3. **Create Web Service**
   - Build command: `pip install -r backend/requirements.txt`
   - Start command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000`
   - Environment: Add variables from `.env`

4. **Create PostgreSQL Database**
   - Use Render's PostgreSQL service
   - Update `DATABASE_URL` in environment variables

5. **Create Redis Cache**
   - Use Render's Redis service
   - Update `REDIS_URL` in environment variables

6. **Deploy Celery Worker** (optional)
   - Create another Web Service with command: `cd backend && celery -A app.core.celery_app worker -l info`

### Environment Variables for Production

```
DATABASE_URL=postgresql://user:password@host:5432/db
REDIS_URL=redis://user:password@host:6379/0
SECRET_KEY=generate-strong-random-key
DEBUG=False
```

## Troubleshooting

### Database connection errors
- Ensure PostgreSQL is running
- Check DATABASE_URL format
- Verify credentials

### Redis connection errors
- Ensure Redis is running
- Check REDIS_URL format
- Verify port (default 6379)

### TensorFlow/LSTM errors
- Install TensorFlow: `pip install tensorflow`
- Check Python version (3.11+ recommended)

### Import errors
- Ensure PYTHONPATH includes backend directory
- Install all requirements: `pip install -r requirements.txt`

## Future Improvements

- [ ] Add authentication/authorization
- [ ] Implement WebSocket for real-time updates
- [ ] Add more ML models (ARIMA, GRU, Attention)
- [ ] Implement model versioning
- [ ] Add monitoring and alerting
- [ ] Create web dashboard
- [ ] Add portfolio analysis features

## License

MIT License - See LICENSE file

## Support

For issues and questions, please open a GitHub issue.
