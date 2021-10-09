import sys
import time
from os import listdir
from pathlib import Path
from typing import List

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.Qt import QTimer

from ui import player_ui
from utils.player import Player


class PlayerUI(QMainWindow, player_ui.Ui_MainWindow):
    playlist: List[str]
    display_timer: QTimer

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.playlist = list()
        self.display_timer = QTimer(self)
        self.display_timer.setInterval(10)
        self.display_timer.timeout.connect(self.display_info)

        self.playbar_slider.setDisabled(True)

        self.button_play.clicked.connect(self.play_pause_sound)
        self.button_next.clicked.connect(self.next_sound)
        self.button_prev.clicked.connect(self.prev_sound)
        self.action_open_folder.triggered.connect(self.open_folder)

    def open_folder(self) -> None:
        """Opens folder with music"""

        dir_name: str = QFileDialog.getExistingDirectory(self, 'Select directory')

        self.playlist = [
            Path(dir_name).joinpath(x).absolute().as_posix()
            for x in listdir(Path(dir_name).absolute()) if x.endswith((".mp3", ".wav", ".ogg"))
        ]

    def play_pause_sound(self):
        """Pause or play sound"""
        if player.is_playing():
            player.pause_sound()
        else:
            try:
                player.sound
            except AttributeError:
                self.play_playlist()
            else:
                player.resume_sound()

    def play_playlist(self):
        if not self.playlist:
            return

        for song in self.playlist:
            try:
                self.play_sound(song)
            except ValueError:
                continue

    def display_info(self):
        if not player.is_playing():
            self.display_timer.stop()

        current_length: int = player.get_length()
        current_pos: int = player.get_pos()

        self.playbar_slider.setMaximum(current_length)
        self.playbar_slider.setSliderPosition(current_pos)
        self.playbar_length.setText(f"{current_length // 60:02d}:{current_length % 60:02d}")
        self.playbar_current.setText(f"{current_pos // 60:02d}:{current_pos % 60:02d}")

    def play_sound(self, filename: str) -> None:
        player.load_sound(filename)

        self.title_label.setText(filename.split("/")[-1])
        self.display_timer.start()

        player.play_sound()

    def next_sound(self):
        """Plays next sound"""

    def prev_sound(self):
        """Plays previous sound"""
        pass

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication([])
    player_window = PlayerUI()
    player = Player()

    player_window.show()

    sys.exit(app.exec())
