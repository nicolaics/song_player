import os
from mutagen.wave import WAVE
from mutagen.mp3 import MP3
  
from type import *

'''
    Songs must be in the
        "[Title] - [Artist] - [Album]"
    format.

    If the Artist or Album is unknown, just write Unknown
'''

'''
    function to get the audio duration from the file
'''
def audio_duration(length): 
    length %= 3600
    mins = length // 60  # calculate in minutes 
    length %= 60
    seconds = length  # calculate in seconds 
  
    return mins, seconds  # returns the duration

'''
    function to get all of the songs inside the songs folder
'''
def get_all_songs() -> list[Song]:
    f_path = './songs'
    
    songs_list_rough = os.listdir(f_path)

    songs_list = []    

    for s in songs_list_rough:
        if s.endswith(".md"):
            continue

        data = s.split('] - [')

        data[0] = data[0].removeprefix('[')
        data[2] = data[2].split('].')

        if data[2][1] == 'wav':
            audio = WAVE("./songs/" + s)
        elif data[2][1] == 'mp3':
            audio = MP3("./songs/" + s)
        else:
            audio = None
            duration = '00:00'

        audio_info = audio.info 
        length = int(audio_info.length) 
        mins, seconds = audio_duration(length) 

        duration = f"{mins:02d}:{seconds:02d}"

        songs_list.append(Song(data[0], data[1], data[2][0], duration, data[2][1]))

    return songs_list

'''
    function to only print the border for displaying the songs information
'''
def print_border():
    header_len = {
        "no": 7,
        "title": 32,
        "artist": 22,
        "album": 22,
        "duration": 12,
        "type": 7
    }

    print("+" + ("-" * header_len['no']), end='')
    print("+" + ("-" * header_len['title']), end='')
    print("+" + ("-" * header_len['artist']), end='')
    print("+" + ("-" * header_len['album']), end='') 
    print("+" + ("-" * header_len['duration']), end='')
    print("+" + ("-" * header_len['type']), end='')
    print("+")

'''
    function to show all of the songs’ information in the form of table
'''
def print_data(no: str, title: str, artist: str,
               album: str, dur: str, type: str):
    
    if len(title) > 30:
        title = title[:27]
    
    if len(artist) > 20:
        artist = artist[:17]

    if len(album) > 20:
        album = album[:17]

    print(f"| {no:5s} | {title:30s} | {artist:20s} | {album:20s} | {dur:10s} | {type:5s} |")

'''
    the main function that shows all of the songs in the screen,
    that incorporates print_data() and print_border() functions
'''
def show_all_songs(songs_list: list[Song]):
    print_border()
    print_data("No.", "Title", "Artist", "Album", "Duration", "Type")
    print_border()
    
    s_count = 1

    for song in songs_list:
        print_data((str(s_count) + "."), song.title, song.artist, song.album, song.duration, song.file_type)
        s_count += 1

    print_border()

'''
    function to search songs inside the folder, based on title, artist, or album
'''
def search_songs(songs_list: list[Song], search_val: str, search_params: str) -> list[Song]:
    res = []

    if search_params == 'title':
        for s in songs_list:
            if s.title.lower() == search_val.lower():
                res.append(s)

    elif search_params == 'artist':
        for s in songs_list:
            if s.artist.lower() == search_val.lower():
                res.append(s)

    elif search_params == 'album':
        for s in songs_list:
            if s.album.lower() == search_val.lower():
                res.append(s)

    return res

'''
    function to sort the displayed songs based on the title, artist, album,
    or file type, in the order of ascending or descending
'''
def sort_songs(songs_list: list[Song], sort_params: str, order: str):
    swapped = True

    if order == 'asc':
        while swapped:
            swapped = False

            for i in range(1, len(songs_list)):
                if sort_params == 'title':
                    if songs_list[i - 1].title.lower() > songs_list[i].title.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
                elif sort_params == 'artist':
                    if songs_list[i - 1].artist.lower() > songs_list[i].artist.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
                elif sort_params == 'album':
                    if songs_list[i - 1].album.lower() > songs_list[i].album.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
                elif sort_params == 'type':
                    if songs_list[i - 1].file_type.lower() > songs_list[i].file_type.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
    else:
        while swapped:
            swapped = False

            for i in range(1, len(songs_list)):
                if sort_params == 'title':
                    if songs_list[i - 1].title.lower() < songs_list[i].title.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
                elif sort_params == 'artist':
                    if songs_list[i - 1].artist.lower() < songs_list[i].artist.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
                elif sort_params == 'album':
                    if songs_list[i - 1].album.lower() < songs_list[i].album.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True
                elif sort_params == 'type':
                    if songs_list[i - 1].file_type.lower() < songs_list[i].file_type.lower():
                        temp = songs_list[i]
                        songs_list[i] = songs_list[i - 1]
                        songs_list[i - 1] = temp
                        swapped = True


    return songs_list

if __name__ == '__main__':
    show_all_songs(get_all_songs())