from parser import readMazeFromFile
from graph import Graph, Edge
from fringeheap import Fringeheap
import math

"""Heuristic calculation function, uses Euclidean distance"""
def h(key, goal):
    return math.sqrt((key[0]-goal[0])**2 + (key[1]-goal[1])**2)

"""A* algorithm"""
def a_star(g, start, end):
    # bookkeeping structures, visited set and parents map
    visited = set()
    parents = {}

    # internal function for generating the path from the parents map
    def generatePath(origin, goal):
        #import pdb; pdb.set_trace()
        path = []
        curr = goal
        while curr.getCoordTuple() != origin.getCoordTuple():
            path.append(curr)
            curr = parents.get(curr.getCoordTuple())
        path.append(origin)
        path.reverse()
        return path

    start = g.v.get(start)
    goal = g.v.get(end)

    # preliminary input checks
    if not start or not goal:
        if not start:
            print "Not a valid starting node!"
        if not goal:
            print "Not a valid ending node!"
        return None

    for k,v in g.v.iteritems():
        v.updateHeuristic(h(k, end))

    fringe = Fringeheap()
    start.updateCost(0)
    fringe.push(start)

    while not fringe.isEmpty():
        curr = fringe.pop()
        if curr.getCoordTuple() == goal.getCoordTuple():
            return generatePath(start, curr)
        visited.add(curr)
        key = curr.getCoordTuple()
        for e in g.e.get(key):
            nKey = e.getNeighbor(key)
            neighbor = g.v.get(nKey)
            if neighbor in visited:
                continue
            cost = curr.getCost() + 1
            if not fringe.contains(neighbor):
                fringe.push(neighbor)
            elif cost >= neighbor.getCost():
                continue
            parents[nKey] = curr
            neighbor.updateCost(cost)
    return None

"""Clears the stored bookkeeping values in the graph vertices left over from previous search"""
def clearSearch(g):
    for k,v in g.v.iteritems():
        v.updateCost(float("inf"))
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
    filename = raw_input("Enter the path to the maze file: ")
    g = Graph()
    height, width, data = readMazeFromFile(filename, None)
    constructGraph(g, data, height, width)


    for i in xrange(height):
        print data[i]

    if raw_input("Raw search?(y/n): ") == "y":
        raw_search(g, width, height)

    print "Please provide start and goal for the search: "
    path = None
    try:
        startx = int(raw_input("starting index x: "))
        starty = int(raw_input("starting index y: "))
        goalx = int(raw_input("ending index x: "))
        goaly = int(raw_input("ending index y: "))

        path = a_star(g, (starty,startx),(goaly,goalx))
    except Exception as e:
        pass
    
    if path == None:
        print "No valid path could be found"
        clearSearch(g)
    else:
        for i in path:
            print i.getCoordTuple()

if __name__ == '__main__':
    main()
