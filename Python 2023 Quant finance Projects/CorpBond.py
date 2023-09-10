import numpy as np
import matplotlib.pyplot as plt

def generate_interest_rate_paths(r0, alpha, sigma, T, dt, n_simulations):
    n_steps = int(T/dt)
    rates = np.zeros((n_steps, n_simulations))
    rates[0] = r0

    for t in range(1, n_steps):
        dW = np.random.normal(0, np.sqrt(dt), n_simulations) # small normalized random change
        dr = alpha * (r0 - rates[t-1]) * dt + sigma * dW  # change in Interest rate
        rates[t] = rates[t-1] + dr

    return rates

def monte_carlo_bond_price(r0, alpha, sigma, T, dt, n_simulations, face_value, coupon_rate):
    rates = generate_interest_rate_paths(r0, alpha, sigma, T, dt, n_simulations)
    
    n_steps = int(T/dt)
    cash_flows = np.zeros((n_steps, n_simulations))
    
    annual_steps = int(1/dt)  # steps in a year
    for i in range(0, n_steps, annual_steps):
        cash_flows[i] = coupon_rate * face_value

    cash_flows[-1] += face_value  # add face value to the last cash flow
    
    discounts = np.exp(-rates * dt)
    discounted_cash_flows = cash_flows * np.cumprod(discounts, axis=0)
    bond_prices = np.sum(discounted_cash_flows, axis=0) # formulae for calulating bond present value from future cash flows

    return np.mean(bond_prices), np.median(bond_prices), np.std(bond_prices)

# Sample parameters
r0 = 0.03  # initial interest rate
alpha = 0.1  # mean reversion coefficient
sigma = 0.02  # volatility of interest rate
T = 5  # bond maturity in years
dt = 0.01  # time step
n_simulations = 10000  # number of Monte Carlo paths
face_value = 1000  # bond face value
coupon_rate = 0.05  # annual coupon rate

mean_price, median_price, price_std = monte_carlo_bond_price(r0, alpha, sigma, T, dt, n_simulations, face_value, coupon_rate) # for visualising the plots

print(f"Mean Bond Price: {mean_price:.2f}")
print(f"Median Bond Price: {median_price:.2f}")
print(f"Bond Price Standard Deviation: {price_std:.2f}")

# Generate interest rate paths
rates = generate_interest_rate_paths(r0, alpha, sigma, T, dt, n_simulations)

# Plot the first 10 paths
for i in range(100):
    plt.plot(np.arange(0, T, dt), rates[:, i]) # calculated interest rate at each point
    
plt.title('Simulated Interest Rate Paths')
plt.xlabel('Time (Years)')
plt.ylabel('Interest Rate')
plt.grid(True)
plt.show()
