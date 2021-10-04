from pathlib import Path
import time
from typing import Type

import pybass3 as bass
from pybass3 import Song
from pybass3.playlist import Playlist


class Player:
    def __init__(self):
        self.song: Type[Song] = Song
        self.playlist: Playlist = Playlist()

    def playlist_from_dir(self, dir_path: str):
        dir_path: Path = Path(dir_path)

        self.playlist.add_directory(dir_path, recurse=True)

        for i in self.playlist.items():
            print(i)
        self.playlist.play()
        play_indefinitely = True
        while play_indefinitely:
            try:
                print(self.playlist.current.file_path.name, self.playlist.current.position, self.playlist.current.duration)
                if self.playlist.current.position == self.playlist.current.duration:
                    print("next")
                    self.playlist.next()
                self.playlist.tick()
                time.sleep(1)
            except KeyboardInterrupt:
                self.playlist.free()
                play_indefinitely = False

    def play_sound(self, file_path: str) -> None:
        file_path: Path = Path(file_path)

        self.playlist.clear()
        self.playlist: Playlist = Playlist()
        self.playlist.add_song(file_path, add2queue=True)

        self.playlist.play()
        while True:
            print(self.playlist.current.file_path.name, self.playlist.current.position, self.playlist.current.duration)
            if self.playlist.current.position >= self.playlist.current.duration:
                break

            self.playlist.tick()

    def stop_sound(self) -> None:
        self.playlist.stop()

