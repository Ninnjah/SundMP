from typing import List

import pygame
from pygame import mixer, error
from pygame.mixer import Sound


class Player:
    channel = mixer.music
    sound: Sound

    def __init__(self):
        mixer.init(44100)
        pygame.init()

    def is_playing(self) -> bool:
        return self.channel.get_busy()

    def get_pos(self) -> int:
        return int(self.channel.get_pos()/10//60)

    def get_length(self) -> int:
        return int(self.sound.get_length()*100//60)

    def load_sound(self, filename: str) -> None:
        try:
            self.sound = mixer.Sound(filename)
            self.channel.load(filename)
        except error:
            raise ValueError("This format doesn't support!")
        else:
            return

    def play_sound(self) -> None:
        self.channel.unload()
        self.channel.play()

    def stop_sound(self) -> None:
        self.channel.stop()

    def pause_sound(self) -> None:
        self.channel.pause()

    def resume_sound(self) -> None:
        self.channel.unpause()
