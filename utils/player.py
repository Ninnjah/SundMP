from pathlib import Path
from typing import List

import numpy as np
from numpy.typing import NDArray
from pydub import AudioSegment
import sounddevice as sd


class Loader:
    @staticmethod
    def audio_from_file(filename: Path):
        suffix: str = filename.suffix.replace(".", "")

        if suffix not in ["mp3", "wav"]:
            raise ValueError("File doesn't support. This moment player supports only .mp3 .wav files")

        audio: AudioSegment = AudioSegment.from_file(
            filename.absolute(),
            format=suffix
        )
        audio_bytes: NDArray = np.array(audio.get_array_of_samples())

        return audio_bytes, audio.frame_rate


class Player:
    playlist: List[str]

    def __init__(self):
        self.playlist = list()

    def play_sound(self, filename: Path) -> None:
        try:
            data, fs = Loader.audio_from_file(filename)
        except ValueError:
            return
        else:
            sd.play(data, fs)
            sd.wait()

