import numpy as np

def crosses_single_boundary(D, num_samples=10000):
    # Start points
    start_points = np.random.rand(num_samples, 3)

    # Random directions
    directions = np.random.randn(num_samples, 3)
    normalized_directions = directions / np.linalg.norm(directions, axis=1)[:, np.newaxis]

    # Endpoints
    end_points = start_points + D * normalized_directions

    # Check if it crosses a boundary
    int_crossings = np.sum(np.floor(end_points) != np.floor(start_points), axis=1)
    return np.sum(int_crossings == 1)

def estimate_probability(D, num_trials=10000):
    count = crosses_single_boundary(D, num_samples=num_trials)
    return count / num_trials

D_values = np.arange(0, 1.41, 0.01)  # Values from 0 to 1.40
probabilities = np.array([estimate_probability(D) for D in D_values])
best_index = np.argmax(probabilities)
best_D = D_values[best_index]
best_prob = probabilities[best_index]

print(f"Best D: {best_D:.10f}, Probability: {best_prob:.10f}")
