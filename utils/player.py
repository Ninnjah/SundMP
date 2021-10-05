import sounddevice as sd
import soundfile as sf


class Player:

    def play_sound(self, filename: str) -> None:
        data, fs = sf.read(filename)
        print(data, fs)
        sd.play(data, fs)
        sd.wait()
