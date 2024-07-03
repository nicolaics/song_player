from type import *

import songs
import sleep_timer
import player
import playlist

import pickle

global song_q
song_q = []

def load_queue():
    q_path = "./playlists/QUEUE.bin"
    global song_q

    try:
        fh = open(q_path, 'rb')
        song_q = pickle.load(fh)
        fh.close()
    except:
        return

def select_one_song(songs_list: list[Song]):
    global song_q

    song_no = int(input("Which song do you want to select (number only)? "))
    song_no -= 1

    print()
    print("Selected song:")
    print("Title:", songs_list[song_no].title)
    print("Artist:", songs_list[song_no].artist)
    print("Album:", songs_list[song_no].album)
    print("Duration:", songs_list[song_no].duration)
    print("Type:", songs_list[song_no].file_type)
            
    print("\nWhat do you want to do?")
    print("1. Play Song")
    print("2. Add to Queue")
    print("3. Add to Play Next")
    print("4. Play from Queue")
    print("5. Add to Playlist")
    print("6. Previous")
    print("0. Exit")

    song_select_choose = int(input("Your choice (number only): "))

    if song_select_choose == 1:
        player.play_single_song(songs_list[song_no])
    elif song_select_choose == 2:
        song_q = player.add_to_queue(songs_list[song_no], song_q)
    elif song_select_choose == 3:
        song_q = player.play_next(songs_list[song_no], song_q)
    elif song_select_choose == 4:
        player.play_from_queue(song_q)
    elif song_select_choose == 5:
        playlists_list = playlist.view_all_playlists()
        
        p_name = input("Playlist Name (Enter number/Playlist Name): ")
        p_name = playlist.find_playlist_name(playlists_list, p_name)
        
        playlist.add_to_playlist(p_name, songs_list[song_no])

        print(f"Successfully added to {p_name}!")
    elif song_select_choose == 6:
        song_selection(songs_list)
    elif song_select_choose == 0:
        sleep_timer.close_app(song_q)

def song_selection(songs_list: list[Song]):
    print()
    songs.show_all_songs(songs_list)

    print()
    print("What do you want to do?")
    print("1. Select Song")
    print("2. Sort Song by Title Ascending")
    print("3. Sort Song by Title Descending")
    print("4. Sort Song by Artist Ascending")
    print("5. Sort Song by Artist Descending")
    print("6. Sort Song by Album Ascending")
    print("7. Sort Song by Album Descending")
    print("8. Sort Song by File Type")
    print("9. Previous")
    print("0. Exit")

    choose = int(input("Your selection (number only): "))

    if choose == 1:
        select_one_song(songs_list)
    elif choose == 2:
        songs_list = songs.sort_songs(songs_list, "title", 'asc')
    elif choose == 3:
        songs_list = songs.sort_songs(songs_list, "title", 'desc')
    elif choose == 4:
        songs_list = songs.sort_songs(songs_list, "artist", 'asc')
    elif choose == 5:
        songs_list = songs.sort_songs(songs_list, "artist", 'desc')
    elif choose == 6:
        songs_list = songs.sort_songs(songs_list, "album", 'asc')
    elif choose == 7:
        songs_list = songs.sort_songs(songs_list, "album", 'desc')
    elif choose == 8:
        songs_list = songs.sort_songs(songs_list, "type", 'asc')
    elif choose == 9:
        print()
        return
    elif choose == 0:
        sleep_timer.close_app(song_q)
        return

    song_selection(songs_list)

def main():
    global song_q
    load_queue()

    while True:
        songs_list = songs.get_all_songs()

        print()
        print("1. Show All Songs")
        print("2. Search for a Song")
        print("3. View Queue")
        print("4. Play from Queue")
        print("5. View Playlist")
        print("6. Set Sleep Timer")
        print("0. Exit")

        choose = int(input("Selection (number only): ").strip())

        if choose == 2:
            print()
            print("Search Parameters:")
            print("1. Title")
            print("2. Artist")
            print("3. Album")

            search_params = int(input("Search by (number only): ").strip())
            search_val = input("Search: ")

            songs_list = songs.search_songs(songs_list, search_val, search_params)
        elif choose == 3:
            playlist.view_songs_in_a_playlist("QUEUE")
            continue
        elif choose == 4:
            player.play_from_queue(song_q)
            continue
        elif choose == 5:
            playlists_list = playlist.view_all_playlists()

            print()
            print("What do you want to do?")
            print("1. View Songs in a Playlist")
            print("2. Delete a Playlist")
            print("0. Exit")

            playlist_choose = int(input("Your Choice (number only): "))

            if playlist_choose != 0:
                playlist_no = int(input("Input Playlist No.: "))
                playlist_no -= 1

                if playlist_choose == 1:
                    playlist.view_songs_in_a_playlist(playlists_list[playlist_no])
                elif playlist_choose == 2:
                    playlist.delete_playlist(playlists_list[playlist_no])
            else:
                sleep_timer.close_app(song_q)
        elif choose == 6:
            timer = input("Enter the time (hh:mm:ss): " )
            sleep_timer.set_timer(timer, song_q)
        elif choose == 0:
            sleep_timer.close_app(song_q)


        song_selection(songs_list)

if __name__ == "__main__":
    main()
