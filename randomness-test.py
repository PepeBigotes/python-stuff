#!/usr/bin/env python3

var0 = 0
var1 = 0

import random

for i in range(0,1000000):
    x = random.randint(0, 1)
    if x:
        var0 += 1
    else:
        var1 += 1
        
print(var0)
print(var1)