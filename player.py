from pygame import mixier
from mutagen.mp3 import MP3
import time

def mutagen_length(path) -> float:
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None

def play(file_path: str) -> None:
    length = mutagen_length(file_path)
    mixier.init()
    mixier.music.load(file_path)
    mixier.music.play()
    time.sleep(int(length) + 1)
    mixier.music.stop()
    return