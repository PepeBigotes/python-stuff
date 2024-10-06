#!/usr/bin/env python3
#Created by PepeBigotes

square =  [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['M', 'N', 'Ñ', 'O', 'P', 'Q'], ['R', 'S', 'T', 'U', 'V', 'W'], ['X', 'Y', 'Z']]


# ENCRYPT #
text = input("Text to encrypt (avoid special characters):\n> ").upper()
cipher = ""

for char in text:
    if char == " ":
        cipher += "  "
        continue
    x = 0
    y = 0
    for i in square:
        x += 1 
        y = 0
        for j in i:
            y += 1
            if char == j:
                cipher += str(x) + str(y) + " "
                break
    
print('\n' + cipher)


# DECRYPT #
text = ""

for i, char in enumerate(cipher):
    try: nextchar = cipher[i+1]
    except IndexError: break

    if char == " " and nextchar == " ":
        text += " "
        continue
    if char == " ": continue
    try:
        x = int(char)
        y = int(nextchar)
        text += square[x-1][y-1]
    except IndexError: pass
    except ValueError: pass

for char in text:
    if char == " ": print(" ", end='')
    else: print(char + "  ", end='')
print()