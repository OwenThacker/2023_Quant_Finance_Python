import random

def is_on_diagonal(x, y):
    return y == -x + 10 and 0 <= x <= 10 and 0 <= y <= 10

def random_walk_for_diagonal():
    x, y = 0, 0
    steps = 0

    while not is_on_diagonal(x, y):
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        else:  # direction == 'W'
            x -= 1

        steps += 1

    return steps

def average_time_to_find_diagonal(n_simulations=10):  # Reduced to 10 for quicker testing
    total_steps = 0
    for _ in range(n_simulations):
        total_steps += random_walk_for_diagonal()

    return total_steps / n_simulations

print("Average time to find food on the diagonal:", average_time_to_find_diagonal())
