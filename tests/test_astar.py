from pathfinding_playground import Solver
import random

maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = (random.randint(0,9), random.randint(0,9))
end = (random.randint(0,9), random.randint(0,9))
if start == end:
    end = (random.randint(0,9), random.randint(0,9))


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