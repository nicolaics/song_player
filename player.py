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
    
    print("1. Next")
    print("2. Previous")
    print("3. Stop")
    choose = int(input("Your choice (number only): "))
    
    play_audio.terminate()

    if choose == 2:
        return 'prev'
    elif choose == 3:
        return 'stop'
    
    return None
    
def play_from_queue(song_q: list[SongQueue]):
    if len(song_q) == 0:
        print("Queue is empty!")
        return
    
    i = 0

    while True:
        song_q[i].is_playing = True
        cue = play_single_song(song_q[i].song)
        song_q[i].is_playing = False

        if cue == 'prev':
            i -= 2
        elif cue == 'stop':
            song_q[i].is_playing = True
            break

        i += 1

        if i == len(song_q):
            break

def add_to_queue(song: Song, song_queue: list) -> list:
    song_queue.append(SongQueue(song))
    return song_queue

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