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
    s_title = ""

    for s in songs_list:
        data = s.split('] - [')

        title = data[0].removeprefix('[')

        if title.lower() == song.title.lower():
            song_path = s
            s_title = title
            break

    print()
    print(f"Now Playing: {s_title}")
    
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
    
    idx = 0

    for i in range(len(song_q)):
        if song_q[i].is_playing == True:
            idx = i
            break

    while True:
        song_q[idx].is_playing = True
        cue = play_single_song(song_q[i].song)
        song_q[idx].is_playing = False

        if cue == 'prev':
            idx -= 2

            if idx < -1:
                idx = -1
        elif cue == 'stop':
            song_q[idx].is_playing = True
            break

        idx += 1

        if idx == len(song_q):
            song_q[0].is_playing = True
            break

def add_to_queue(song: Song, song_q: list) -> list:
    if len(song_q) == 0:
        song_q.append(SongQueue(song, True))    
    else:
        song_q.append(SongQueue(song))

    return song_q

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

def clear_queue() -> list:
    if os.path.exists(P_PATH):
        os.remove(P_PATH)
    
    save_queue([])

    print("Queue is emptied!")
    
    return []

if __name__ == "__main__":
    play_single_song(Song("Keep It", "LiQWYD", "Unknown", None, None))