# TDA Systemic Risk Early Warning System

Applied Topological Data Analysis to 30 years of multi-index equity data (S&P 500, NASDAQ, Dow Jones, Jan 1995 – Feb 2026). Persistence landscape features show clear leading signals approximately 100 days prior to the Dotcom Bubble, 2008 Financial Crisis, and COVID-19 crash.

---

## Results

**Full 30-year L1 and L2 norm time series:**

![L1, L2 norms over 30 years, 50 day window](https://github.com/keltonmccormick18/TDA-basics/raw/main/50window.png)

![L1, L2 norms over 30 years, 100 day window](https://github.com/keltonmccormick18/TDA-basics/raw/main/100window.png)

Volatility spikes align clearly with all three major crashes. The more useful observation is what happens in the 500 days *before* each crash:

**Dotcom Bubble (2000):** Norm stability for the first ~400 days, then a clear upturn beginning ~100 days before the crash.

![L1, L2 norms for Dotcom Bubble, 100 day window](https://github.com/keltonmccormick18/TDA-basics/raw/main/100dotcom.png)

**2008 Financial Crisis:** Same pattern — extended stability followed by a sharp norm increase well before the market peak.

![L1, L2 norms for 2008, 100 day window](https://github.com/keltonmccormick18/TDA-basics/raw/main/1002008.png)

**COVID-19 (2020):** Compressed timescale but the leading upturn is still visible.

![L1, L2 norms for Covid-19 (2020), 100 day window](https://github.com/keltonmccormick18/TDA-basics/raw/main/100covid.png)

**Present day (2026, normal conditions):** Norms remain flat, consistent with no structural instability in the current market.

![L1, L2 norms for present day, 100 day window](https://github.com/keltonmccormick18/TDA-basics/raw/main/100normal.png)

Using a window size of 100 makes this leading signal especially clear, as it smooths out noise while preserving the structural upturn.

---

## How It Works

1. **Point cloud construction.** For each sliding window of trading days, plot the daily log-returns of the three indices as a point in R³. Each point represents one day; the Euclidean distance between points directly represents cross-index volatility dispersion.

2. **Vietoris-Rips complex.** Construct a simplicial complex from the point cloud by connecting points within a growing distance threshold. This produces a nested sequence of topological spaces (a filtration).

3. **Persistent homology.** Track when topological features (connected components, loops) appear ("birth") and disappear ("death") across the filtration. This is recorded in a persistence diagram.

4. **Persistence landscapes.** Convert each birth-death pair into a tent function. Take L1 and L2 norms of the resulting landscape — these summarize the total lifetime of topological features. Short-lived features (noise) contribute little; long-lived features (structural market geometry) dominate.

5. **Time series.** Slide the window across 30 years and plot the landscape norms over time.

The key insight: as market volatility builds before a crash, the point cloud geometry changes — return distributions spread out and develop higher-dimensional structure (loops) that persist longer in the filtration. The L1/L2 norms detect this structural change before it manifests as a drawdown in price.

---

## Run Locally

```bash
git clone https://github.com/keltonmccormick18/TDA-basics.git
cd TDA-basics
pip install numpy pandas yfinance gudhi matplotlib seaborn
python downloadmarketdata.py    # fetches S&P, NASDAQ, Dow from Yahoo Finance
python tdamarketvol.py          # runs TDA pipeline and generates plots
```

---

## Repository Structure

```
├── downloadmarketdata.py    # Yahoo Finance data ingestion (3 indices, 1995–present)
├── tdamarketvol.py          # Full pipeline: point clouds → distance matrices → Rips complexes
│                            #   → persistence diagrams → landscapes → L1/L2 norms → plots
└── README.md
```

---

## Dependencies

Python 3.8+, `gudhi`, `pandas`, `numpy`, `seaborn`, `matplotlib`, `yfinance`
