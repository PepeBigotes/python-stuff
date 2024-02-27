#!/usr/bin/env python3
#Created by PepeBigotes

import time
print("Counting Game (Powers of 2)\n")

def calc(i):
    # You can define your own counting game here
    # I did powers of 2, but you can do fibonacci, multiplication tables, or whatever idk
    return 2 ** i

start = time.time()

for i in range(100):
    try:
        try: user_input = eval(input(f"{i}> "))
        except SyntaxError: raise KeyboardInterrupt()
        result = calc(i)
        if not user_input == result: raise KeyboardInterrupt()
    except KeyboardInterrupt:
        end = time.time()
        seconds = int(end - start)
        print(f"\nGame Over! The correct answer was {result}\n Score: {i}\n Time: {seconds} seconds\n Speed: {int(i/seconds * 1000)}")
        exit()