#!/usr/bin/env python3
#Created by PepeBigotes

from random import getrandbits


while True:
    try:
        bools = [getrandbits(1) for i in range(8)]
        
        ints = []
        for x,i in enumerate(bools):
            if i: ints.append(2**x)
        ints = ints[::-1]
        
        result = 0
        for i in ints: result += i
        
        string = ""
        for i in ints: string += f"{i} + "
        string = string.rstrip(" +")
        
        ans = eval(input(string + " = "))
        if ans != result: print(f"{' ' * (len(string) + 3)}wrong! its {result}")

    except KeyboardInterrupt: exit()