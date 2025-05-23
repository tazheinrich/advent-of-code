# Import libraries
from pathlib import Path 

# Define input path
script_dir = Path(__file__).resolve().parent
input_path = script_dir.parent / "input01.txt"

with input_path.open("r", encoding="utf-8") as f:
    input = f.read()

grid = [list(row) for row in input.strip().split("\n")]
num_rows = len(grid)
num_cols = len(grid[0])

# String to look for
mas = list("MAS")

# Define diagonals
diagonal_offsets = [
    [(-1, -1), (1, 1)],
    [(-1, 1), (1, -1)]
]

# Initialize answer
ans = 0

# Loop through grid
for i in range(num_rows):
    for j in range(num_cols):
        # Skip if no A at location
        if grid[i][j] != mas[1]:  # Check for A
            continue
        
        # Initialize counter
        count = 0
        # Loop through diagonals
        for offsets in diagonal_offsets:
            # Define locations
            y1, x1 = i + offsets[0][0], j + offsets[0][1]
            y2, x2 = i + offsets[1][0], j + offsets[1][1]

            # Check boundaries
            if (0 <= y1 < num_rows and 0 <= x1 < num_cols and
                0 <= y2 < num_rows and 0 <= x2 < num_cols):
                # Search for MAS in diagonals
                if (grid[y1][x1] == mas[0] and grid[y2][x2] == mas[2]) or \
                   (grid[y1][x1] == mas[2] and grid[y2][x2] == mas[0]):
                    count += 1

        if count >= 2:
            ans += 1

print(ans)
