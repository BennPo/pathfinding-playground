from pathfinding_playground import Solver
import random

def test_solver_exists():
    assert Solver is not None

test_solver_exists()

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