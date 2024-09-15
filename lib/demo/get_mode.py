import os

def get_mode():
    return os.getenv("MODE", "demo")
