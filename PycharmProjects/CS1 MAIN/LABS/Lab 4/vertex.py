# Author: Ore James
# Date: 3/6/23
# Purpose: Create a vertex class

from cs1lib import *

VERTEX_RADIUS = 10
EDGE_WIDTH = 4


# create a vertex class
class Vertex:

    def __init__(self, name, adjacent_list, x, y):

        # initialize parameters
        self.name = str(name)
        self.x = int(x)
        self.y = int(y)
        self.adjacent_list = adjacent_list

    def draw_vertex(self, r, g, b):

        # draw vertex as a circle
        set_fill_color(r, g, b)
        set_stroke_width(0)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    def draw_edges(self, r, g, b):

        # draw an edge between all adjacent vertices in the list
        for vertex in self.adjacent_list:

            # draw line from the vertex to item in adjacent list
            set_stroke_color(r, g, b)
            set_stroke_width(EDGE_WIDTH)
            draw_line(self.x, self.y, vertex.x, vertex.y)


    # method to determine if a point (parameters x and y) is in the surrounding area of the vertex
    def is_in_surrounding(self, an_x, a_y):

        # return true if the given x and y are within a range from the vertex's center coordinates
        if (self.x - VERTEX_RADIUS) <= an_x <= (self.x + VERTEX_RADIUS) and (self.y - VERTEX_RADIUS) <= a_y <= (self.y + VERTEX_RADIUS):
            return True

        # if not in range, return false
        else:
            return False


    # method to draw an edge between another vertex
    def draw_an_edge(self, vertex, r, g, b):

        # draw a line between vertex and the other vertex
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, vertex.x, vertex.y)


    # create a string method
    def __str__(self):

        # create a string to hold the adjacent vertices
        adj_string = ""

        # add name of each adjacent vertex to adjacent vertices string
        for place in self.adjacent_list:

            # if it is the last vertex in the list, do not add a comma; add to adjacent vertices string
            if self.adjacent_list[len(self.adjacent_list) - 1] == place:
                adj_string += place.name

            # add a comma after everything else in the list; add to adjacent vertices string
            else:
                adj_string += place.name + ", "

        # return a string containing the name, location, and adjacent vertices
        return self.name + "; " + "Location: " + str(self.x) + "," + str(self.y) + "; " + "Adjacent vertices: " + adj_string
