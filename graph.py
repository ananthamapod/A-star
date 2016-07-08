class Vertex(object):
    """Vertex Class, includes fields for cost and heuristic values"""
    def __init__(self, y, x):
        super(Vertex, self).__init__()
        self.y = y
        self.x = x
        self.h = 0.0
        self.g = float('inf')
        self.f = float('inf')

    """Setters"""
    def updateCost(self, g):
        self.g = g
        self.f = self.g + self.h

    def updateHeuristic(self, h):
        self.h = h
        self.f = self.g + self.h

    """Getters"""
    def getCost(self):
        return self.g

    def getHeuristic(self):
        return self.h

    """String representation"""
    def __str__(self):
        return str({
            "pos" : (self.y, self.x),
            "h" : self.h,
            "g" : self.g
        })

    """Comparison function"""
    def __cmp__(self, other):
        return

class Edge(object):
    """Edge Class"""
    def __init__(self, v1, v2):
        super(Edge, self).__init__()
        self.vertices = (v1, v2)

    """String representation"""
    def __str__(self):
        return str({
            "vs" : self.vertices
        })

    """Comparison function"""
    def __eq__(self, other):
        for i in other.vertices:
            if i not in self.vertices:
                return False
        return True


class Graph(object):
    """Graph Class"""
    def __init__(self):
        super(Graph, self).__init__()
        self.v = {}
        self.e = {}

    def addVertex(self, y, x):
        key = (y, x)
        v = Vertex(y, x)
        self.v[key] = v
        self.e[key] = []

    def addEdge(self, key1, key2):
        if self.v.get(key1) and self.v.get(key2):
            edge = Edge(key1, key2)
            if edge in self.e[key1] or edge in self.e[key2]:
                raise Exception("This edge already exists")
            else:
                self.e[key1].append(edge)
                self.e[key2].append(edge)
        else:
            raise Exception("One of both of those vertices do not exist")

    """ String representation"""
    def __str__(self):
        return str({
            "v" : str(self.v),
            "e" : str(self.e)
        })

    def printEdges(self):
        for k,v in self.e.iteritems():
            print k
            print map(str, v)
            raw_input(">")
