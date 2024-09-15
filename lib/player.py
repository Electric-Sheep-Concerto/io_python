from pygame import mixer
from mutagen.mp3 import MP3
import time


def mutagen_length(path) -> float:
    try:
        audio = MP3(path)
        if audio.info is not None:
            length = audio.info.length
        else:
            length = 0.0
        return length
    finally:
        return 0.0


def play(file_path: str) -> None:
    length = mutagen_length(file_path)
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    time.sleep(int(length) + 1)
    mixer.music.stop()
    return
