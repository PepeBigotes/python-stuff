#!/usr/bin/env python3
#Created by PepeBigotes

def try_input(msg) -> str:
    try: x = input(msg)
    except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()
    return x

import os

try:
	try: import curses
	except ImportError:
		print("[!] Module 'curses' is not installed")
		try_input("  Press ENTER to install it (or CTRL+C to exit)")
		os.system('pip3 install windows-curses')
		try: import curses
		except ImportError: print("\n[!] Curses couldn't be installed"); exit(1)
		try_input("\n  Curses installed, press ENTER to continue")
except KeyboardInterrupt: print("\nKeyboardInterrupt"); exit()

import curses
from curses import wrapper
from time import sleep



def do_exit(code = 0):
    # Escape getch() idk how
    curses.endwin()
    exit(code)


def main(stdscr):
    curses.cbreak()
    curses.noecho()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GRN_BLK = curses.color_pair(1)
    TERM = curses.termname().decode()

    while True:
        height,width = stdscr.getmaxyx()
        lines_cols = f"{height}x{width}"
        char = curses.keyname(stdscr.getch()).decode()
        if char == "^X": do_exit()
        stdscr.clear()

        stdscr.addstr(0,0, f"{TERM} {lines_cols}")
        stdscr.addstr(2,0, char)
        stdscr.addstr(11,10, "hello world!", curses.A_UNDERLINE)
        stdscr.addstr(12,10, "hello world!", GRN_BLK)
        stdscr.refresh()


try: wrapper(main)
except KeyboardInterrupt: do_exit()