# Import libraries
from collections import Counter
from pathlib import Path 

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

# Read and parseinput 
with input_path.open("r") as file:
    pairs = [tuple(map(int, line.strip().split())) for line in file if line.strip()]

# Unzip into two parts
l, r = zip(*pairs)

"""
Faster solution importing Counter:
- Counts occurences of values in list r and stores as dictionary
- For each value in l multiply value with count in r, summarize solution
- Number of lookups O(1)
"""

# Count occurrences in right list
r_counts = Counter(r)

# Multiply each value in l with its count in r
solution = sum(val * r_counts[val] for val in l)

"""
Slower solution with loop:
- Looking up each value of l in r
- Counting occurences of val of l in r
- Multiplicing count with val of l
- Appending to list of counts c
- Summarizing c 
- Number of lookups O(n)
"""

# # Multiply value of left list with count in right list
# c = []
# for val in l:
#     c.append(val * r.count(val))

# # Sum for solution
# solution = sum(c)

# Print solution
print(f"Solution: {solution}")