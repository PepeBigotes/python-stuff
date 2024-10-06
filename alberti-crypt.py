#!/usr/bin/env python3
#Created by PepeBigotes

# This version assumes that both circles are equal
circle = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# ENCRYPT #
align = input("Lettter to align with A:\n> ").upper()
if not align in circle: print("Invalid alignment"); exit(1)
align = circle.index(align)
text = input("Text to encrypt (avoid special characters):\n> ").upper()
cipher = ""

for char in text:
    if char == " ":
        cipher += " "
        continue
    try: cipher += circle[circle.index(char) + align]
    except IndexError: cipher += circle[circle.index(char) + align - len(circle)]
    
print('\n' + cipher)


# DECRYPT #
text = ""

for char in cipher:
    if char == " ":
        text += " "
        continue
    text += circle[circle.index(char) - align]
    
print(text)
