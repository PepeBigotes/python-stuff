#!/usr/bin/env python3
#Created by PepeBigotes

import os
from keyboard import *

RECORD_HOTKEY = 'ctrl+alt+q'
PLAY_HOTKEY = 'ctrl+alt+p'
STOP_HOTKEY = 'ctrl+alt+space'


os.system('cls' if os.name=='nt' else 'clear')
print( "┬┌─┌─┐┬ ┬┌┐ ┌─┐┌─┐┬─┐┌┬┐   ┌┬┐┌─┐┌─┐┬─┐┌─┐")
print( "├┴┐├┤ └┬┘├┴┐│ │├─┤├┬┘ ││───│││├─┤│  ├┬┘│ │")
print( "┴ ┴└─┘ ┴ └─┘└─┘┴ ┴┴└──┴┘   ┴ ┴┴ ┴└─┘┴└─└─┘\n")

print(f"  'Record' hotkey: {RECORD_HOTKEY.upper()}")
print(f"  'Play' hotkey: {PLAY_HOTKEY.upper()}")
print(f"  'Stop' hotkey: {STOP_HOTKEY.upper()}")
print( "------------------------------------------")

running = True

def stop_all(): # Stops the script, but as it runs on a separate thread it does not fully exit
    global running
    running = False
    unhook_all_hotkeys()
    unhook_all()
    print("keyboard-macro Stopped,\nPress CTRL+C to exit the script")
    exit()

def exit_all(): # Stops and exits the scripts fully
    global running
    running = False
    unhook_all_hotkeys()
    unhook_all()
    print("Exiting keyboard-macro...\n")
    exit()

add_hotkey(STOP_HOTKEY, stop_all)

try:
    print(f"Press {RECORD_HOTKEY.upper()} to begin recording")
    print(f"Then press {RECORD_HOTKEY.upper()} again to stop recording")
    if not running: exit_all()
    wait(RECORD_HOTKEY)
    if not running: exit_all()
    print(f"Recording macro...")
    macro = record(until=RECORD_HOTKEY)
    if not running: exit_all()
    print(f"Macro recorded! You can now play by pressing {PLAY_HOTKEY.upper()}")
    print(f"When you are done, stop the script by pressing {STOP_HOTKEY.upper()}")
    while True:
        wait(PLAY_HOTKEY)
        if not running: exit_all()
        print("Playing macro...")
        play(macro)
        if not running: exit_all()
        print("Macro finished playing!")
        print(f"You can play it again by pressing {PLAY_HOTKEY.upper()}")
        print(f"Or stop the script by pressing {STOP_HOTKEY.upper()}")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    exit_all()