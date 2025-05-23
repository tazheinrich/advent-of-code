# Import libraries
from pathlib import Path 

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

with input_path.open("r", encoding="utf-8") as f:
    input = f.read()

# Create the grid
grid = [list(row) for row in input.strip().split('\n')]
num_rows = len(grid)
num_cols = len(grid[0])

# Define string to search for
xmas = list("XMAS")

# Define directions
directions = [
    (0, 1),   # right
    (0, -1),  # left
    (1, 0),   # down
    (-1, 0),  # up
    (1, 1),   # diagonal down-right
    (-1, -1), # diagonal up-left
    (1, -1),  # diagonal down-left
    (-1, 1),  # diagonal up-right
]

# Initialize answer counter
ans = 0

# Loop through grid
for i in range(num_rows):
    for j in range(num_cols):
        for dy, dx in directions:
            # Check boundaries for the whole string "XMAS" before accessing grid
            end_i = i + 3 * dy
            end_j = j + 3 * dx
            if 0 <= end_i < num_rows and 0 <= end_j < num_cols:
                # Now check all four letters
                if all(grid[i + k * dy][j + k * dx] == xmas[k] for k in range(4)):
                    ans += 1

print(ans)
