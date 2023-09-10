import random
import math

def crosses_single_boundary(D):
    # Start point
    x1, y1, z1 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)

    # Random direction
    dx, dy, dz = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)
    len_d = math.sqrt(dx**2 + dy**2 + dz**2)
    
    # Scaling to get segment of length D
    dx, dy, dz = (D * dx / len_d), (D * dy / len_d), (D * dz / len_d)

    # End point
    x2, y2, z2 = x1 + dx, y1 + dy, z1 + dz

    # Check if it crosses a boundary
    int_crossings = int(math.floor(x2) != math.floor(x1)) + int(math.floor(y2) != math.floor(y1)) + int(math.floor(z2) != math.floor(z1))
    return int_crossings == 1

def estimate_probability(D, num_trials=10000):
    count = sum(crosses_single_boundary(D) for _ in range(num_trials))
    return count / num_trials

D_values = [i * 0.01 for i in range(141)]  # Values from 0 to 1.40
probabilities = [estimate_probability(D) for D in D_values]
best_index = probabilities.index(max(probabilities))
best_D = D_values[best_index]
best_prob = probabilities[best_index]

print(f"Best D: {best_D:.10f}, Probability: {best_prob:.10f}")
