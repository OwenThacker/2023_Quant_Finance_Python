import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Set up a grid of stock prices and strike prices
stock_prices = np.linspace(50, 150, 100)  # Example stock prices from $50 to $150
strike_prices = np.linspace(50, 150, 100)  # Example strike prices from $50 to $150

# Step 2: Calculate the PnL for each combination
# Assume a call option for simplicity and that the premium (cost) for the option was $10 for all strikes
premium = 10
pnl_matrix = np.zeros((len(stock_prices), len(strike_prices)))

for i, s in enumerate(stock_prices):
    for j, k in enumerate(strike_prices):
        pnl_matrix[i, j] = max(s - k, 0) - premium

# Step 3: Visualize using a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(pnl_matrix, annot=False, cmap="YlGnBu", 
            xticklabels=20, yticklabels=20,
            cbar_kws={'label': 'PnL'})
plt.title("PnL Heatmap based on Stock and Strike Prices")
plt.xlabel("Strike Prices")
plt.ylabel("Stock Prices")
plt.xticks(ticks=np.arange(0, len(strike_prices), 20), labels=np.round(strike_prices[::20], 1))
plt.yticks(ticks=np.arange(0, len(stock_prices), 20), labels=np.round(stock_prices[::20], 1))
plt.show()
