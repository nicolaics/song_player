from type import *

import pickle
import os
import multiprocessing
from playsound import playsound

P_PATH = "./playlists/QUEUE.bin"
S_PATH = "./songs/"

'''
    function to accept an input when a song is playing
'''
def accept_input(choice: multiprocessing.Queue): 
    print("1. Next")
    print("2. Previous")
    print("3. Stop")
    print("Your choice (number only): ")
    
    stdin = open(0)
    choose = int(stdin.readline())

    if choose == 2:
        choice.put('prev')
    elif choose == 3:
        choice.put('stop')
    else:
        choice.put(None)

'''
    function to play a single song
'''
def play_single_song(song: Song):
    songs_list = os.listdir(S_PATH)
    song_path = ""
    s_title = ""

    choice = multiprocessing.Queue()

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
    accept_choice = multiprocessing.Process(target=accept_input, args=(choice,))

    play_audio.start()
    accept_choice.start()
    
    while play_audio.is_alive():
        # if the audio has finished playing
        if play_audio.is_alive() is False:
            # stop accepting user input
            accept_choice.kill()
        
        # if the user has input something
        if accept_choice.is_alive() is False:
            # stop playing
            play_audio.terminate()
            break
    
    accept_choice.join()
    play_audio.join()
    
    return choice.get()

'''
    function to play from a queue or playlist
'''
def play_from_queue(song_q: list[SongQueue], p_name: str):
    if len(song_q) == 0:
        print("Queue/Playlist is empty!")
        return
    
    print()
    print(f"Playing from {p_name}")

    idx = 0

    for i in range(len(song_q)):
        if song_q[i].is_playing == True:
            idx = i
            break
    
    # keep playing from the queue
    while True:
        song_q[idx].is_playing = True
        cue = play_single_song(song_q[idx].song)
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

'''
    function to add songs to queue
'''
def add_to_queue(song: Song, song_q: list) -> list:
    if len(song_q) == 0:
        song_q.append(SongQueue(song, True))    
    else:
        song_q.append(SongQueue(song))

    return song_q

'''
    function to add songs to the next play in the queue
'''
def play_next(song: Song, song_q: list) -> list:
    new_song_queue = song_q

    for i in range(len(song_q)):
        if song_q[i][1] == True:
            break

    new_song_queue.insert((i + 1), (song, False))

    return new_song_queue

'''
    function to save the queue to the file
'''
def save_queue(song_q: list):
    fh = open(P_PATH, 'wb')

    pickle.dump(song_q, fh)

    fh.close()

'''
    function to empty or clear the queue
'''
def clear_queue() -> list:
    if os.path.exists(P_PATH):
        os.remove(P_PATH)
    
    save_queue([])

    print("Queue is emptied!")
    
    return []

if __name__ == "__main__":
    song_q = []

    song_q.append(SongQueue(Song("I Stan U", "IU", "The Winning", None, None), is_playing=True))
    song_q.append(SongQueue(Song("Shopper", "IU", "The Winning", None, None), is_playing=False))

    play_from_queue(song_q, "QUEUE")