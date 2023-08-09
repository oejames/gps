# Author: Ore James
# Date: 3/7/23
# Purpose: Create a breadth-first search algorithm function


from collections import deque
from load_graph import *
from vertex import *


def bfs(start_vertex, goal, dictionary): # dictionary parameter???????

    # set deque as queue
    queue = deque()

    # create empty dictionary for backpointers
    backpointer = {}

    # add the start vertex to the queue
    queue.append(start_vertex)

    # set the backpointer of start vertex as none (no backpointer to itself)
    backpointer[start_vertex] = None

    # loop while there are items in the queue
    while len(queue) > 0:

        # set vertexpop as the item popped from top of queue
        vertexpop = queue.popleft()

        # if vertex popped is the goal vertex create a path
        if vertexpop == goal:

            # set path as empty list
            path = []

            # loop until no backpointers left (starting point)
            while vertexpop is not None:

                # add vertex to the path list
                path.append(vertexpop)

                # move through rest of the backpointer dictionary by updating vertexpop
                vertexpop = backpointer[vertexpop]

            # return path list
            return path

        # if vertex popped is not the goal vertex add adjacent vertices to the queue and check those
        else:
            # check each adjacent vertex of the vertex popped
            for adj_vertex in vertexpop.adjacent_list:

                # if the adjacent vertex is not in the backpointer yet, add it to the queue (frontier) to check later
                if adj_vertex not in backpointer:
                    queue.append(adj_vertex)

                    # add adjacent vertex to the backpointer dictionary (backpointer is vertexpop)
                    backpointer[adj_vertex] = vertexpop














