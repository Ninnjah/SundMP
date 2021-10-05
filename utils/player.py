from pathlib import Path
from typing import List

import pygame
from pygame import mixer, event, error


class Player:
    playlist: List[str]
    player = mixer.music

    def __init__(self):
        self.playlist = list()
        mixer.init(44100)
        pygame.init()

    def play_sound(self, filename: str) -> None:
        self.player.unload()
        try:
            self.player.load(filename)
        except error:
            raise ValueError("This format doesn't support!")
        else:
            self.player.play()

    def stop_sound(self):
        self.player.stop()

    def pause_sound(self):
        self.player.pause()

    def resume_sound(self):
        self.player.unpause()
