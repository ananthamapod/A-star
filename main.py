from parser import readMazeFromFile
from graph import Graph, Edge
import math

"""Heuristic calculation function, uses Euclidean distance"""
def h(key, goal):
    return math.sqrt((key[0]-goal[0])**2 + (key[1]-goal[1])**2)

"""A* algorithm"""
def a_star(g, start, end):
    for k,v in g.v.iteritems():
        v.updateHeuristic(h(k, end))

def clearSearch(g):
    for v in g.v:
        v.updateCost(0)
        v.updateHeuristic(0.0)

"""Function for constructing graph from parsed maze data"""
def constructGraph(g, data, height, width):
    for i in xrange(height):
        for j in xrange(width):
            if data[i][j] == '.':
                g.addVertex(i, j)

    for i in xrange(height):
        for j in xrange(width):
            curr = data[i][j]
            if curr == '.':
                key1 = (i, j)
                if j < width-1:
                    right = data[i][j+1]
                    if right == '.':
                        key2 = (i, j+1)
                        g.addEdge(key1, key2)
                if i < height-1:
                    bottom = data[i+1][j]
                    if bottom == '.':
                        key2 = (i+1, j)
                        g.addEdge(key1, key2)

"""Checker function that searches through graph structure to check existence of vertices"""
def raw_search(g, width, height):
    while True:
        try:
            a = int(raw_input("search: "))
            if a >= 0 and a < height:
                for i in xrange(width):
                    if not g.v.get((a, i)):
                        print i
        except Exception as e:
            break

def main():
    filename = "maze.txt"#raw_input("Enter the name of the maze file: ")
    g = Graph()
    height, width, data = readMazeFromFile("tests/" + filename, None)
    constructGraph(g, data, height, width)


    for i in xrange(height):
        print data[i]

    if raw_input("Raw search?(y/n): ") == "y":
        raw_search(g, width, height)
    import pdb; pdb.set_trace()
    a_star(g, (0,0),(11,11))
    print "a"

if __name__ == '__main__':
    main()
