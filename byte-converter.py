#!/usr/bin/env python3
#Created by PepeBigotes

def ib_2_b(x, lenght):
    x = x * 1024**lenght
    x = x / (1000**lenght)
    return x   
def b_2_ib(x, lenght):
    x = x * 1000**lenght
    x = x / (1024**lenght)
    return x

def convert(num, text):
    text = text.upper()
    if text == "KB": y = b_2_ib(num, 1)
    if text == "KIB": y = ib_2_b(num, 1)
    if text == "MB": y = b_2_ib(num, 2)
    if text == "MIB": y = ib_2_b(num, 2)
    if text == "GB": y = b_2_ib(num, 3)
    if text == "GIB": y = ib_2_b(num, 3)
    if text == "TB": y = b_2_ib(num, 4)
    if text == "TIB": y = ib_2_b(num, 4)
    return y
   
while True:
    num = eval(input("Type the number: "))
    text = input("Type the base (mb, gb, kib, ...): ")
    print(f"Result: {convert(num, text)}")
    print()