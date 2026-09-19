import heapq
import math
import random

class Solver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end

        self.max_height = len(maze)
        self.max_width = len(maze[0])

        self.open_set = []

        self.closed_set = set()

        self.g_score = {
            self.start: 0
        }

        self.came_from = {
            self.start: None
        }

        start_h = self.heuristic(self.start)

        heapq.heappush(
            self.open_set,
            (start_h, self.start)
        )

    def heuristic(self, pos):
        x, y = pos
        end_x, end_y = self.end

        return (
            math.sqrt((pos[0]-self.end[0])**2 + (pos[1]-self.end[1])**2)
        ) * 10

    def get_neighbours(self, pos):
        x, y = pos
        directions = [
            (1, 0),    # right
            (-1, 0),   # left
            (0, -1),   # up
            (0, 1)     # down
        ]

        neighbours = []

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            # Check inside maze
            if not (
                0 <= new_x < self.max_width
                and
                0 <= new_y < self.max_height
            ):
                continue

            # Check that the cell is not a wall
            if self.maze[new_y][new_x] == 1:
                continue

            neighbours.append(
                (new_x, new_y)
            )

        return neighbours

    def solve(self):
        while self.open_set:

            # Get node with lowest f score
            current_f, current = heapq.heappop(
                self.open_set
            )

            if current in self.closed_set:
                continue

            if current == self.end:
                return self.traceback()

            # Mark current node as checked
            self.closed_set.add(current)

            # Look through its neighbours
            for neighbour in self.get_neighbours(current):

                if neighbour in self.closed_set:
                    continue

                # Movement up/down/left/right costs 10
                new_g = self.g_score[current] + 10

                if (
                    neighbour not in self.g_score
                    or
                    new_g < self.g_score[neighbour]
                ):

                    # Save new best distance
                    self.g_score[neighbour] = new_g

                    self.came_from[neighbour] = current

                    h = self.heuristic(neighbour)

                    f = new_g + h

                    heapq.heappush(
                        self.open_set,
                        (f, neighbour)
                    )

        return None

    def traceback(self):
        path = []

        current = self.end

        while current is not None:

            path.append(current)

            current = self.came_from[current]

        path.reverse()

        return path

    def print_maze(self, path=None):
        display = [
            row.copy()
            for row in self.maze
        ]

        if path:

            for x, y in path:

                if (x, y) != self.start and (x, y) != self.end:
                    display[y][x] = "*"

        for y in range(self.max_height):
            line = ""
            for x in range(self.max_width):
                pos = (x, y)
                if pos == self.start:
                    line += "S "
                elif pos == self.end:
                    line += "E "
                elif display[y][x] == 1:
                    line += "# "
                elif display[y][x] == "*":
                    line += "* "
                else:
                    line += ". "
            print(line)

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