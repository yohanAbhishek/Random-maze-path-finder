"""
This is an algorithm showcasing the depth first search being executed in a maze to find the end goal from a given
start with 4 barriers.The directions list specifies the order in which surrounding cells will be explored (in this
case, north, east, west, south, NE, SE, SW, and NW) Starting at the beginning, the algorithm explores the nearby
cells, marking them as visited and adding them to a stack as it proceeds. If all of a cell's neighbors have been
visited, the algorithm returns to the most recent cell in the stack and resumes the search from there. This method is
continued until the end position is reached or no path to the end position is found.
"""

import model.generate as generate

# define the starting position (row, column)
start = generate.start_node()


def getStart():
    return start


# define the ending position (row, column)
end = generate.end_node()


def getEnd():
    return end


# define the maze as a 2D list of integers
maze = generate.generate_maze(start, end)


def getMaze():
    return maze


# Directions->   N        E        W        S         NE       SE        SW         NW
#            [(0, -1), (+1, 0), (-1, 0), (0, +1), (+1, -1), (+1, +1), (-1, +1), (-1, -1)]

# Define the directions to explore in ascending order
directions = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]


def getDirections():
    return directions


# Initialize a stack to store the path
path = []

# Initialize a set to store the visited cells(Doesn't store duplicate values)
visited = set()

# Set the current position to the start position
x_axis, y_axis = start


def executeSearch():
    # Repeat the search until the end position is reached, or it is determined that there is no path
    global y_axis, x_axis
    while (x_axis, y_axis) != end:
        # Mark the current cell as visited
        visited.add((x_axis, y_axis))

        # Explore the neighboring cells
        for d in directions:
            # Calculate the row and column of the neighbor
            row = x_axis + d[0]
            col = y_axis + d[1]
            # Check if the neighbor is within the bounds of the maze and not a barrier
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                # If the neighbor has not been visited before, add it to the stack and set it as the current cell
                if (row, col) not in visited:
                    path.append((row, col))
                    x_axis, y_axis = row, col
                    break
        else:
            # If all neighbors have been visited, backtrack to the most recent cell in the stack
            x_axis, y_axis = path.pop()


def chebyshev_distance(x1, y1, x2, y2):
    # Calculate the Chebyshev distance between goal node and start node
    return max(abs(x1 - x2), abs(y1 - y2))


def getPath():
    return path


def getVisited():
    return visited


# Time will be calculated as 1 minute per visited node
def getTime():
    return f"The algorithm took {len(visited)} minutes to find a solution. The time taken for the shortest path" \
           f" is {len(path)} minutes"
