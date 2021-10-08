import sys
from os import listdir
from pathlib import Path
from typing import List

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

from ui import player_ui
from utils.player import Player


class PlayerUI(QtWidgets.QMainWindow, player_ui.Ui_MainWindow):
    playlist: List[str]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button_play.clicked.connect(self.play_pause_sound)
        self.button_next.clicked.connect(self.next_sound)
        self.button_prev.clicked.connect(self.prev_sound)
        self.action_open_folder.triggered.connect(self.open_folder)

    def open_folder(self) -> None:
        """Opens folder with music"""

        dir_name: str = QFileDialog.getExistingDirectory(self, 'Select directory')

        self.playlist = [x for x in listdir(Path(dir_name).absolute()) if x.endswith((".mp3", ".wav", ".ogg"))]

    def play_pause_sound(self):
        """Pause or play sound"""
        pass

    def next_sound(self):
        """Plays next sound"""
        pass

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
