# the class to store a Song file or type
class Song:
    def __init__(self, title, artist, album, duration, file_type) -> None:
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.file_type = file_type

# the class for the queue
class SongQueue:
    def __init__(self, song: Song, is_playing=False) -> None:
        self.song = song
        self.is_playing = is_playing
    