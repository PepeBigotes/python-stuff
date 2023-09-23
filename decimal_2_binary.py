#!/usr/bin/env python3
# Created by PepeBigotes

def get_integer(prompt):
    try:
        value = int(input(prompt))
        return int(value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit()

bits = 40
nums = [2 ** i for i in range(bits - 1, -1, -1)]
#print(nums)


while True:
    try:
        decimal = get_integer("Enter your decimal number or press CTRL+C to stop\n >> ")
    except KeyboardInterrupt:
        print("CTRL+C, Stopping...")
        exit()
    result = []
    
    if decimal == 0:
        print(0)
        print()
        continue
    
    for num in nums:
        if decimal >= num:
            result.append(1)
            decimal -= num
        else:
            result.append(0)

    while result == 0 or result[0] == 0:
        result.pop(0)
    
    if len(result) <= 4:
        for i in result: print(i, end="")
        print()
    
    else:
        div4 = len(result) / 4
        while div4 > 0: div4 -= 1.0
        div4 = -div4
        div4 *= 4
        div4 = int(0) if div4 == 4 else int(div4)
        
        result_4 = list()
        cache = list()
        if div4 > 0:
            for i in range(div4): cache.append(0)
                
        while len(result) > 0:
            while len(cache) != 4:
                cache.append(result[0])
                result.pop(0)
            result_4.append(cache)
            cache = []
        for i in result_4:
            for x in i: print(x, end="")
            print(" ", end="")
        print()
