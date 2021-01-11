from array import array
class Song:

    def __init__(self, songRecord):
        tokens=songRecord[:len(songRecord)-1].split(',')
        tokens1=";".join(tokens[5:]).split(';')
        tokens1 = ','.join(tokens1)
        if len(tokens) != 6:
            print("incorrect song record")
        else:
            self.title = tokens[1]
            self.artist = tokens[2]
            self.duration = tokens[3]
            self.trackID = tokens[4]
            self.co = tokens1      # making a global variable of the co artists string
    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


class SongLibrary:

    def __init__(self):
        self.songArray = list()
        self.isSorted = False
        self.size = 0

    def loadLibrary(self, inputFilename):

        with open(inputFilename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                song = Song(line)
                self.songArray.append(song)


        file.close()
        return self.songArray
    """
    Return song libary information
    """
    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)


