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

# Convert to grid
grid = [list(row) for row in input.strip().split("\n")]
num_rows = len(grid)
num_cols = len(grid[0])

# String to look for
mas = list("MAS")

# Directions: (dy, dx) pairs for diagonals with A in the middle
diagonal_offsets = [
    [(-1, -1), (1, 1)],  
    [(-1, 1), (1, -1)]    
]

ans = 0

for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] != mas[1]:
            continue

        count = 0  # Count how many "MAS" diagonals this A is in

        for offsets in diagonal_offsets:
            try:
                y1, x1 = i + offsets[0][0], j + offsets[0][1]
                y2, x2 = i + offsets[1][0], j + offsets[1][1]

                if (
                    0 <= y1 < num_rows and 0 <= x1 < num_cols and
                    0 <= y2 < num_rows and 0 <= x2 < num_cols and
                    grid[y1][x1] == mas[0] and grid[y2][x2] == mas[2] or 
                    0 <= y1 < num_rows and 0 <= x1 < num_cols and
                    0 <= y2 < num_rows and 0 <= x2 < num_cols and
                    grid[y1][x1] == mas[2] and grid[y2][x2] == mas[0]
                ):
                    count += 1
            except IndexError:
                continue 

        if count >= 2:
            ans += 1

print(ans)
