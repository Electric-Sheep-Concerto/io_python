from pygame import mixer, error as pygame_error
from mutagen import mp3, MutagenError
import time


def mutagen_length(path) -> float:
    try:
        audio = mp3.MP3(path)
    except MutagenError:
        print(f"File not found: {path}")
        return 0.0
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
    except pygame_error:
        print(f"File not found: {file_path}")
    return
