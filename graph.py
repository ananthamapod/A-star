class Edge(object):
    """Edge Class, includes fields for cost and heuristic values"""
    def __init__(self, v1, v2):
        super(Edge, self).__init__()
        self.vertices = (v1, v2)
        self.h = 0
        self.g = 0

    """Setters"""
    def updateCost(self, g):
        self.g = g

    def updateHeuristic(self, h):
        self.h = h

    """Getters"""
    def getCost(self):
        return self.g

    def getHeuristic(self):
        return self.h

    """String representation"""
    def __str__(self):
        return str({
            "vs" : self.vertices,
            "h" : self.h,
            "g" : self.g
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

    def addVertex(self, x, y):
        key = (x, y)
        self.v[key] = True
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
