import os

from utils.player import Player


if __name__ == "__main__":
    player = Player()

    for song in os.listdir("test"):
        player.play_sound(os.path.join("test", song))
