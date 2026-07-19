# MarketPredict - تقرير المشروع الشامل 📊

## 🎯 ملخص المشروع

**MarketPredict** هو تطبيق ويب متكامل للتنبؤ بأسعار الأسهم باستخدام شبكات **LSTM (Long Short-Term Memory)** العصبية العميقة. المشروع يجمع بين:
- **جلب البيانات التلقائي** من Yahoo Finance
- **معالجة البيانات وتطبيع** البيانات بشكل احترافي
- **نماذج Machine Learning** متقدمة للتنبؤ
- **API REST** سريعة وآمنة بـ FastAPI
- **معالجة مهام خلفية** غير متزامنة بـ Celery
- **قاعدة بيانات** PostgreSQL وتخزين مؤقت Redis

---

## 📁 هيكل المشروع

### البنية الأساسية المحسّنة:

```
MarketPredict/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    ✨ نقطة الدخول الرئيسية للـ FastAPI
│   │   │
│   │   ├── core/                      🔧 إعدادات وتكوين
│   │   │   ├── __init__.py
│   │   │   ├── config.py              ⚙️ إعدادات من متغيرات البيئة
│   │   │   └── celery_app.py          🔄 إعداد Celery للمهام الخلفية
│   │   │
│   │   ├── database/                  💾 طبقة قاعدة البيانات
│   │   │   ├── __init__.py
│   │   │   ├── db.py                  🔗 اتصال SQLAlchemy والجلسات
│   │   │   └── models.py              📊 نماذج SQLAlchemy (StockData, Predictions, ModelMetadata)
│   │   │
│   │   ├── api/                       🌐 نقاط نهاية REST API
│   │   │   ├── __init__.py
│   │   │   ├── health.py              💚 فحوصات الصحة والجاهزية
│   │   │   └── predictions.py         🔮 التنبؤات بأسعار الأسهم
│   │   │
│   │   ├── ml/                        🤖 نماذج التعلم الآلي
│   │   │   ├── __init__.py
│   │   │   ├── preprocessor.py        📈 معالجة البيانات للـ LSTM
│   │   │   └── lstm_model.py          🧠 نموذج LSTM الرئيسي
│   │   │
│   │   ├── tasks/                     ⚡ مهام Celery الخلفية
│   │   │   ├── __init__.py
│   │   │   └── worker_tasks.py        🔄 جلب البيانات والتنبؤ بشكل غير متزامن
│   │   │
│   │   └── utils/                     🛠️ أدوات ومساعدات
│   │       ├── __init__.py
│   │       ├── logging.py             📝 إعداد السجلات المنظمة
│   │       └── data_fetcher.py        🌍 جلب البيانات من Yahoo Finance
│   │
│   ├── tests/                         ✅ اختبارات شاملة
│   │   ├── __init__.py
│   │   ├── test_api.py                🧪 اختبار نقاط النهاية
│   │   ├── test_config.py             🧪 اختبار الإعدادات
│   │   ├── test_data_fetcher.py       🧪 اختبار جلب البيانات
│   │   └── test_preprocessor.py       🧪 اختبار معالجة البيانات
│   │
│   ├── requirements.txt               📦 جميع المكتبات المطلوبة
│   └── conftest.py                    🧪 إعداد pytest
│
├── Dockerfile                         🐳 بناء صورة Docker
├── docker-compose.yml                 🐳 تعريف الخدمات المتعددة
├── .env.example                       📋 مثال لمتغيرات البيئة
├── .gitignore                         🚫 ملفات التجاهل
├── README.md                          📖 التوثيق الرئيسي
└── REPORT.md                          📄 هذا الملف
```

---

## 📊 وظيفة كل ملف

### 🎯 `app/main.py` - نقطة الدخول الرئيسية
```python
# ينشئ تطبيق FastAPI
# يعدّ قاعدة البيانات عند البدء
# يسجل جميع الأخطاء والأحداث
# يوفر نقاط نهاية صحية للمراقبة
```

### ⚙️ `app/core/config.py` - إعدادات التطبيق
```python
# يقرأ متغيرات البيئة من .env
# ينظم جميع الإعدادات في مكان واحد
# يستخدم Pydantic للتحقق من الأنواع
```

### 💾 `app/database/db.py` - الاتصال بقاعدة البيانات
```python
# ينشئ محرك SQLAlchemy
# يدير جلسات قاعدة البيانات
# ينفذ نمط Dependency Injection
```

### 📊 `app/database/models.py` - نماذج البيانات
```python
# StockData: بيانات الأسهم التاريخية (Date, Open, High, Low, Close, Volume)
# Prediction: التنبؤات المحفوظة (predicted_price, confidence)
# ModelMetadata: معلومات النموذج (version, accuracy, RMSE)
```

### 🌍 `app/utils/data_fetcher.py` - جلب البيانات
```python
# fetch_stock_data(): جلب البيانات من Yahoo Finance
# fetch_multiple_symbols(): جلب بيانات عدة أسهم
# generate_mock_data(): توليد بيانات وهمية للاختبار
```

### 📈 `app/ml/preprocessor.py` - معالجة البيانات
```python
# ينسّق البيانات (تطبيع Normalization) بين 0 و 1
# ينشئ نوافذ زمنية (Sequences) لـ LSTM
# يحفظ التطبيع للاستخدام لاحقاً
```

### 🧠 `app/ml/lstm_model.py` - نموذج LSTM
```python
# بناء شبكة LSTM بـ 3 طبقات + Dropout
# تدريب النموذج على البيانات التاريخية
# التنبؤ بأسعار المستقبل
# حساب المقاييس (RMSE, R²)
```

### ⚡ `app/tasks/worker_tasks.py` - المهام الخلفية
```python
# fetch_stock_data_task(): جلب البيانات بشكل غير متزامن
# test_task(): مهمة اختبار بسيطة
```

### 🌐 `app/api/health.py` - فحوصات الصحة
```python
# /health: هل التطبيق يعمل؟
# /ready: هل قاعدة البيانات متصلة؟
```

### 🔮 `app/api/predictions.py` - التنبؤات
```python
# GET /api/v1/predictions/stock/{symbol}: الحصول على آخر تنبؤ
# POST /api/v1/predictions/generate/{symbol}: توليد تنبؤ جديد
```

---

## 🌐 جلب البيانات التلقائي

### كيفية عمل جلب البيانات:

```python
# 1. من Yahoo Finance (الخيار الأول - أفضل)
from app.utils.data_fetcher import fetch_stock_data
data = fetch_stock_data('AAPL', period='1y')

# 2. بيانات وهمية للاختبار (الخيار الثاني)
from app.utils.data_fetcher import generate_mock_data
mock_data = generate_mock_data('AAPL', days=252)
```

### البيانات المسترجعة:
```
Date        Open      High      Low       Close     Volume
2024-01-01  150.50    151.20    150.10    150.80    1000000
2024-01-02  150.80    152.30    150.50    152.10    1200000
...
```

### المكتبات المستخدمة:
- **yfinance**: جلب البيانات من Yahoo Finance (مجاني وموثوق)
- **pandas**: معالجة البيانات في DataFrames
- **numpy**: حسابات رياضية سريعة

---

## 🤖 خط أنابيب ML (Machine Learning Pipeline)

### 1️⃣ جلب البيانات
```
Yahoo Finance → DataFrame
```

### 2️⃣ معالجة البيانات
```python
DataPreprocessor:
- تطبيع البيانات (0-1)
- إنشاء نوافذ زمنية (lookback=60)
- فصل المدخلات والمخرجات
```

### 3️⃣ بناء النموذج
```python
LSTM Architecture:
Input (60, 1) 
  ↓
LSTM(50) + Dropout(0.2)
  ↓
LSTM(50) + Dropout(0.2)
  ↓
LSTM(25) + Dropout(0.2)
  ↓
Dense(1)
  ↓
Output (تنبؤ السعر)
```

### 4️⃣ التدريب
```python
model.train(X_train, y_train, epochs=50, batch_size=32)
```

### 5️⃣ التنبؤ
```python
predictions = model.predict(X_test)
```

### 6️⃣ التقييم
```python
metrics = model.evaluate(X_test, y_test)
# RMSE: root mean squared error
# R²: coefficient of determination
```

---

## ⚙️ متغيرات البيئة المطلوبة (.env)

### قاعدة البيانات
```
DATABASE_URL=postgresql://postgres:postgres@db:5432/marketpredict
POSTGRES_PASSWORD=postgres
```

### Redis والمهام الخلفية
```
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/1
```

### الأمان
```
SECRET_KEY=super_secret_key_change_me_in_production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### مفاتيح API (اختيارية)
```
PROXY_API_KEY=your-proxy-key
TWOCAPTCHA_API_KEY=your-captcha-key
OPENAI_API_KEY=your-openai-key
```

### نماذج ML
```
MODEL_PATH=/app/models/lstm_model.joblib
SCALER_PATH=/app/models/scaler.joblib
```

### إعدادات التطبيق
```
APP_NAME=MarketPredict API
DEBUG=False
```

---

## ✅ اختبار المشروع

### تشغيل الاختبارات:
```bash
# تشغيل جميع الاختبارات
pytest

# مع نسبة التغطية
pytest --cov=app tests/

# اختبار واحد
pytest tests/test_api.py

# بتفاصيل
pytest -v
```

### الاختبارات المتوفرة:
✅ `test_api.py` - اختبار نقاط النهاية
✅ `test_config.py` - اختبار الإعدادات
✅ `test_data_fetcher.py` - اختبار جلب البيانات
✅ `test_preprocessor.py` - اختبار معالجة البيانات

---

## 🚀 تشغيل المشروع

### الطريقة 1️⃣: Docker (موصى به)

```bash
# 1. استنساخ المشروع
git clone https://github.com/Ibrahim-Awad329/MarketPredict.git
cd MarketPredict

# 2. نسخ متغيرات البيئة
cp .env.example .env

# 3. بدء جميع الخدمات
docker-compose up -d

# 4. التحقق من الخدمات
docker-compose logs -f

# 5. الوصول للـ API
curl http://localhost:8000/health
```

### الطريقة 2️⃣: التطوير المحلي

```bash
# 1. البيئة الافتراضية
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو على Windows:
venv\Scripts\activate

# 2. تثبيت المكتبات
cd backend
pip install -r requirements.txt

# 3. إعداد .env
cp .env.example .env

# 4. تشغيل الـ API
uvicorn app.main:app --reload

# 5. في terminal آخر - تشغيل Celery
celery -A app.core.celery_app worker -l info

# 6. الوصول للـ API
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

---

## 📱 استخدام API

### فحص الصحة
```bash
curl http://localhost:8000/health
# Response:
# {
#   "status": "ok",
#   "message": "MarketPredict API is running",
#   "version": "1.0.0"
# }
```

### الحصول على تنبؤ
```bash
curl http://localhost:8000/api/v1/predictions/stock/AAPL
# Response:
# {
#   "symbol": "AAPL",
#   "predicted_price": 185.50,
#   "confidence": 0.85,
#   "prediction_date": "2024-01-15T10:30:00",
#   "model_version": "v1.0.0"
# }
```

### توليد تنبؤ جديد
```bash
curl -X POST http://localhost:8000/api/v1/predictions/generate/AAPL
# Response:
# {
#   "status": "success",
#   "symbol": "AAPL",
#   "predicted_price": 185.50,
#   "confidence": 0.85
# }
```

---

## 🌍 رفع على Render

### خطوات النشر:

#### 1️⃣ إعداد الريبو
```bash
# Push الكود إلى GitHub
git add .
git commit -m "Complete MarketPredict setup"
git push origin fix/complete-refactor
```

#### 2️⃣ إنشاء Web Service على Render

**الإعدادات:**
- **Repository**: Ibrahim-Awad329/MarketPredict
- **Branch**: fix/complete-refactor
- **Build Command**: `pip install -r backend/requirements.txt`
- **Start Command**: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000`

#### 3️⃣ إضافة متغيرات البيئة

في Render Dashboard:
```
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
SECRET_KEY=<generate-random>
DEBUG=False
```

#### 4️⃣ إنشاء قاعدة بيانات PostgreSQL

- في Render: Database → PostgreSQL
- Copy الـ Internal Database URL
- Paste في `DATABASE_URL`

#### 5️⃣ إنشاء Redis Cache

- في Render: Cache → Redis
- Copy الـ Redis URL
- Paste في `REDIS_URL`

#### 6️⃣ (اختياري) نشر Celery Worker

إنشاء Web Service آخر:
```
Start Command: cd backend && celery -A app.core.celery_app worker -l info
```

#### 7️⃣ Deploy
- اضغط على Deploy
- انتظر حتى ينتهي البناء (~5 دقائق)
- الـ API جاهزة على: `https://your-app.onrender.com`

---

## 🔧 المشاكل التي تم إصلاحها

### ❌ المشكلة 1: الهيكل الفوضوي
```
❌ قبل:  backend/app/backend/app/backend/app/...
✅ بعد:  backend/app/ (هيكل نظيف ومنظم)
```

### ❌ المشكلة 2: ملفات ناقصة
```
❌ قبل:  لا توجد نماذج ML، لا توجد معالجة بيانات
✅ بعد:  نماذج LSTM كاملة، preprocessor، data_fetcher
```

### ❌ المشكلة 3: بدون اختبارات
```
❌ قبل:  اختبارات وهمية فقط
✅ بعد:  اختبارات شاملة مع pytest
```

### ❌ المشكلة 4: بدون توثيق
```
❌ قبل:  README بسيط جداً
✅ بعد:  توثيق شامل + تقرير مفصل
```

### ❌ المشكلة 5: بدون معالجة أخطاء
```
❌ قبل:  لا توجد معالجة exceptions
✅ بعد:  معالجة شاملة + logging منظم
```

---

## 📦 المكتبات المثبتة

```
# Web Framework
fastapi==0.115.0
uvicorn[standard]==0.30.6

# Data & ML
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
joblib==1.4.2
yfinance==0.2.38

# Database
sqlalchemy==2.0.35
psycopg2-binary==2.9.10

# Caching & Queue
redis==5.1.1
celery==5.4.0

# Configuration
pydantic==2.9.2
pydantic-settings==2.1.0
python-dotenv==1.0.1

# Logging
structlog==24.4.4
python-json-logger==2.0.7

# Testing
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.25.2

# (اختيارية) Deep Learning
# tensorflow==2.15.0
# keras==2.15.0
```

---

## 🎯 الحاجات الناقصة / المستقبلية

### 🔐 الأمان
- [ ] إضافة JWT Authentication
- [ ] Role-based access control (RBAC)
- [ ] Rate limiting

### 📊 الميزات
- [ ] دعم نماذج ML متعددة (ARIMA, GRU)
- [ ] نسخ نماذج متعددة
- [ ] تقارير تفصيلية للأداء

### 🎨 الواجهة
- [ ] لوحة تحكم ويب (Dashboard)
- [ ] رسوم بيانية تفاعلية
- [ ] WebSocket للتحديثات الحية

### 🔔 المراقبة
- [ ] Monitoring مع Prometheus
- [ ] Alerting مع email/Slack
- [ ] Health checks محسّنة

---

## 🐛 استكشاف الأخطاء

### خطأ: "ModuleNotFoundError: No module named 'app'"
```bash
# الحل:
cd backend
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
uvicorn app.main:app --reload
```

### خطأ: "could not connect to server"
```bash
# تحقق من:
1. هل PostgreSQL يعمل؟
2. هل DATABASE_URL صحيح؟
3. هل الكلمة السرية صحيحة؟

# جرب:
docker-compose logs db
```

### خطأ: "Connection refused" Redis
```bash
# تحقق من:
1. هل Redis يعمل؟
2. هل REDIS_URL صحيح؟

# جرب:
docker-compose logs redis
```

### خطأ: "No module named tensorflow"
```bash
# الحل:
pip install tensorflow
# أو للـ CPU فقط:
pip install tensorflow-cpu
```

---

## 📞 التواصل والدعم

- 📧 البريد الإلكتروني: awd11846@gmail.com
- 🐙 GitHub: https://github.com/Ibrahim-Awad329
- 💬 للتبليغ عن مشاكل: استخدم GitHub Issues

---

## 📄 الترخيص

هذا المشروع مرخص تحت **MIT License** - انظر ملف LICENSE

---

**تم إعداد هذا التقرير بواسطة GitHub Copilot** 🤖
**آخر تحديث: 2024** 📅
