import random

# Function to generate a random list of coin flips
def generate_coin_flips():
    return [random.randint(0, 1) for _ in range(100)]

# Function to check for streaks of 6 heads or tails
def has_streak(coin_flips):
    streak_count = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i-1]:
            streak_count += 1
            if streak_count == 6:  # We found a streak of 6
                return True
        else:
            streak_count = 1
    return False

# Running the experiment 10,000 times
experiments = 10000
streak_count = 0

for _ in range(experiments):
    flips = generate_coin_flips()
    if has_streak(flips):
        streak_count += 1

# Calculating the percentage of experiments with a streak of 6 heads or tails
percentage_with_streak = (streak_count / experiments) * 100
print(f"Percentage of experiments with a streak of 6 heads or tails: {percentage_with_streak}%")
