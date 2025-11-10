
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Smart Trade Calculator",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== PREMIUM BASE.ORG-INSPIRED CSS ====================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* ===== GLOBAL STYLES ===== */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-attachment: fixed;
    }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ===== HERO SECTION ===== */
    .hero-section {
        text-align: center;
        padding: 60px 20px 40px;
        margin-bottom: 40px;
        background: linear-gradient(135deg, rgba(88, 80, 236, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #5850EC, #764ba2, transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 1; }
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 0%, #a8c0ff 50%, #c471f5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px;
        letter-spacing: -2px;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.15rem;
        color: rgba(255, 255, 255, 0.6);
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* ===== GLASS CARD CONTAINERS ===== */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 32px;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card:hover {
        border-color: rgba(88, 80, 236, 0.4);
        box-shadow: 0 12px 48px rgba(88, 80, 236, 0.2);
        transform: translateY(-4px);
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(88, 80, 236, 0.5), transparent);
    }
    
    /* ===== SECTION HEADERS ===== */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .section-header::before {
        content: '';
        width: 4px;
        height: 24px;
        background: linear-gradient(180deg, #5850EC, #764ba2);
        border-radius: 4px;
        box-shadow: 0 0 12px rgba(88, 80, 236, 0.6);
    }
    
    /* ===== NEON GLOW DIVIDER ===== */
    .neon-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #5850EC, #764ba2, transparent);
        margin: 40px 0;
        box-shadow: 0 0 20px rgba(88, 80, 236, 0.5);
        border-radius: 2px;
    }
    
    /* ===== STREAMLIT INPUT CUSTOMIZATION ===== */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > div:focus {
        border-color: #5850EC !important;
        box-shadow: 0 0 0 3px rgba(88, 80, 236, 0.2) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    /* Input labels */
    .stTextInput > label,
    .stNumberInput > label,
    .stSelectbox > label,
    .stRadio > label,
    .stSlider > label {
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 8px !important;
    }
    
    /* ===== RADIO BUTTONS ===== */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.03);
        padding: 12px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .stRadio > div > label > div {
        color: rgba(255, 255, 255, 0.7) !important;
        transition: all 0.3s ease;
    }
    
    .stRadio > div > label:hover > div {
        color: #ffffff !important;
    }
    
    /* ===== SLIDER ===== */
    .stSlider > div > div > div {
        background: rgba(88, 80, 236, 0.3) !important;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #5850EC, #764ba2) !important;
    }
    
    /* ===== BUTTONS ===== */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #5850EC 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 16px 32px;
        border: none;
        border-radius: 12px;
        box-shadow: 0 4px 24px rgba(88, 80, 236, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        letter-spacing: 0.5px;
        text-transform: uppercase;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 32px rgba(88, 80, 236, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0) scale(0.98);
    }
    
    /* ===== METRICS ===== */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #ffffff, #a8c0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.6) !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
    }
    
    /* Metric container glow */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        border-color: rgba(88, 80, 236, 0.5);
        box-shadow: 0 0 24px rgba(88, 80, 236, 0.3);
        transform: translateY(-2px);
    }
    
    /* ===== INFO/SUCCESS/WARNING/ERROR BOXES ===== */
    .stAlert {
        background: rgba(255, 255, 255, 0.04) !important;
        border-radius: 12px !important;
        border-left: 3px solid !important;
        backdrop-filter: blur(10px) !important;
        padding: 16px !important;
    }
    
    .stSuccess {
        border-left-color: #10b981 !important;
        background: rgba(16, 185, 129, 0.1) !important;
    }
    
    .stInfo {
        border-left-color: #3b82f6 !important;
        background: rgba(59, 130, 246, 0.1) !important;
    }
    
    .stWarning {
        border-left-color: #f59e0b !important;
        background: rgba(245, 158, 11, 0.1) !important;
    }
    
    .stError {
        border-left-color: #ef4444 !important;
        background: rgba(239, 68, 68, 0.1) !important;
    }
    
    /* ===== RESULT CARDS WITH GLOW ===== */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        margin: 12px 0;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .result-card:hover {
        background: rgba(255, 255, 255, 0.05);
        box-shadow: 0 0 32px rgba(88, 80, 236, 0.2);
    }
    
    .result-card-title {
        font-size: 0.85rem;
        color: rgba(255, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    .result-card-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    /* ===== MARKDOWN HEADINGS ===== */
    .markdown-text-container h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.4rem !important;
        margin-top: 32px !important;
        margin-bottom: 16px !important;
    }
    
    .markdown-text-container h4 {
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        margin-bottom: 12px !important;
    }
    
    /* ===== PLOTLY CHARTS ===== */
    .js-plotly-plot {
        border-radius: 16px;
        overflow: hidden;
    }
    
    /* ===== CUSTOM FOOTER ===== */
    .custom-footer {
        text-align: center;
        padding: 32px 20px;
        margin-top: 60px;
        background: rgba(255, 255, 255, 0.02);
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.95rem;
    }
    
    .custom-footer strong {
        color: rgba(255, 255, 255, 0.9);
        font-weight: 600;
    }
    
    .custom-footer a {
        color: #5850EC;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .custom-footer a:hover {
        color: #764ba2;
        text-shadow: 0 0 8px rgba(88, 80, 236, 0.6);
    }
    
    /* ===== LOADING ANIMATION ===== */
    @keyframes pulse-glow {
        0%, 100% {
            box-shadow: 0 0 20px rgba(88, 80, 236, 0.4);
        }
        50% {
            box-shadow: 0 0 40px rgba(88, 80, 236, 0.8);
        }
    }
    
    .glow-pulse {
        animation: pulse-glow 2s infinite;
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.02);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(88, 80, 236, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(88, 80, 236, 0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ==================== INSTRUMENT DATABASE ====================
INSTRUMENTS = {
    "XAU/USD (Gold)": {
        "type": "GOLD",
        "pip_size": 0.01,
        "pip_value": 1.0,
        "symbol": "🥇"
    },
    "BTC/USD (Bitcoin)": {
        "type": "CRYPTO",
        "pip_size": 1.0,
        "pip_value": 1.0,
        "symbol": "₿"
    },
    "ETH/USD (Ethereum)": {
        "type": "CRYPTO",
        "pip_size": 0.01,
        "pip_value": 0.01,
        "symbol": "⟠"
    },
    "EUR/USD": {
        "type": "FOREX",
        "pip_size": 0.0001,
        "pip_value": 10.0,
        "symbol": "💱"
    },
    "GBP/USD": {
        "type": "FOREX",
        "pip_size": 0.0001,
        "pip_value": 10.0,
        "symbol": "💱"
    },
    "USD/JPY": {
        "type": "FOREX",
        "pip_size": 0.01,
        "pip_value": 10.0,
        "symbol": "💱"
    },
    "AUD/USD": {
        "type": "FOREX",
        "pip_size": 0.0001,
        "pip_value": 10.0,
        "symbol": "💱"
    },
    "EUR/GBP": {
        "type": "FOREX",
        "pip_size": 0.0001,
        "pip_value": 10.0,
        "symbol": "💱"
    }
}

# ==================== CALCULATION FUNCTIONS ====================

def calculate_trade_metrics(instrument_data, direction, entry, sl, tp, balance, risk_amount):
    price_risk = abs(entry - sl)
    price_reward = abs(tp - entry)
    pips_risk = price_risk / instrument_data['pip_size']
    pips_reward = price_reward / instrument_data['pip_size']
    lot_size = risk_amount / (pips_risk * instrument_data['pip_value'])
    potential_profit = pips_reward * instrument_data['pip_value'] * lot_size
    rr_ratio = price_reward / price_risk if price_risk > 0 else 0
    risk_percentage = (risk_amount / balance) * 100
    
    return {
        'price_risk': price_risk,
        'price_reward': price_reward,
        'pips_risk': pips_risk,
        'pips_reward': pips_reward,
        'lot_size': lot_size,
        'potential_profit': potential_profit,
        'rr_ratio': rr_ratio,
        'risk_percentage': risk_percentage
    }

def validate_trade_setup(direction, entry, sl, tp):
    warnings = []
    if direction == "BUY 📈":
        if sl >= entry:
            warnings.append("⚠️ For BUY: Stop Loss should be BELOW Entry!")
        if tp <= entry:
            warnings.append("⚠️ For BUY: Take Profit should be ABOVE Entry!")
    else:
        if sl <= entry:
            warnings.append("⚠️ For SELL: Stop Loss should be ABOVE Entry!")
        if tp >= entry:
            warnings.append("⚠️ For SELL: Take Profit should be BELOW Entry!")
    return warnings

def create_price_chart(instrument_name, direction, entry, sl, tp):
    fig = go.Figure()
    
    entry_color = '#3b82f6'
    sl_color = '#ef4444'
    tp_color = '#10b981'
    
    prices = [sl, entry, tp]
    labels = ['Stop Loss', 'Entry', 'Take Profit']
    colors = [sl_color, entry_color, tp_color]
    
    for price, label, color in zip(prices, labels, colors):
        fig.add_trace(go.Scatter(
            x=[0, 1],
            y=[price, price],
            mode='lines+markers+text',
            name=label,
            line=dict(color=color, width=4, dash='solid'),
            marker=dict(size=16, symbol='diamond', line=dict(width=2, color='rgba(255,255,255,0.3)')),
            text=["", f"<b>{label}</b><br>${price:.5f}"],
            textposition="top center",
            textfont=dict(size=13, color=color, family="Inter", weight='bold'),
            hovertemplate=f"<b>{label}</b><br>Price: ${price:.5f}<extra></extra>"
       ))
    
    fig.add_shape(
        type="rect",
        x0=0, x1=1,
        y0=min(entry, sl), y1=max(entry, sl),
        fillcolor="rgba(239, 68, 68, 0.15)",
        line_width=0,
        layer="below"
    )
    
    fig.add_shape(
        type="rect",
        x0=0, x1=1,
        y0=min(entry, tp), y1=max(entry, tp),
        fillcolor="rgba(16, 185, 129, 0.15)",
        line_width=0,
        layer="below"
    )
    
    fig.update_layout(
        title=None,
        xaxis=dict(


            showticklabels=False,
            showgrid=False,
            zeroline=False,
            range=[-0.1, 1.1]
        ),
        yaxis=dict(
            title="Price Level",
            showgrid=True,
            gridcolor='rgba(255,255,255,0.05)',
            color='rgba(255,255,255,0.7)',
            title_font=dict(family="Inter", size=12)
        ),
        plot_bgcolor='rgba(0,0,0,0.2)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(color='rgba(255,255,255,0.8)', size=11, family="Inter")
        ),
        height=400,
        margin=dict(l=60, r=60, t=80, b=50)
    )
    
    return fig

def create_risk_reward_chart(risk_amount, potential_profit):
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=['Risk', 'Reward'],
        y=[risk_amount, potential_profit],
        marker=dict(
            color=['#ef4444', '#10b981'],
            line=dict(color='rgba(255,255,255,0.2)', width=2)
        ),
        text=[f"${risk_amount:.2f}", f"${potential_profit:.2f}"],
        textposition='outside',
        textfont=dict(size=15, color='white', family="Inter", weight=700),
        hovertemplate="<b>%{x}</b><br>Amount: $%{y:.2f}<extra></extra>",
        width=[0.5, 0.5]
    ))
    
    fig.update_layout(
        title=None,
        plot_bgcolor='rgba(0,0,0,0.2)',

        xaxis=dict(
            showgrid=False,
            color='rgba(255,255,255,0.7)',
            tickfont=dict(size=12, family="Inter")
        ),
        yaxis=dict(
            title="Amount (USD)",
            showgrid=True,
            gridcolor='rgba(255,255,255,0.05)',
            color='rgba(255,255,255,0.7)',
            title_font=dict(family="Inter", size=12)
        ),
        height=380,
        margin=dict(l=60, r=60, t=70, b=50)
    )
    
    return fig

# ==================== MAIN APP ====================

def main():
    # Hero Section
    st.markdown("""
        <div class="hero-section">
            <div style="font-size: 3rem; margin-bottom: 12px;"></div>
            <div class="hero-title">Smart Trade Calculator</div>
            <div class="hero-subtitle">Precision-powered trading insights for modern traders</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Layout
    col1, col2 = st.columns([1, 1.4], gap="large")
    
    with col1:
        st.markdown('<div class="glass-card"><div class="section-header"> Trade Setup</div>', unsafe_allow_html=True)
        
        direction = st.radio(
            "Trade Direction",
            ["BUY 📈", "SELL 📉"],
            horizontal=True,
            label_visibility="visible"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        instrument_name = st.selectbox(
            "Trading Instrument",
            list(INSTRUMENTS.keys()),
            index=0
        )
        
        instrument_data = INSTRUMENTS[instrument_name]
        st.info(f"{instrument_data['symbol']} **{instrument_data['type']}** | Pip: {instrument_data['pip_size']}")
        
        st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">💰 Price Levels</div>', unsafe_allow_html=True)
        
        entry_price = st.number_input(
            "Entry Price",
            min_value=0.0,
            value=2000.0 if "Gold" in instrument_name else 1.1000,
            step=0.01,
            format="%.5f"
        )
        
        stop_loss = st.number_input(
            "Stop Loss",
            min_value=0.0,
            value=1998.0 if "Gold" in instrument_name else 1.0980,
            step=0.01,
            format="%.5f"
        )
        
        take_profit = st.number_input(
            "Take Profit",
            min_value=0.0,
            value=2004.0 if "Gold" in instrument_name else 1.1040,
            step=0.01,
            format="%.5f"
        )
        
        st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">💼 Risk Management</div>', unsafe_allow_html=True)
        
        account_balance = st.number_input(
            "Account Balance ($)",
            min_value=0.0,
            value=5000.0,
            step=100.0
        )
        
        risk_type = st.radio(
            "Risk Method",
            ["Percentage (%)", "Fixed Amount ($)"],
            horizontal=True
        )
        
        if risk_type == "Percentage (%)":
            risk_percentage = st.slider(
                "Risk Percentage",
                min_value=0.1,
                max_value=10.0,
                value=1.0,
                step=0.1
            )
            risk_amount = (risk_percentage / 100) * account_balance
            st.success(f"💵 Risk Amount: **${risk_amount:.2f}**")
        else:
            risk_amount = st.number_input(
                "Risk Amount ($)",
                min_value=0.0,
                value=50.0,
                step=5.0
            )
            risk_percentage = (risk_amount / account_balance) * 100
            st.success(f" Risk: **{risk_percentage:.2f}%** of account")
        
        if risk_percentage > 5:
            st.error(f"⚠️ High Risk: {risk_percentage:.1f}%! Consider 1-2% per trade.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        calculate_button = st.button(" CALCULATE TRADE")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        if calculate_button:
            warnings = validate_trade_setup(direction, entry_price, stop_loss, take_profit)
            
            if warnings:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown('<div class="section-header">⚠️ Setup Issues</div>', unsafe_allow_html=True)
                for warning in warnings:
                    st.warning(warning)
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)

            # Calculate metrics
            metrics = calculate_trade_metrics(
                instrument_data,
                direction,
                entry_price,
                stop_loss,
                take_profit,
                account_balance,
                risk_amount
            )
            
            # Display Results
            # st.markdown("###  Trade Analysis Results")

            # Detailed Metrics Section
            st.markdown('<div class="glass-card"><div class="section-header"> Trade Analysis Results</div>', unsafe_allow_html=True)
            
            d1, d2 = st.columns(2)
            
            with d1:
                st.markdown('<div class="section-header">📉 Risk Metrics</div>', unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">Pips at Risk</div>
                        <div class="result-card-value" style="color: #ef4444;">{metrics['pips_risk']:.1f} pips</div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">Risk Amount</div>
                        <div class="result-card-value" style="color: #ef4444;">${risk_amount:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">Risk Percentage</div>
                        <div class="result-card-value" style="color: #ef4444;">{metrics['risk_percentage']:.2f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with d2:
                st.markdown('<div class="section-header">📈 Reward Metrics</div>', unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">Pips to Gain</div>
                        <div class="result-card-value" style="color: #10b981;">{metrics['pips_reward']:.1f} pips</div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">Potential Profit</div>
                        <div class="result-card-value" style="color: #10b981;">${metrics['potential_profit']:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-card-title">Profit Percentage</div>
                        <div class="result-card-value" style="color: #10b981;">{(metrics['potential_profit']/account_balance)*100:.2f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Trade Assessment
            st.markdown('<div class="glass-card"><div class="section-header">💭 Trade Assessment</div>', unsafe_allow_html=True)
            
            if metrics['rr_ratio'] >= 3:
                st.success("✅ **EXCELLENT** - Outstanding risk-reward ratio! This is a premium setup.")
            elif metrics['rr_ratio'] >= 2:
                st.success("✅ **GREAT** - Solid trade setup with good potential.")
            elif metrics['rr_ratio'] >= 1.5:
                st.info("ℹ️ **GOOD** - Acceptable setup, room for improvement.")
            elif metrics['rr_ratio'] >= 1:
                st.warning("⚠️ **MODERATE** - Consider improving your risk-reward ratio.")
            else:
                st.error("❌ **POOR** - Risk exceeds reward. Reconsider this trade!")
            
            if metrics['lot_size'] > 10:
                st.error(f"⚠️ WARNING: {metrics['lot_size']:.2f} lots is extremely large! Verify your inputs.")
            elif metrics['lot_size'] < 0.01:
                st.warning(f"⚠️ NOTE: {metrics['lot_size']:.4f} lots is very small. Most brokers require 0.01 minimum.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        else:
            st.markdown("""
                <div class="glass-card" style="text-align: center; padding: 80px 40px;">
                    <div style="font-size: 4rem; margin-bottom: 20px;">📊</div>
                    <div style="font-size: 1.3rem; color: rgba(255,255,255,0.6); margin-bottom: 12px;">
                        Configure your trade parameters
                    </div>
                    <div style="font-size: 1rem; color: rgba(255,255,255,0.4);">
                        Enter your trade details on the left and click <strong>CALCULATE</strong> to see comprehensive analysis
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # Charts Section (Full Width)
    if calculate_button and not warnings:
        st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
        
        chart_col1, chart_col2 = st.columns(2, gap="large")
        
        with chart_col1:
            st.markdown('<div class="glass-card"><div class="section-header"> Price Setup</div>', unsafe_allow_html=True)
            price_chart = create_price_chart(
                instrument_name,
                direction,
                entry_price,
                stop_loss,
                take_profit
            )
            st.plotly_chart(price_chart, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with chart_col2:
            st.markdown('<div class="glass-card"><div class="section-header"> Risk vs Reward</div>', unsafe_allow_html=True)
            rr_chart = create_risk_reward_chart(risk_amount, metrics['potential_profit'])
            st.plotly_chart(rr_chart, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="custom-footer">
            🚀 Created by <strong>Ankit Khaliya</strong> & <strong>Princy Khatri</strong> |  
            <strong>NIT Calicut</strong> | 
            Materials Science & Engineering<br>
            <span style="font-size: 0.85rem; color: rgba(255,255,255,0.3);">
                {datetime.now().strftime("%B %Y")} • Built with Streamlit & Plotly
            </span>
        </div>
    """, unsafe_allow_html=True)

# ==================== RUN THE APP ====================
if __name__ == "__main__":
    main()