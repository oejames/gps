# Author: Ore James
# Date: 3/7/23
# Purpose: Code for drawing


from load_graph import *
from vertex import *
from cs1lib import *
from bfs import bfs


# set vertex_dict variable as value returned by load graph
vertex_dict = load_graph("dartmouth_graph.txt")


# load the map image
img = load_image("dartmouth_map.png")


# initialize global variables
clicking = False
hoverx = 0
hovery = 0


# draw the vertices and edges on the map
def draw():

    # draw each vertex and edge in the vertex dictionary
    for vertex in vertex_dict:

        # draw each vertex as a blue circle using the method from vertex class
        vertex_dict[vertex].draw_vertex(0, 0, 1)

        # draw the blue edges between each vertex using the draw_edges method
        vertex_dict[vertex].draw_edges(0, 0, 1)


# set what happens when the mouse is moved (hover over map)
def move(mx, my):
    global hoverx, hovery
    hoverx = mx
    hovery = my


# setting what happens when mouse is pressed
def press(mx, my):
    global clicking, clickx, clicky
    clicking = False
    clickx = mx
    clicky = my


# setting what happens when mouse is released (make clicking true)
def release(mx, my):
    global clicking
    clicking = True


# create function to draw paths
def draw_paths():
    global start, clickx, clicky, clicking, goal, hoverx, hovery

    # check dictionary for a start vertex
    for clickvertex in vertex_dict:

        # proceed if mouse has been clicked and released
        if clicking:

            # check if the area user is clicking on is a vertex on the map
            if vertex_dict[clickvertex].is_in_surrounding(clickx, clicky):

                # set clicked vertex as start vertex
                start = vertex_dict[clickvertex]

                # turn the vertex red
                vertex_dict[clickvertex].draw_vertex(1, 0, 0)


                # check dictionary for a hover vertex when clicked vertex is found
                for hoververtex in vertex_dict:

                    # check if the mouse is hovering over a vertex
                    if vertex_dict[hoververtex].is_in_surrounding(hoverx, hovery):

                        # set end goal vertex as hover vertex
                        goal = vertex_dict[hoververtex]

                        # turn hover vertex red
                        vertex_dict[hoververtex].draw_vertex(1, 0, 0)


                # when start and goal vertices have both been found, draw path between them
                if start is not None and goal is not None:

                    # set path as list returned by breadth-first search (the shortest path between start and goal)
                    path = bfs(start, goal, vertex_dict)

                    # draw edge between each item in path list, starting at first index
                    pathindex = 0

                    # draw edge between each vertex in the path list
                    while pathindex < len(path) - 1:

                        # draw the vertex in path as red
                        path[pathindex].draw_vertex(1, 0, 0)

                        # draw an edge between the vertex and the next vertex in path
                        path[pathindex].draw_an_edge(path[pathindex+1], 1, 0, 0)

                        # increment path index
                        pathindex = pathindex + 1


def main():

    clear()

    # draw map image
    draw_image(img, 0, 0)

    # call draw function
    draw()

    # call drawing path function
    draw_paths()



start_graphics(main, width=1012, height=811, mouse_press=press, mouse_release=release, mouse_move = move)


