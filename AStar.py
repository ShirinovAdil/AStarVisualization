# PSEUDOCODE OF  A* Search Algorithm
"""
1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open
    list (you can leave its f at zero)

3.  while the open list is not empty
    a) find the node with the least f on
       the open list, call it "q"

    b) pop q off the open list

    c) generate q's 8 successors and set their
       parents to q

    d) for each successor
        i) if successor is the goal, stop search
          successor.g = q.g + distance between
                              successor and q
          successor.h = distance from goal to
          successor (This can be done using many
          ways, we will discuss three heuristics-
          Manhattan, Diagonal and Euclidean
          Heuristics)

          successor.f = successor.g + successor.h

        ii) if a node with the same position as
            successor is in the OPEN list which has a
           lower f than successor, skip this successor

        iii) if a node with the same position as
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)

    e) push q on the closed list
    end (while loop)
"""


import numpy as np
import Board


class Node:
    """A node class for A*"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # From current node to start node
        self.h = 0  # Heuristic -> Estimated from current to end(destination)
        self.f = 0  # F = G + H

    def __eq__(self, other):
        return self.position == other.position


def AStar(maze, start, end):

    # Create start and end node
    # Setting F = G + H to 0
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]  # Start_node at first loop
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Check if reached the destination
        if current_node == end_node:
            path = []  # Will keep traversed path
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Traverse the path back

        # Generate children, explained below
        children = []
        # Smejniye kvadrati
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure new square is within the range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            if Node(current_node, node_position) in closed_list:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append new node to children list
            children.append(new_node)

        for child in children:

            # Child is on the closed list already
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


class Green:
    TO_GREEN = None

    def __init__(self, path):
        Green.TO_GREEN = path


def main():
    # print("IN")
    obj1 = Board.chess_board(13)


def solve(obj1):
    maze = obj1.returnChessArray()
    temp_maze = np.array(maze)
    maze = (temp_maze.T).tolist()
    # print(maze)

    start = obj1.startXY
    end = obj1.endXY

    path = AStar(maze, start, end)
    print(path)
    return path


if __name__ == '__main__':
    main()


"""
        Generating all the 8 successor of this cell

            N.W   N   N.E
              \   |   /
               \  |  /
            W----Cell----E
                 / | \
               /   |  \
            S.W    S   S.E

        Cell-->Popped Cell (i, j)
        N -->  North       (i-1, j)
        S -->  South       (i+1, j)
        E -->  East        (i, j+1)
        W -->  West           (i, j-1)
        N.E--> North-East  (i-1, j+1)
        N.W--> North-West  (i-1, j-1)
        S.E--> South-East  (i+1, j+1)
        S.W--> South-West  (i+1, j-1)*/

        // To store the 'g', 'h' and 'f' of the 8 successors
        double gNew, hNew, fNew;

        //----------- 1st Successor (North) ------------
"""
