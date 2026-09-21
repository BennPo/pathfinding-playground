import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import random

from perlin_noise import generate_noise
from pathfinding_playground import Solver


height_map = generate_noise(130105, 4, 20, 20, 0.05)

start = (random.randint(0,19), random.randint(0,19))
end = (random.randint(0,19), random.randint(0,19))
if start == end:
    end = (random.randint(0,19), random.randint(0,19))

print(height_map[0][10])

solver = Solver(
    height_map,
    start,
    end,
    1
)

path = solver.solve()
print(path)

if path is None:
    print("No path found")

else:
    # Coordinates for the terrain
    x = np.arange(height_map.shape[1])
    y = np.arange(height_map.shape[0])

    X, Y = np.meshgrid(x, y)

    # Get path coordinates
    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]

    # Get height of terrain at each path position
    path_z = [
        height_map[y][x]
        for x, y in path
    ]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(
        X,
        Y,
        height_map,
        alpha=0.6
    )
    ax.plot(
        path_x,
        path_y,
        path_z,
        linewidth=4
    )

    ax.scatter(
        path_x[0],
        path_y[0],
        path_z[0],
        s=80,
        label="Start"
    )

    ax.scatter(
        path_x[-1],
        path_y[-1],
        path_z[-1],
        s=80,
        label="End"
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Height")

    ax.legend()

    plt.tight_layout()
    plt.show()