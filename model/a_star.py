"""
This is the A* algorithm implemented to use a heuristic cost(Chebyshev Distance) and calculate the shortest path from
the start node to the goal node. It can be seen that this algorithm outperforms the DFS algorithm as it performs a path
cost calculation to the goal before advancing.
"""

import model.dfs as dfs

start = dfs.getStart()  # define the starting position (row, column)
end = dfs.getEnd()  # define the ending position (row, column)
maze = dfs.getMaze()  # define the maze as a 2D list of integers
directions = dfs.getDirections()  # Define the directions to explore in ascending order


visited = set()  # Initialize a set to store the visited cells(Doesn't store duplicate values)
queue = []  # Initialize a queue to store the cells that need to be visited
parent = {}  # Initialize a dictionary to store the parents of each cell
cost = {start: 0}  # Initialize dict to store cost of visiting each cell (# Set cost of visiting  starting cell to 0)

# Calculate the heuristic cost of the starting cell using the Chebyshev distance
h_cost = dfs.chebyshev_distance(start[0], start[1], end[0], end[1])

queue.append((h_cost, start))  # Add the starting cell to the queue with the total cost (g_cost + h_cost)

x_axis, y_axis = start  # Set the current position to the start position


# Repeat the search until the end position is reached, or it is determined that there is no path
def executeSearch():
    global queue
    while queue:
        queue = sorted(queue, key=lambda x: x[0])  # Sort queue in ascending order based on the total cost of each cell

        _, current = queue.pop(0)  # Get the cell with the lowest total cost

        visited.add(current)  # Mark the current cell as visited

        if current == end:  # If the current cell is the end position, break the loop
            break

        # Explore the neighboring cells
        for d in directions:
            # Calculate the row and column of the neighbor
            row = current[0] + d[0]
            col = current[1] + d[1]

            # Check if the neighbor is within the bounds of the maze and not a barrier
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                # If the neighbor has not been visited before, add it to the queue and store its parent and cost
                if (row, col) not in visited:
                    g_cost = cost[current] + 1  # Calculate the cost of visiting the neighbor
                    h_cost = dfs.chebyshev_distance(row, col, end[0], end[1])  # Calculate heuristic cost of neighbor
                    f_cost = g_cost + h_cost  # Calculate the total cost of the neighbor
                    queue.append((f_cost, (row, col)))  # Add the neighbor to the queue with the total cost
                    parent[(row, col)] = current  # Store the parent of the neighbor
                    cost[(row, col)] = g_cost  # Store the cost of visiting the neighbor
    backTrack()


# Initialize a list to store the shortest path
shortest_path = []


# Backtrack from the end position to the start position to get the shortest path
def backTrack():
    current = end
    while current != start:
        shortest_path.append(current)  # Add the current cell to the shortest path
        current = parent[current]  # Set the current cell to its parent


shortest_path.append(start)  # Add the starting cell to the shortest path
shortest_path = shortest_path[::-1]  # Reverse the shortest path to get the path from start to end


def getShortestPath():
    return shortest_path


def getVisitedNodes():
    return visited


def getTime():
    return f"The algorithm took {len(visited)} minutes to find a solution. The time taken for the shortest path" \
           f" is {len(shortest_path)} minutes"
