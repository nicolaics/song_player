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

def view_all_playlists():
    f_path = './playlists'
    
    playlists_list = os.listdir(f_path)

    # TODO: print the playlists
    print()
    

def view_songs_in_a_playlist(p_name: str):
    p_fname = FOLDER_PATH + p_name + ".bin"

    fh = open(p_fname, 'rb')
    
    songs_list = []
        
    while True:
        try:
            songs_list.append(pickle.load(fh))
        except EOFError:
            break    
        
    fh.close()

    print(f"PLAYLIST: {p_name}")
    show_all_songs(songs_list)
