from parser import readMazeFromFile
from graph import Graph, Edge

def a_star(graph, start, end):
    pass

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

def raw_search(g):
    while True:
        try:
            a = int(raw_input("search: "))
            print a
            for i in xrange(width):
                print a
                if not g.v.get((a, i)):
                    print i
        except Exception as e:
            break

def main():
    filename = raw_input("Enter the name of the maze file: ")
    g = Graph()
    height, width, data = readMazeFromFile("tests/" + filename, None)
    constructGraph(g, data, height, width)


    for i in xrange(height):
        print data[i]

    if raw_input("Search?(y/n): ") == "y":
        raw_search(g)

if __name__ == '__main__':
    main()
