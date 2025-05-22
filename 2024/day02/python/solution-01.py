# Import libraries
from pathlib import Path 

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

with input_path.open("r", encoding="utf-8") as f:
    input = f.read().splitlines()

# sample = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

# input = sample.splitlines()

# Set counter
c = 0

# Interate through lines of input
for line in input:
    lines = list(map(int, line.split()))

    # Check if elements in list a monotonically increasing or decreasing
    is_monotonic = (
        all(lines[i] < lines[i+1] for i in range(len(lines) - 1)) or
        all(lines[i] > lines[i+1] for i in range(len(lines) - 1))
    )

    # Check if elements difference is at least 1 or max 3
    steps_valid = all(
        1 <= abs(lines[i] - lines[i+1]) <= 3
        for i in range(len(lines) - 1)
    )

    # Increase counter if both conditions are met
    if is_monotonic and steps_valid:
        c += 1

# Print solution
print(f"Solution: {c}")