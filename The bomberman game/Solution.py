def bomberMan(n, grid):
    if n == 1:
        return grid
    r, c = len(grid), len(grid[0])

    def detonate(grid):
        new_grid = [['O'] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    new_grid[i][j] = '.'
                    if i > 0:
                        new_grid[i - 1][j] = '.'
                    if i < r - 1:
                        new_grid[i + 1][j] = '.'
                    if j > 0:
                        new_grid[i][j - 1] = '.'
                    if j < c - 1:
                        new_grid[i][j + 1] = '.'
        return [''.join(row) for row in new_grid]

    state_after_detonate = detonate(grid)
    if n % 2 == 0:
        return ['O' * c for _ in range(r)]
    elif n == 3:
        return state_after_detonate
    else:
        grid_after_second_detonate = detonate(state_after_detonate)
        grid_after_third_detonate = detonate(grid_after_second_detonate)
        return grid_after_second_detonate if n % 4 == 1 else grid_after_third_detonate


print(bomberMan(5, grid =['.......', '...O.O.', '....O..', '..O....', 'OO...OO', 'OO.O...']))