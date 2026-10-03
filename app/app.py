import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PriceFlow",
    page_icon="ðŸ’¸",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PRICEFLOW CSS
# ============================================================

st.markdown(
    """
<style>

html, body {
    background-color: #f6f0e6 !important;
}

.stApp {
    background-color: #f6f0e6 !important;
    color: #171717 !important;
}

.block-container {
    max-width: 1100px;
    padding-top: 35px;
    padding-bottom: 50px;
}

/* Hide Streamlit defaults */

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ==========================================================
   HERO
   ========================================================== */

.hero {
    background: #171717;
    border-radius: 18px;
    padding: 38px 42px;
    margin-bottom: 24px;
}

.hero-small {
    color: #f28c28;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.hero-title {
    color: #ffffff;
    font-size: 38px;
    font-weight: 850;
    line-height: 1.08;
    margin: 0;
}

.hero-description {
    color: #c9c3ba;
    font-size: 13px;
    line-height: 1.6;
    max-width: 720px;
    margin-top: 15px;
    margin-bottom: 0;
}


/* ==========================================================
   SECTION HEADINGS
   ========================================================== */

.section-heading {
    color: #171717;
    font-size: 16px;
    font-weight: 800;
    margin-top: 18px;
    margin-bottom: 4px;
}

.section-description {
    color: #817a72;
    font-size: 11px;
    margin-bottom: 13px;
}


/* ==========================================================
   CURRENT MARKET
   ========================================================== */

.market-container {
    background: #ffffff;
    border: 1px solid #e5ddd2;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 25px;
}

.market-heading {
    color: #171717;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 15px;
}

.market-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
}

.market-item {
    padding: 5px 20px;
    border-right: 1px solid #eee7dc;
}

.market-item:first-child {
    padding-left: 0;
}

.market-item:last-child {
    border-right: none;
}

.market-label {
    color: #89827a;
    font-size: 10px;
    margin-bottom: 6px;
}

.market-value {
    color: #171717;
    font-size: 21px;
    font-weight: 800;
}


/* ==========================================================
   PRICING INPUT HEADER
   ========================================================== */

.input-header {
    background: #ffffff;
    border: 1px solid #e5ddd2;
    border-radius: 16px;
    padding: 18px 20px;
    margin-bottom: 13px;
}

.input-title {
    color: #171717;
    font-size: 15px;
    font-weight: 800;
}

.input-description {
    color: #817a72;
    font-size: 10px;
    margin-top: 4px;
}


/* ==========================================================
   STREAMLIT INPUTS
   ========================================================== */

div[data-testid="stTextInput"] label,
div[data-testid="stNumberInput"] label {
    color: #716a62 !important;
    font-size: 10px !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] {
    background-color: #202027 !important;
    border: 1px solid #202027 !important;
    border-radius: 7px !important;
}

div[data-baseweb="input"] input {
    color: #ffffff !important;
    background-color: #202027 !important;
    font-size: 12px !important;
}

div[data-baseweb="input"] input::placeholder {
    color: #aaa5a0 !important;
}


/* ==========================================================
   NUMBER INPUT BUTTONS
   ========================================================== */

button[data-testid="stNumberInputStepDown"],
button[data-testid="stNumberInputStepUp"] {
    color: #ffffff !important;
}


/* ==========================================================
   CALCULATE BUTTON
   ========================================================== */

.stButton {
    margin-top: 8px;
}

.stButton > button {
    background-color: #f28c28 !important;
    color: #171717 !important;
    border: none !important;
    border-radius: 7px !important;
    font-size: 11px !important;
    font-weight: 800 !important;
    height: 40px !important;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background-color: #e77e1d !important;
    color: #171717 !important;
}

.stButton > button:focus {
    box-shadow: none !important;
}


/* ==========================================================
   RECOMMENDATION
   ========================================================== */

.recommendation-card {
    background: #171717;
    border-radius: 18px;
    padding: 28px 30px;
    margin-top: 23px;
}

.recommendation-label {
    color: #f28c28;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.6px;
}

.recommendation-price {
    color: #ffffff;
    font-size: 46px;
    font-weight: 900;
    line-height: 1;
    margin-top: 9px;
}

.recommendation-current {
    color: #aaa49c;
    font-size: 11px;
    margin-top: 10px;
}


/* ==========================================================
   SNAPSHOT
   ========================================================== */

.snapshot-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 10px;
}

.snapshot-card {
    background: #ffffff;
    border: 1px solid #e5ddd2;
    border-radius: 12px;
    padding: 16px;
}

.snapshot-label {
    color: #817a72;
    font-size: 9px;
    margin-bottom: 7px;
}

.snapshot-value {
    color: #171717;
    font-size: 17px;
    font-weight: 800;
}


/* ==========================================================
   INSIGHT
   ========================================================== */

.insight-card {
    background: #fff7ed;
    border-left: 4px solid #f28c28;
    border-radius: 10px;
    padding: 17px 18px;
    margin-top: 15px;
}

.insight-title {
    color: #171717;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 7px;
}

.insight-status {
    color: #171717;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 7px;
}

.insight-text {
    color: #514b44;
    font-size: 11px;
    line-height: 1.6;
}


/* ==========================================================
   REDIS STATUS
   ========================================================== */

.redis-card {
    background: #ffffff;
    border: 1px solid #e5ddd2;
    border-radius: 10px;
    padding: 13px 17px;
    margin-top: 13px;
}

.redis-success {
    color: #376b45;
    font-size: 10px;
    font-weight: 700;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.priceflow-footer {
    color: #918a82;
    font-size: 9px;
    text-align: center;
    margin-top: 30px;
    padding-top: 18px;
    border-top: 1px solid #ded6ca;
}


/* ==========================================================
   RESPONSIVE
   ========================================================== */

@media (max-width: 800px) {

    .market-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
    }

    .market-item {
        border-right: none;
        padding: 8px;
    }

    .snapshot-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .hero-title {
        font-size: 30px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# DEFAULT VALUES
# ============================================================

DEFAULT_PRODUCT = "P0002"
DEFAULT_DEMAND = 229.0
DEFAULT_INVENTORY = 117.0
DEFAULT_CURRENT_PRICE = 80.16
DEFAULT_COMPETITOR_PRICE = 85.00




# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">
        <div class="hero-small">
            PRICEFLOW
        </div>

        <div class="hero-title">
            Find the right price<br>
            at the right moment.
        </div>

        <div class="hero-description">
            PriceFlow combines demand, inventory and competitor
            pricing to generate a market-aware price recommendation.
        </div>
    </div>

    """
)



# ============================================================
# MARKET CONDITIONS
# ============================================================

st.html(
    """
    <div class="section-heading">
        Market conditions
    </div>

    <div class="section-description">
        Current market conditions used to calculate a recommendation.
    </div>

    <div class="market-container">

        <div class="market-heading">
            CURRENT MARKET
        </div>

        <div class="market-grid">

            <div class="market-item">
                <div class="market-label">
                    Current price
                </div>

                <div class="market-value">
                    &#8377;80.16
                </div>
            </div>

            <div class="market-item">
                <div class="market-label">
                    Competitor
                </div>

                <div class="market-value">
                    &#8377;85.00
                </div>
            </div>

            <div class="market-item">
                <div class="market-label">
                    Demand
                </div>

                <div class="market-value">
                    229
                </div>
            </div>

            <div class="market-item">
                <div class="market-label">
                    Inventory
                </div>

                <div class="market-value">
                    117
                </div>
            </div>

        </div>

    </div>
    """
)


# ============================================================
# PRICING INPUT HEADER
# ============================================================

st.html(
    """
    <div class="input-header">

        <div class="input-title">
            Pricing inputs
        </div>

        <div class="input-description">
            Enter the current market conditions.
        </div>

    </div>
    """
)


# ============================================================
# INPUTS
# ============================================================

left_column, right_column = st.columns(2)

with left_column:

    product_id = st.text_input(
        "Product ID",
        value=DEFAULT_PRODUCT
    )

    demand = st.number_input(
        "Demand",
        min_value=0.0,
        value=DEFAULT_DEMAND,
        step=1.0
    )

    inventory = st.number_input(
        "Inventory",
        min_value=0.0,
        value=DEFAULT_INVENTORY,
        step=1.0
    )


with right_column:

    current_price = st.number_input(
        "Current Price (&#8377;)",
        min_value=0.0,
        value=DEFAULT_CURRENT_PRICE,
        step=0.01
    )

    competitor_price = st.number_input(
        "Competitor Price (&#8377;)",
        min_value=0.0,
        value=DEFAULT_COMPETITOR_PRICE,
        step=0.01
    )


# ============================================================
# CALCULATE BUTTON
# ============================================================

calculate = st.button(
    "CALCULATE PRICE",
    use_container_width=True
)


# ============================================================
# PRICE CALCULATION
# ============================================================

if calculate:

    # ========================================================
    # MARKET-AWARE PRICING LOGIC
    # ========================================================

    recommended_price = current_price

    market_status = "Balanced Market"

    pricing_insight = (
        "Market conditions are relatively balanced. "
        "The recommended price stays close to the current price."
    )

    # High demand + limited inventory
    if demand > 150 and inventory < 150:

        recommended_price = current_price * 1.10

        market_status = "High Demand / Limited Inventory"

        pricing_insight = (
            "Demand is high while inventory is limited. "
            "The engine increased the price to capture stronger demand."
        )

    # Low demand + high inventory
    elif demand < 80 and inventory > 150:

        recommended_price = current_price * 0.90

        market_status = "Low Demand / High Inventory"

        pricing_insight = (
            "Demand is relatively low and inventory is high. "
            "The engine reduced the price to encourage sales."
        )

    # ========================================================
    # COMPETITOR PRICE LIMIT
    # ========================================================

    lower_limit = competitor_price * 0.90
    upper_limit = competitor_price * 1.10

    recommended_price = max(
        lower_limit,
        min(recommended_price, upper_limit)
    )

    recommended_price = round(
        recommended_price,
        2
    )


    # ========================================================
    # RECOMMENDED PRICE
    # ========================================================

    st.html(
        """
        <div class="section-heading">
            Pricing recommendation
        </div>
        """,
    )

    st.html(
        f"""
        <div class="recommendation-card">

            <div class="recommendation-label">
                RECOMMENDED SELLING PRICE
            </div>

            <div class="recommendation-price">
                &#8377;{recommended_price:.2f}
            </div>

            <div class="recommendation-current">
                Current price: &#8377;{current_price:.2f}
            </div>

        </div>
        """,
    )


    # ========================================================
    # MARKET SNAPSHOT
    # ========================================================

    st.html(
        """
        <div class="section-heading">
            Market snapshot
        </div>
        """,
    )

    st.html(
        f"""
        <div class="snapshot-grid">

            <div class="snapshot-card">

                <div class="snapshot-label">
                    Current price
                </div>

                <div class="snapshot-value">
                    &#8377;{current_price:.2f}
                </div>

            </div>


            <div class="snapshot-card">

                <div class="snapshot-label">
                    Competitor
                </div>

                <div class="snapshot-value">
                    &#8377;{competitor_price:.2f}
                </div>

            </div>


            <div class="snapshot-card">

                <div class="snapshot-label">
                    Demand
                </div>

                <div class="snapshot-value">
                    {int(demand)}
                </div>

            </div>


            <div class="snapshot-card">

                <div class="snapshot-label">
                    Inventory
                </div>

                <div class="snapshot-value">
                    {int(inventory)}
                </div>

            </div>

        </div>
        """,
    )


    # ========================================================
    # PRICING INSIGHT
    # ========================================================

    st.html(
        f"""
        <div class="insight-card">

            <div class="insight-title">
                Pricing insight
            </div>

            <div class="insight-status">
                {market_status}
            </div>

            <div class="insight-text">
                {pricing_insight}
            </div>

        </div>
        """,
    )


    # ========================================================
    # CLOUD STATUS
    # ========================================================

    st.html(
        """
        <div class="redis-card">

            <span class="redis-success">
                &#10003; Price recommendation generated successfully
            </span>

        </div>
        """,
    )


# ============================================================# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="priceflow-footer">
        PriceFlow &#8226; Dynamic Pricing Engine &#8226; Cloud Demo
    </div>
    """
)

