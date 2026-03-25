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

---

## See Also

This project evolved into the production [Portfolio Analyser](https://nwc-advisory.com/app/analyser/) at **[New Way Capital Advisory](https://nwc-advisory.com)**.

### Related Tools

- [Portfolio X-Ray](https://nwc-advisory.com/xray) — Free fund look-through analysis
- [Portfolio Consolidation](https://nwc-advisory.com/portfolio/consolidation) — Multi-custodian portfolio merge
- [MomentumFlow AI](https://nwc-advisory.com/app/) — AI stock scanner
- [Property Comps](https://property.nwc-advisory.com) — Comparable sales across 11 global markets

