import os
import threading

import player

def close_app(song_q: list):
    # print("After 5 secs")

    player.save_queue(song_q)

    os._exit(0)

def set_timer(t: float, song_q: list):
    timer = threading.Timer(3.0, function=close_app, args=(song_q,))
    timer.start()
