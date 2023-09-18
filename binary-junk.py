#!/usr/bin/env python3

import random
import time

while True:
    myvar = ""
    mytime = random.random() * 0.1
    for i in range(0,120):
        myvar += str(random.randint(0,1) )

    print(myvar)
    time.sleep(mytime)