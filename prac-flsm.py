#!/usr/bin/env python3
#Created by PepeBigotes

def split_parts(total, nparts):
    if total % 2 != 0: print("total must devide by 2"); exit()
    if nparts % 2 != 0: print("nparts must devide by 2"); exit()
    lastnum = 0
    part = int(total/nparts)
    print(f"part={part}")
    while lastnum != total:
        x = lastnum
        lastnum += part
        y = lastnum -1
        print(f"{x} - ", end="")
        try: ans = eval(input())
        except KeyboardInterrupt: exit()
        except Exception as error: print(error); ans = -1
        if ans != y: print(f"WRONG! its {y}")
        

total = input("total [256]: ")
total = eval(total) if total != "" else 256
nparts = input("parts number [8]: ")
nparts = eval(nparts) if nparts != "" else 8

split_parts(total, nparts)