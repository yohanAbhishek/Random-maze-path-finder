"""
The maze is defined as a list of lists in this code, with 0s representing vacant cells and 1s signifying
obstacles.
"""

import random


def start_node():
    # Set x and y axis to generate the start node
    x_axis = random.randint(0, 1)
    y_axis = random.randint(0, 5)
    return x_axis, y_axis


def end_node():
    # Set x and y axis to generate the start node
    x_axis = random.randint(4, 5)
    y_axis = random.randint(0, 5)
    return x_axis, y_axis


def barriers(start, end):
    # Create a list to store 4 barriers
    barriers_list = []
    # Randomly select 4 barriers obeying the conditions
    while len(barriers_list) < 4:
        x_axis = random.randint(0, 5)
        y_axis = random.randint(0, 5)
        barrier = x_axis, y_axis
        if barrier != start and barrier != end and barrier not in barriers_list:
            barriers_list.append(barrier)
    return barriers_list


def generate_maze(start, end):
    # Initialize the barriers
    b = barriers(start, end)

    # Initialize outline for maze
    outline = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    print(f"\nStart node: {start} | End node: {end} | Barriers: {b}")

    # Replace the 0's for 1's where there's a barrier
    for barrier in b:
        outline[barrier[0]][barrier[1]] = 1
    return outline


def display(maze):
    # This is a method to print the maze
    for row in maze:
        for element in row:
            print(element, end=" ")
        print()
