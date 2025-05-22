# Import libraries
from pathlib import Path 

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir / "input01.txt"

# Read input
with input_path.open("r") as file:
    pairs = [tuple(map(int, line.strip().split())) for line in file if line.strip()]

# Unzip into two separate lists
l, r = zip(*pairs)

# Sort both lists
l_sorted = sorted(l)
r_sorted = sorted(r)

# Calculate total absolute difference
solution = sum(abs(ll - rr) for ll, rr in zip(l_sorted, r_sorted))

# Print solution
print(f"Solution: {solution}")

