from pygame import mixer
from mutagen.mp3 import MP3
import time


def mutagen_length(path) -> float:
    audio = MP3(path)
    if audio.info is not None:
        length = audio.info.length
    else:
        length = 0.0
    return length

def play(file_path: str) -> None:
    length = mutagen_length(file_path)
    try:
        mixer.init()
        mixer.music.load(file_path)
        mixer.music.play()
        time.sleep(int(length) + 1)
        mixer.music.stop()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return
