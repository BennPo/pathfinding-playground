from pathfinding_playground import Solver
from perlin_noise import generate_noise
import random

start = (random.randint(0,20), random.randint(0,20))
end = (random.randint(0,20), random.randint(0,20))
if start == end:
    end = (random.randint(0,20), random.randint(0,20))



maze = [[None for _ in range(20)]for _ in range(20)]

noise_map = generate_noise(130105, 1, 20, 20, 0.5)


for a in range(len(noise_map)):
    for b in range(len(noise_map[a])):
        if noise_map[a][b] *100 < -0.15*100:
            maze[a][b] = 1
        else:
            maze[a][b] = 0

print("Start:", start, maze[start[1]][start[0]])
print("End:", end, maze[end[1]][end[0]])

maze[start[1]][start[0]] = 0
maze[end[1]][end[0]] = 0

solver = Solver(
    maze,
    start,
    end
)

path = solver.solve()

if path is None:
    print("No path found")

else:
    print("Path:")
    print(path)

    print("\nPath length:")
    print(len(path) - 1)

    print("\nMaze:")
    solver.print_maze(path)