# Import libraries
from pathlib import Path 

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

with input_path.open("r", encoding="utf-8") as f:
    input = f.read()

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# Create the grid
grid = [list(row) for row in input.strip().split('\n')]
num_rows = len(grid)
num_cols = len(grid[0])

# String to look for
xmas = list("XMAS")

ans = 0

# Direction vectors: (dy, dx)
directions = [
    (0, 1),   # right 
    (0, -1),  # left 
    (1, 0),   # down 
    (-1, 0),  # up 
    (1, 1),   # diagonal top left down right
    (-1, -1), # diagonal top right down left
    (1, -1),  # diagonal top left down left
    (-1, 1),  # diagonal top right down right
]

for i in range(num_rows):
    for j in range(num_cols):
        for dy, dx in directions:
            try:
                if all(
                    0 <= i + k * dy < num_rows and
                    0 <= j + k * dx < num_cols and
                    grid[i + k * dy][j + k * dx] == xmas[k]
                    for k in range(4)
                ):
                    ans += 1
            except IndexError:
                continue

print(ans)
