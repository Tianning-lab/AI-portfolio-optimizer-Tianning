import yfinance as yf
import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier, risk_models, expected_returns, objective_functions

# ------------------------------
# Data Download
# ------------------------------
def download_data(tickers, start="2020-01-01", end="2025-01-01"):
    df = yf.download(tickers, start=start, end=end)
    if "Adj Close" in df:
        prices = df["Adj Close"].dropna()
    else:
        prices = df["Close"].dropna()
        print("⚠️ Adj Close not found, using Close instead")
    return prices

# ------------------------------
# Portfolio Optimization
# ------------------------------
def optimize_portfolio(prices, rf_rate=0.02):
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)
    
    ef = EfficientFrontier(mu, S)
    ef.add_objective(objective_functions.L2_reg, gamma=0.01)  # Regularization
    weights = ef.max_sharpe(risk_free_rate=rf_rate)
    cleaned_weights = ef.clean_weights()
    
    perf = ef.portfolio_performance(verbose=False, risk_free_rate=rf_rate)
    return cleaned_weights, perf, mu, S

# ------------------------------
# Additional Portfolio Metrics
# ------------------------------
def portfolio_metrics(weights, mu, S, rf_rate=0.02):
    w = np.array(list(weights.values()))
    exp_return = np.dot(w, mu)
    volatility = np.sqrt(np.dot(w.T, np.dot(S, w)))
    sharpe = (exp_return - rf_rate) / volatility
    
    # Sortino Ratio
    downside_returns = mu[mu < rf_rate]
    downside_std = np.sqrt(np.dot(w.T, np.dot(S, w))) if len(downside_returns) > 0 else np.nan
    sortino = (exp_return - rf_rate) / downside_std if downside_std and downside_std > 0 else np.nan

    # Max Drawdown (approx via cumulative returns)
    returns = (prices.pct_change().dropna() @ w)
    cum_returns = (1 + returns).cumprod()
    rolling_max = cum_returns.cummax()
    drawdown = (cum_returns - rolling_max) / rolling_max
    max_dd = drawdown.min()
    
    return {
        "Expected Return": exp_return,
        "Volatility": volatility,
        "Sharpe Ratio": sharpe,
        "Sortino Ratio": sortino,
        "Max Drawdown": max_dd
    }
