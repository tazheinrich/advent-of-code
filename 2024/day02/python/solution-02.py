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

# Define function to check if slope is monotonic and steps between and including 1 and 3
def is_valid(seq):
    return (
        all(seq[i] < seq[i+1] for i in range(len(seq) - 1)) or
        all(seq[i] > seq[i+1] for i in range(len(seq) - 1))
    ) and all(1 <= abs(seq[i] - seq[i+1]) <= 3 for i in range(len(seq) - 1))

# Iterate through intput
for line in input:
    lines = list(map(int, line.split()))

    # Increase counter if line is valid
    if is_valid(lines):
        c += 1
    # Remove element from list and check validity
    else:
        for i in range(len(lines)):
             # If removing one element from list makes line valid, increase counter
            new_lines = lines[:i] + lines[i+1:]
            if is_valid(new_lines):
                c += 1
                break

# Print solution
print(f"Solution: {c}")