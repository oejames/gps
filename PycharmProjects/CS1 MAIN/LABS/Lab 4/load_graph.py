# Author: Ore James
# Date: 3/6/23
# Purpose: Create a dictionary of vertex objects

from vertex import Vertex


# create a load graph function
def load_graph(filename):

    # open the file given by the parameter
    fp = open(filename, "r")

    # create an empty vertex dictionary
    vertex_dict = {}

    # create vertex objects for each line in the file
    for l in fp:

        # strip each line in the file and split by semicolon
        line = l.strip()
        part = line.split("; ")

        # set vertex name as the first item in the split list
        vertex_name = part[0]

        # separate x and y
        xy = part[2].strip().split(", ")
        x = xy[0]
        y = xy[1]

        # create a vertex object for each vertex name and add to dictionary
        vertex_dict[vertex_name] = Vertex(vertex_name, [], x, y)

    # close the file
    fp.close()


    # reopen file
    fp = open(filename, "r")

    # create adjacency list for each vertex object:
    for lines in fp:

        # strip and split each line by semicolon, with vertex name as first item
        line = lines.strip()
        parts = line.split("; ")
        vertex_name = parts[0]

        # strip and split each item in adjacent (second item in the parts list created by split)
        adjacent = parts[1].strip().split(", ")

        # create an empty adjacent vertices list
        adjacent_vertices = []

        # add each item in adjacent (created by split) to the adjacent vertices list
        for a in adjacent:
            vertex_dict[vertex_name].adjacent_list.append(vertex_dict[a])

    # close the file
    fp.close()

    # return vertex dictionary
    return vertex_dict


# call load graph function with dartmouth_graph file
load_graph("dartmouth_graph.txt")


