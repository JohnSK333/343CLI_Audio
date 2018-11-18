

class Libary:
    def __init__(self, size):
        self.songList = [None] * size

    def addToLibary(self, song):
        self.songList + song

    def __str__(self):
        st = "This Library holds: \n\n"
        for i in self.songList:
            st = st + str(i) + '\n'
        return st

    def chooseSong(self, song):
        for i in self.songList:
            if(self.songList[i] == song):
                return self.songList[i]

