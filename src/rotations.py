class Rotations:
    def clockwise_turn(grid, grid_size):
        new_grid = [[True for _ in range(grid_size)] for _ in range(grid_size)]
        for i in range(grid_size):
            for j in range(grid_size):
                new_grid[i][j] = grid[grid_size-j-1][i]
        return new_grid

    def anticlockwise_turn(grid, grid_size):
        new_grid = [[True for _ in range(grid_size)] for _ in range(grid_size)]
        for i in range(grid_size):
            for j in range(grid_size):
                new_grid[i][j] = grid[j][grid_size-i-1]
        return new_grid

    def full_turn(grid, grid_size):
        new_grid = [[True for _ in range(grid_size)] for _ in range(grid_size)]
        for i in range(grid_size):
            for j in range(grid_size):
                new_grid[i][j] = grid[grid_size-i-1][grid_size-j-1]
        return new_grid