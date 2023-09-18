#!/usr/bin/env python3

import random
import time

myvar = ["a", "b", "c", "d", "e", "f", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

while True:
    random.shuffle(myvar)
    for x in myvar:
        print(x, end="")
    print()
    time.sleep(0.1)