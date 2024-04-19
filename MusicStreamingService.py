from abc import ABC, abstractmethod

class Music(ABC):
    @abstractmethod
    def play(self):
        pass
class MusicOperations(ABC):
    @abstractmethod
    def listen_song(self):
        pass

class Rock(Music):
    def play(self):
        print("Playing rock music")
class Pop(Music):
    def play(self):
        print("Playing pop music")

class Song:
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length
    
class Album:
    def __init__(self, title, artist, relase_date):
        self.title = title
        self.artist = artist
        self.relase_date = relase_date

class Playlist:
    def __init__(self, name):
        self.name= name
        self.included_songs = []

class MusicStreamingService(MusicOperations):
    def __init__(self):
        self.songs = []
        self.playlist = []


    def create_playlist(self, playlist):
        self.playlist.append(playlist)

    def manage_playlist(self, playlist):
        self.playlist.remove(playlist)

    def search_song(self, song):
        print(f"The song is : {song.title}")

    def listen_song(self, song):
        print(f"You are listening {song.name}")
        
song1 = Song("Song 1", "Artist 1", 2)
song2 = Song("Song 2", "Artist 2", 4)
album1 = Album("Album1", "Artist1", 28)
playlist1 = Playlist("Playlist1")

service = MusicStreamingService()
service.songs.append(song1)
service.songs.append(song2)
service.create_playlist(playlist1)

service.search_song(song1)


