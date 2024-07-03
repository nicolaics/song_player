from type import *

import songs
import sleep_timer
import player

# songs_list = songs.get_all_songs()
song_q = []

def song_selection(songs_list: list[Song]):
    songs.show_all_songs(songs_list)

    print()
    print("What do you want to do?")
    print("1. Select Song")
    print("2. Sort Song by Title")
    print("3. Sort Song by Artist")
    print("4. Sort Song by Album")
    print("5. Sort Song by File Type")
    print("0. Exit")

    choose = int(input("Your selection (number only): "))

    if choose == 1:
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
        print("3. Play Next")
        print("4. Previous")
        print("0. Exit")

        song_select_choose = int(input("Your choice (number only): "))

        if song_select_choose == 1:
            player.play_single_song(songs_list[song_no])
        elif song_select_choose == 2:
            song_q = player.add_to_queue(songs_list[song_no], song_q)
        elif song_select_choose == 3:
            pass
        elif song_select_choose == 4:
            song_selection(songs_list)
        elif song_select_choose == 0:
            sleep_timer.close_app(song_q)

    elif choose == 2:
        pass
    elif choose == 3:
        pass
    elif choose == 4:
        pass
    elif choose == 5:
        pass
    elif choose == 0:
        sleep_timer.close_app(song_q)

def main():
    # while True:
    # sleep_timer.set_timer(0, None)
    # playlist.add_to_playlist("Test", songs_list[0])

    while True:
        songs_list = songs.get_all_songs()

        print("1. Show All Songs")
        print("2. Search for a Song")
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
        elif choose == 0:
            sleep_timer.close_app(song_q)


        # songs.show_all_songs(songs_list)

        # print()
        # print("What do you want to do?")
        # print("1. Select Song")
        # print("2. Sort Song by Title")
        # print("3. Sort Song by Artist")
        # print("4. Sort Song by Album")
        # print("5. Sort Song by File Type")
        # print("0. Exit")

        # choose = int(input("Your selection (number only): "))

        # if choose == 1:
        #     song_no = int(input("Which song do you want to select (number only)? "))
        #     song_no -= 1
        #     print()
        #     print("Selected song:")
        #     print("Title:", songs_list[song_no].title)
        #     print("Artist:", songs_list[song_no].artist)
        #     print("Album:", songs_list[song_no].album)
        #     print("Duration:", songs_list[song_no].duration)
        #     print("Type:", songs_list[song_no].file_type)
            
        #     print("\nWhat do you want to do?")
        #     print("1. Play Song")
        #     print("2. Add to Queue")
        #     print("3. Play Next")
        #     print("4. Previous")
        #     print("0. Exit")

        #     song_select_choose = int(input("Your choice (number only): "))

        #     if song_select_choose == 1:
        #         pass
        #     elif song_select_choose == 2:
        #         pass
        #     elif song_select_choose == 3:
        #         pass
        #     elif song_select_choose == 4:
        #         pass
        #     elif song_select_choose == 0:
        #         sleep_timer.close_app(song_q)

        # elif choose == 2:
        #     pass
        # elif choose == 3:
        #     pass
        # elif choose == 4:
        #     pass
        # elif choose == 5:
        #     pass
        # elif choose == 0:
        #     sleep_timer.close_app(song_q)

        


if __name__ == "__main__":
    main()
