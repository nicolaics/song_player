from type import *
from songs import sort_songs, show_all_songs

import os
import pickle

FOLDER_PATH = "./playlists/"

def create_playlist(p_name: str, songs_list: list[Song]):
    fh = open(FOLDER_PATH + p_name + '.bin', 'wb')

    for s in songs_list:
        pickle.dump(s, fh)
    
    fh.close

def add_to_playlist(p_name: str, song: Song):
    playlist_fname = FOLDER_PATH + p_name + ".bin"

    if os.path.exists(playlist_fname) == False:
        create_playlist(p_name, [song])
    else:
        fh = open(playlist_fname, '+rb')
        # songs_list = []
        
        # while True:
        #     try:
        #         songs_list.append(pickle.load(fh))
        #     except EOFError:
        #         break

        # for s in songs_list:
        #     if s.title == song.title:
        #         if s.artist == song.artist:
        #             if s.album == song.album:
        #                 dup = int(input)

        # songs_list.append(song)

        pickle.dump(song, fh)
        
        fh.close()

def sort_playlist(p_name: str, sort_params: str, sort_order: str) -> list[Song]:
    p_fname = FOLDER_PATH + p_name + ".bin"

    fh = open(p_fname, 'rb')
    
    songs_list = []
        
    while True:
        try:
            songs_list.append(pickle.load(fh))
        except EOFError:
            break    
        
    fh.close()

    songs_list = sort_songs(songs_list, sort_params, sort_order)

    create_playlist(p_name, songs_list)
    
    return songs_list

def view_all_playlists() -> list[str]:
    f_path = './playlists'
    
    playlists_list_rough = os.listdir(f_path)

    header_len = {
        "no": 7,
        "p_name": 32,
    }

    print()
    print("+" + ("-" * header_len['no']), end='')
    print("+" + ("-" * header_len['p_name']), end='')
    print("+")
    print("| {0:5s} | {1:30s} |".format("No.", "Playlist Name"))
    print("+" + ("-" * header_len['no']), end='')
    print("+" + ("-" * header_len['p_name']), end='')
    print("+")

    playlists_list = []

    for i in playlists_list_rough:
        if (i.endswith(".md")) or (i == "QUEUE.bin"):
            continue
            
        playlists_list.append(i.split('.')[0])

    count = 1 

    for i in playlists_list:
        c = str(count) + "."
        
        i = i.split(".")[0]

        print(f"| {c:5s} | {i:30s} |")
        count += 1

    print("+" + ("-" * header_len['no']), end='')
    print("+" + ("-" * header_len['p_name']), end='')
    print("+")

    return playlists_list   

def view_songs_in_a_playlist(p_name: str):
    p_fname = FOLDER_PATH + p_name + ".bin"

    try:
        fh = open(p_fname, 'rb')
    except:
        print("Playlist do not exist!")
        return
    
    songs_list = []
        
    while True:
        try:
            songs_list.append(pickle.load(fh))
        except EOFError:
            break    
        
    fh.close()

    print()
    print(f"Playlist: {p_name.split('.')[0]}")

    if p_name == 'QUEUE':
        temp = []
        for i in songs_list[0]:
            temp.append(i.song)

        songs_list = temp
        
    show_all_songs(songs_list)

def find_playlist_name(playlists_list: list, p_name: str) -> str:
    p_no = None

    try:
        p_no = int(p_name)
        p_no -= 1
    except:
        pass

    if p_no is not None:
        for i in range(len(playlists_list)):
            if i == p_no:
                p_name = playlists_list[i]
                break

    return p_name.split('.')[0]

def delete_playlist(p_name: str):
    p_name = FOLDER_PATH + p_name + '.bin'

    os.remove(p_name)
