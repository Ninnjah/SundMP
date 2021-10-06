import os
from time import sleep

from utils.player import Player


if __name__ == "__main__":
    player = Player()

    for song in os.listdir("test"):
        try:
            player.play_sound(os.path.join("test", song))
            while player.is_playing():
                print(f"\r{player.get_pos()}/{player.get_length()} sec.", end="")
                sleep(0.01)
                pass
        except ValueError:
            pass
