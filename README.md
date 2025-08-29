# 📊 AI Portfolio Optimizer

This project is an **interactive portfolio optimization dashboard** built with **Streamlit**.  
It uses **Modern Portfolio Theory (MPT)** to compute the **optimal portfolio allocation**.

---

## 🚀 Features
- Download historical stock prices via `yfinance`
- Compute expected returns & risk using `PyPortfolioOpt`
- Optimize for **maximum Sharpe ratio**
- Display portfolio weights in table & pie chart
- Show portfolio performance metrics:
  - Expected Annual Return
  - Annual Volatility
  - Sharpe Ratio
  - Sortino Ratio
  - Max Drawdown
- Risk/Return scatter plot with simulated portfolios (Efficient Frontier)

---

## 🛠️ Installation
```bash
git clone https://github.com/Tianning-lab/ai-portfolio-optimizer.git
cd ai-portfolio-optimizer
python -m venv venv
.\venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
