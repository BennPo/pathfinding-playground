from pathfinding_playground import Solver
from perlin_noise import generate_noise
import random

start = (random.randint(0,19), random.randint(0,19))
end = (random.randint(0,19), random.randint(0,19))
if start == end:
    end = (random.randint(0,19), random.randint(0,19))


noise_map = generate_noise(random.randint(0,1000), 1, 20, 20, 0.5)

maze = [
    [1 if value < -0.1 else 0 for value in row]
    for row in noise_map
]

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