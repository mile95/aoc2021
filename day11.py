with open("input.txt") as f:
    grid = f.read().splitlines()

grid = [list(map(int, row)) for row in grid]

STEPS = 100
potentials = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]

def compute_flashes(grid, flashing_left, flashed):
    if len(flashing_left) == 0:
        return grid, flashed
    for octopus in flashing_left:
        o_x, o_y = octopus
        for p_x, p_y in potentials:
            c_x, c_y = (o_x + p_x, o_y + p_y)
            if c_x >= 0 and c_y >= 0 and c_x < len(grid[0]) and c_y < len(grid):
                grid[c_x][c_y] += 1
                if grid[c_x][c_y] > 9:
                    if (c_x, c_y) not in flashed:
                        if (c_x, c_y) not in flashing_left:
                            flashing_left.append((c_x, c_y))
        flashing_left.remove(octopus)
        flashed.append(octopus)
    return compute_flashes(grid, flashing_left, flashed)

flashes = 0
count = 0
while(True):
    # Update
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
    # Flashing
    flashed = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if int(grid[i][j]) > 9:
                if (i,j) not in flashed:
                    grid, fs = compute_flashes(grid, [(i,j)], flashed)
                    flashed = flashed + fs

    flashes += len(set(flashed))
    # Reset
    for octopus in flashed:
        x, y = octopus
        grid[x][y] = 0
    
    done = True
    for r in grid:
        done = done and (r == [0]*len(r))
    if done:
        print(count)
        break
    count += 1
