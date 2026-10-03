from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# Allow imports from src folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from redis_cache import save_price


# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------

app = FastAPI(
    title="PriceFlow API",
    description="Dynamic Pricing Engine API",
    version="1.0"
)


# --------------------------------------------------
# REQUEST MODEL
# --------------------------------------------------

class PricingRequest(BaseModel):
    product_id: str
    demand: float
    inventory: float
    current_price: float
    competitor_price: float


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "PriceFlow Dynamic Pricing API is running"
    }


# --------------------------------------------------
# PRICE RECOMMENDATION
# --------------------------------------------------

@app.post("/recommend-price")
def recommend_price(request: PricingRequest):

    # Start with current price
    recommended_price = request.current_price

    # Default values
    market_status = "Balanced Market"
    pricing_insight = (
        "Market conditions are relatively balanced. "
        "The recommended price stays close to the current price."
    )


    # --------------------------------------------------
    # HIGH DEMAND + LIMITED INVENTORY
    # --------------------------------------------------

    if request.demand > 150 and request.inventory < 150:

        recommended_price *= 1.10

        market_status = "High Demand / Limited Inventory"

        pricing_insight = (
            "Demand is high while inventory is limited. "
            "The engine increased the price to capture stronger demand."
        )


    # --------------------------------------------------
    # LOW DEMAND + HIGH INVENTORY
    # --------------------------------------------------

    elif request.demand < 80 and request.inventory > 150:

        recommended_price *= 0.90

        market_status = "Low Demand / High Inventory"

        pricing_insight = (
            "Demand is relatively low and inventory is high. "
            "The engine reduced the price to encourage sales."
        )


    # --------------------------------------------------
    # MODERATE MARKET
    # --------------------------------------------------

    else:

        market_status = "Balanced Market"

        pricing_insight = (
            "Market conditions are relatively balanced. "
            "The recommended price stays close to the current price."
        )


    # --------------------------------------------------
    # COMPETITOR PRICE LIMIT
    # --------------------------------------------------

    lower_limit = request.competitor_price * 0.90
    upper_limit = request.competitor_price * 1.10

    # Keep recommended price within competitor range
    recommended_price = max(
        lower_limit,
        min(recommended_price, upper_limit)
    )


    # Round price
    recommended_price = round(recommended_price, 2)


    # --------------------------------------------------
    # SAVE PRICE TO REDIS
    # --------------------------------------------------

    save_price(
        request.product_id,
        recommended_price
    )


    # --------------------------------------------------
    # RESPONSE
    # --------------------------------------------------

    return {

        "product_id": request.product_id,

        "current_price": request.current_price,

        "competitor_price": request.competitor_price,

        "demand": request.demand,

        "inventory": request.inventory,

        "recommended_price": recommended_price,

        "market_status": market_status,

        "pricing_insight": pricing_insight,

        "redis_status": "Price stored successfully"
    }