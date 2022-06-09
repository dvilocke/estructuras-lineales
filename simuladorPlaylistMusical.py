import time
class Song:
    def __init__(self, name_song, execution_time):
        self.name_song = name_song
        self.execution_time = execution_time
        self.next = None


class PlayList:
    def __init__(self):
        self.front = None
        self.end = None
        self.number_of_songs = 0

    def __len__(self):
        return self.number_of_songs

    def __contains__(self, item):
        return True if item in self.__iter__() else False

    def __iter__(self):
        auxiliar = self.front
        while auxiliar is not None:
            yield auxiliar.name_song
            auxiliar = auxiliar.next


    def play(self):

        while True:
            song_to_play = self.pop()
            if song_to_play:
                print(f'Song to play:{song_to_play.name_song}')
                print(f'playing time:{song_to_play.execution_time}')
                time.sleep(song_to_play.execution_time)
            else:
                break

        print('all songs finish playing')

    def pop(self):
        if self.front:
            song = self.front

            if self.front.next:
                self.front = self.front.next
            else:
                self.front = None

            song.next = None
            return song

        else:
            return None

    def add_song(self, song : Song):
        if not self.front:
            self.front = song
            self.end = song
        else:
            self.end.next = song
            self.end = song

        self.number_of_songs += 1


if __name__ == '__main__':
    myList = PlayList()

    song1 = Song(name_song='song1', execution_time=3)
    song2 = Song(name_song='song2', execution_time=4)
    song3 = Song(name_song='song3', execution_time=2)



    myList.add_song(song1)
    myList.add_song(song2)
    myList.add_song(song3)


    myList.play()

