Dynamic pricing 
## 🚀 Live Demo

### 🌐 Live Application

https://priceflow-ienxubhguinhlk7iylrvka.streamlit.app/

### 🎥 Live Demo Video

https://drive.google.com/file/d/1L2OPPIC_yLT7m5ZefEhNRXriWkiftEHG/view?usp=sharing

\## 1. Project Overview

PriceFlow is a dynamic pricing prototype for e-commerce.



It uses demand, inventory level, competitor pricing, discounts, and market conditions to recommend a suitable selling price.



The project combines machine learning, rule-based pricing logic, FastAPI, Streamlit, and Redis.



\## 2. Problem Statement



Traditional e-commerce pricing may remain fixed even when demand, inventory, or competitor prices change.



PriceFlow aims to make pricing more responsive to changing market conditions.



\## 3. Main Features



\- Demand analysis and prediction

\- Feature engineering

\- Dynamic price recommendation

\- Competitor price adjustment

\- Price elasticity analysis

\- Revenue optimization prototype

\- Inventory-based pricing adjustment

\- Flash-sale detection

\- Real-time pricing simulation

\- XGBoost pricing model

\- TensorFlow demand model

\- Monitoring and alerts

\- FastAPI REST API

\- Redis price storage

\- Streamlit dashboard



\## 4. Technology Stack



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- XGBoost

\- TensorFlow

\- FastAPI

\- Uvicorn

\- Streamlit

\- Redis

\- Matplotlib

\- Seaborn



\## 5. Dataset



The project uses a retail inventory and demand dataset containing information such as:



\- Date

\- Store ID

\- Product ID

\- Category

\- Region

\- Inventory Level

\- Units Sold

\- Units Ordered

\- Price

\- Discount

\- Competitor Pricing

\- Seasonality

\- Demand



The dataset contains 76,000 records and 16 columns.



\## 6. System Flow



User Input

↓

Streamlit Dashboard

↓

FastAPI

↓

Pricing Logic

↓

Demand + Inventory + Competitor Price

↓

Recommended Price

↓

Redis Storage

↓

Result shown in Dashboard



\## 7. Example



Example input:



\- Product ID: TEST\_FINAL

\- Demand: 200

\- Inventory: 50

\- Current Price: ₹100

\- Competitor Price: ₹110



The system identifies high demand with limited inventory and recommends:



Recommended Price: ₹110.00



The recommendation is also stored in Redis.



\## 8. API



\### Endpoint



POST /recommend-price



\### Example Request



```json

{

&#x20;   "product\_id": "TEST\_FINAL",

&#x20;   "demand": 200,

&#x20;   "inventory": 50,

&#x20;   "current\_price": 100,

&#x20;   "competitor\_price": 110

}

