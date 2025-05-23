# Import libraries
from pathlib import Path 
import re

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

with input_path.open("r", encoding="utf-8") as f:
    input_str = f.read().splitlines()

#input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

pairs = []

for line in input_str:
    matches = re.findall(pattern,line)
    pairs.extend([tuple(map(int, m)) for m in matches])

n = []
for p in pairs:
    n.append(p[0] * p[1])

solution = sum(n)

print(f"Solution: {solution}")


"""
# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

# Regex pattern to match mul(x,y)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Read input and compute the sum of products in one pass
with input_path.open("r", encoding="utf-8") as f:
    solution = sum(
        int(x) * int(y)
        for line in f
        for x, y in re.findall(pattern, line)
    )

print(f"Solution2: {solution}")
"""