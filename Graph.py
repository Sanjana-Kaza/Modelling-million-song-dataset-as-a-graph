class Vertex:
    def __init__(self, artist):
        self.id = artist
        self.songs = []
        self.coArtists = {}

    def addNeighbor(self, nbr, weight=0):
         if nbr not in self.coArtists:
             self.coArtists[nbr] = weight

         else:
             self.coArtists[nbr] = self.coArtists[nbr]+ 1  # incrementing the weight if the connection already exists

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.coArtists])

    def getConnections(self):
        return self.coArtists.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.coArtists[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f],cost)      # updating the vertlist both ways
    def getVertices(self):
        return self.vertList.keys()

    def addSongs(self,f,title):
        self.vertList[f].songs.append(title)
    def getSongs(self):
        return self.vertList[f].songs
    def __iter__(self):
        return iter(self.vertList.values())


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    g = Graph()
    for i in range(5):
        g.addVertex(i)

    g.addEdge(1,2,1)
    g.addEdge(1,5,2)
    g.addEdge(2,5,3)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
