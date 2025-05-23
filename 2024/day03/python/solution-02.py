# Import libraries
from pathlib import Path 
import re

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

with input_path.open("r", encoding="utf-8") as f:
    input_str = f.read().strip()

#input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
matches = re.finditer(pattern, input_str)

solution = 0
mul_active = True
for match in matches:
    s = match.group(0)
    if s == "do()":
        mul_active = True
    elif s == "don't()":
        mul_active = False 
    else:
        if mul_active:
            x, y = match.groups()
            solution += int(x) * int(y)

print(f"Solution: {solution}")