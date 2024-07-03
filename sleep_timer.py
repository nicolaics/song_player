import os
import threading

import player

def close_app(song_q: list):
    print("\n\nCLOSING APP!")

    player.save_queue(song_q)
    os._exit(0)

def set_timer(t: str, song_q: list):
    parse = t.split(":")
    hrs = float(parse[0])
    mins = float(parse[1])
    secs = float(parse[2])

    t = secs
    t += (mins * 60)
    t += (hrs * 3600)

    timer = threading.Timer(t, function=close_app, args=(song_q,))
    timer.start()

    print("\nTimer has been set for: {0:02.0f}h {1:02.0f}m {2:02.0f}s!".format(hrs, mins, secs))
