def fill_grid(grid, n):
    # Define the formula from the problem: Value(i, j, k) = i + j + 2k + 1
    for k in range(n):  # for each layer
        for i in range(5):  # for each row in the 5x5 grid
            for j in range(5):  # for each column in the 5x5 grid
                if grid[k][i][j] == '?':
                    # grid[k][i][j] = i + j + 2 * k + 1
                    grid[k][i][j] = i + k - j
                else:
                    grid[k][i][j] = int(grid[k][i][j])  # Convert known values to integers

def find_treasure(grid, n):
    max_sum = float('-inf')
    treasure_layer = -1
    treasure_row = -1

    for k in range(n):  # for each layer
        for i in range(5):  # for each row in the 5x5 grid
            row_sum = sum(grid[k][i])
            if row_sum > max_sum:
                max_sum = row_sum
                treasure_layer = k
                treasure_row = i

    return treasure_layer, treasure_row

def parse_input():
    # Read n, the number of layers
    n = int(input().strip())
    grid = []

    for _ in range(n):
        layer = []
        for _ in range(5):  # Each layer has 5 rows
            row = input().strip().split()
            layer.append([cell if cell == '?' else int(cell) for cell in row])
        grid.append(layer)
   
    return grid, n

# Parse input
grid, n = parse_input()

# Fill in missing values and find the treasure
fill_grid(grid, n)
for row in grid[0]:
    print(" ".join(list(map(str, row))))
layer, row = find_treasure(grid, n)

# Output the result
print(f"{layer} {row}")