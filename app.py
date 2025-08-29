import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd
from optimizer import download_data, optimize_portfolio, portfolio_metrics

st.set_page_config(page_title="AI Portfolio Optimizer", layout="wide")

st.title("📊 AI Portfolio Optimizer")
st.markdown("An interactive tool for portfolio optimization using **Modern Portfolio Theory (MPT)** and risk/return analytics.")

# ------------------------------
# Sidebar Inputs
# ------------------------------
st.sidebar.header("Portfolio Settings")
tickers = st.sidebar.text_input("Enter stock tickers (comma separated)", "AAPL,MSFT,GOOG,AMZN")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-01-01"))
rf_rate = st.sidebar.number_input("Risk-Free Rate", value=0.02, step=0.01)

if st.sidebar.button("Optimize Portfolio"):
    tickers = [t.strip().upper() for t in tickers.split(",")]
    
    # Download & Optimize
    prices = download_data(tickers, start=start_date, end=end_date)
    weights, perf, mu, S = optimize_portfolio(prices, rf_rate=rf_rate)
    metrics = portfolio_metrics(weights, mu, S, rf_rate=rf_rate)

    # ------------------------------
    # Display Results
    # ------------------------------
    st.subheader("Optimized Portfolio Weights")
    st.write(pd.Series(weights).sort_values(ascending=False).apply(lambda x: f"{x:.2%}"))

    st.subheader("Portfolio Performance")
    st.json({
        "Expected Annual Return": f"{metrics['Expected Return']:.2%}",
        "Annual Volatility": f"{metrics['Volatility']:.2%}",
        "Sharpe Ratio": f"{metrics['Sharpe Ratio']:.2f}",
        "Sortino Ratio": f"{metrics['Sortino Ratio']:.2f}" if metrics['Sortino Ratio'] else "N/A",
        "Max Drawdown": f"{metrics['Max Drawdown']:.2%}"
    })

    # ------------------------------
    # Pie Chart of Weights
    # ------------------------------
    fig1, ax1 = plt.subplots()
    ax1.pie(weights.values(), labels=weights.keys(), autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    # ------------------------------
    # Efficient Frontier Scatter Plot
    # ------------------------------
    st.subheader("Efficient Frontier Simulation")
    n_portfolios = 3000
    all_returns = []
    all_vols = []
    all_sharpes = []

    for _ in range(n_portfolios):
        rand_weights = np.random.random(len(mu))
        rand_weights /= np.sum(rand_weights)
        exp_ret = np.dot(rand_weights, mu)
        vol = np.sqrt(np.dot(rand_weights.T, np.dot(S, rand_weights)))
        sharpe = (exp_ret - rf_rate) / vol
        all_returns.append(exp_ret)
        all_vols.append(vol)
        all_sharpes.append(sharpe)

    df_plot = pd.DataFrame({
        "Return": all_returns,
        "Volatility": all_vols,
        "Sharpe": all_sharpes
    })

    fig2 = px.scatter(
        df_plot, x="Volatility", y="Return",
        color="Sharpe", color_continuous_scale="Viridis",
        title="Simulated Portfolios - Risk/Return Tradeoff"
    )
    st.plotly_chart(fig2, use_container_width=True)
