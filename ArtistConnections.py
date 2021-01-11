import random
from .Graph import *
from .SongLibrary import *
from .myQueue import*

class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.coartists = {}
        self.songs = {}
        self.numVertices = 0
        self.songArray = list()
        self.g = Graph()
    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """

    def load_graph(self, inputfilename):
        value = 1
        temp_artist =[]
        self.songArray = SongLibrary.loadLibrary(self, inputfilename)  # reading the file using songlibrary
        for line in self.songArray:


                temp_artist.append(line.artist)

                if self.g.getVertex(line.artist)   == None:
                    v = Vertex(line.artist)                  # checking if the vertex exists and if doesnt then adding it
                    self.g.addVertex(line.artist)

                if line.artist in temp_artist:
                    self.g.addSongs(line.artist,line.title)    # makes a songs array for each artist
                co1 = line.co.split(',')
                for i in co1:
                     self.g.addEdge(line.artist,i,value)
                     v.addNeighbor(i,value)     # adding connections between co artists

        t = self.g.getVertices()
        self.numVertices = len(t)       #  getting the number of vertexex
        return self.numVertices

    """
    Return song libary information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)

    """

    def search_artist(self, artist_name):

        numSongs = 0;
        artistLst = []
        for i in self.g.vertList:
            if i == artist_name:
                numSongs = len(self.g.getVertex(i).songs)
                for j in self.g.getVertex(i).coArtists:              # getting the co artists of the artists and the length of the artist's songs array
                    artistLst.append(j.id)
                    if i in artistLst:
                        artistLst.remove(i)                          # removing the search artists's name from artistlst


        return numSongs,artistLst

    """
    Return a list of two-hop neighbors of a given artist
    """

    def find_new_friends(self, artist_name):
        two_hop_friends = []
        t = self.g.getVertex(artist_name).getConnections()
        for i in t:
          t1 = i.getConnections()                      # getting the co artists of the artists
          for j in t1:

             two_hop_friends.append(j.id)             # getting the coartists of coartists and appending it to an array
             if artist_name in two_hop_friends:
                 two_hop_friends.remove(artist_name)

        for i in self.g.getVertex(artist_name).coArtists:
            if i.id in two_hop_friends:
                    two_hop_friends.remove(i.id)        # checking whether co artists of the artist are in two_hop_friends array and if yes then removing them

        two_hop_friends = list(set(two_hop_friends))

        return two_hop_friends

    """
    Search the information of an artist based on the artist name

    """

    def recommend_new_collaborator(self, artist_name):
        art=[]
        arr= [0]
        numSongs = 0
        maxSong = 0
        maxArtist = ""
        two_hop_friends1 = self.find_new_friends(artist_name)

        for i in two_hop_friends1:
            for j in self.g.getVertex(artist_name).getConnections():
                 if self.g.getVertex(i) in  self.g.getVertex(j.id).getConnections():     # checking if artists in two hop friends are co artists of all the collabarotors of the artist
                        arr[len(arr)-1] += self.g.getVertex(i).getWeight(j)           # and if yes then getting the weight and appending it to an array
                        if i not in art:
                           art.append(i)

            arr.append(0)

            """if numSongs > maxSong:
              maxSong = numSongs
              maxArtist = i"""

        maxSong = max(arr)
        maxArtist = art[arr.index(max(arr))]            # getting the maximum of the weights array and the artist associated with it

        return maxSong, maxArtist

    """
    Search the information of an artist based on the artist name

    """


    def shortest_path(self, artist_name):
        path = {}
        level = 0
        vertQueue = Queue()
        vertQueue.enqueue(self.g.getVertex(artist_name))
        last = vertQueue.items[0]  # keeping track of the last element
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            path[currentVert.id] =level     # adding the element getting dequeued and it's level into path dictionary
            if last == currentVert:         # checking if last one that got enqueued is the one that got dequeued
                level +=1                   # and if yes, then incrementing the level


            for nbr in self.g.vertList[currentVert.id].coArtists:
                if nbr.id not in path.keys() and nbr not in vertQueue.items:
                    vertQueue.enqueue(nbr)                # adding vertexes of the co artists to the queue if already is not added previously
            if vertQueue.items and currentVert == last:
                last = vertQueue.items[0]                 # defining the last element which got enqueued


        return path

### tests ###
if __name__ == '__main__':
    artistGraph = ArtistConnections()
    print(artistGraph.load_graph("TenKsongs_proj2.csv"))
    print(artistGraph.search_artist("Charlie Peacock"))
    print(artistGraph.recommend_new_collaborator("Green Day"))
    print(artistGraph.find_new_friends("Snowgoons"))
    print(artistGraph.shortest_path("Santana"))
