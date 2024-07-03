from type import *

import pickle
import os
import multiprocessing
from playsound import playsound

P_PATH = "./playlists/QUEUE.bin"
S_PATH = "./songs/"

def play_single_song(song: Song):
    songs_list = os.listdir(S_PATH)
    song_path = ""

    for s in songs_list:
        print(s)
        data = s.split('] - [')

        title = data[0].removeprefix('[')

        print(title)

        if title.lower() == song.title.lower():
            song_path = s
            break

    print(S_PATH + song_path)
    
    play_audio = multiprocessing.Process(target=playsound, args=((S_PATH + song_path),))
    play_audio.start()
    
    # TODO: to terminate give commands
    input("E")
    
    play_audio.terminate()
    

def play_from_queue(song_q: list[SongQueue]):
    if len(song_q) == 0:
        print("Queue is empty!")
        return
    
    for s in song_q:
        s.is_playing = True
        play_single_song(s.song)
        s.is_playing = False

def add_to_queue(song: Song, song_queue: list) -> list:
    new_song_queue = song_queue.append(SongQueue(song))
    return new_song_queue

def play_next(song: Song, song_q: list) -> list:
    new_song_queue = song_q

    for i in range(len(song_q)):
        if song_q[i][1] == True:
            break

    new_song_queue.insert((i + 1), (song, False))

    return new_song_queue

def save_queue(song_q: list):
    fh = open(P_PATH, 'wb')

    pickle.dump(song_q, fh)

    fh.close()

if __name__ == "__main__":
    play_single_song(Song("Keep It", "LiQWYD", "Unknown", None, None))