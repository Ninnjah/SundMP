import sys
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication

from ui import player_ui
from utils.player import Player


class PlayerUI(QtWidgets.QMainWindow, player_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication([])
    player_window = PlayerUI()
    player = Player()

    player_window.show()

    sys.exit(app.exec())
    # for song in os.listdir("test"):
    #     try:
    #         player.play_sound(os.path.join("test", song))
    #         while player.is_playing():
    #             print(f"\r{player.get_pos()}/{player.get_length()} sec.", end="")
    #             sleep(0.01)
    #             pass
    #     except ValueError:
    #         pass
