#!/usr/bin/env python3
#Created by PepeBigotes

class data():
    def __init__(self, num, base):
        self.num = num
        self.base = base.upper()
        self.bytes = 0
                
        if self.base == "BYTES" or self.base == "BYTE" or self.base == "B": self.bytes = self.num
        if self.base == "BITS" or self.base == "BIT": self.bytes = self.num / 8
        
        if self.base == "KIB": self.bytes = self.num * 1024**1
        if self.base == "MIB": self.bytes = self.num * 1024**2
        if self.base == "GIB": self.bytes = self.num * 1024**3
        if self.base == "TIB": self.bytes = self.num * 1024**4
        if self.base == "PIB": self.bytes = self.num * 1024**5
        
        if self.base == "KB": self.bytes = self.num * 1000**1
        if self.base == "MB": self.bytes = self.num * 1000**2
        if self.base == "GB": self.bytes = self.num * 1000**3
        if self.base == "TB": self.bytes = self.num * 1000**4
        if self.base == "PB": self.bytes = self.num * 1000**5
        #if base is any other value, self.bytes will still be 0,
        #and any other base will also be 0
        
        self.bits = self.bytes * 8
        self.kib = self.bytes / 1024**1
        self.mib = self.bytes / 1024**2
        self.gib = self.bytes / 1024**3
        self.tib = self.bytes / 1024**4
        self.pib = self.bytes / 1024**5
        self.kb = self.bytes / 1000**1
        self.mb = self.bytes / 1000**2
        self.gb = self.bytes / 1000**3
        self.tb = self.bytes / 1000**4
        self.pb = self.bytes / 1000**5
        

"""
USE EXAMPLES:

#Single line convertions:
print(data(1, 'tb').gib) #Prints the actual GBs of "1 tb" disks
print(data(250, 'gb').gib) #Prints the actual GBs of "250 gb" disks

#Interactive Prompt:
while True:
    start_var = input("Type the data in this format ('1 GIB', '25 kb', '300 Mb',...):\n> ")
    target_base = input("Type the base you want to convert it to ('MB', 'Gb', 'KiB', ...):\n> ")
    pars = start_var.split(' ')
    predata = f"data({pars[0]}, '{pars[1]}').{target_base}"
    print(eval(predata))
    print()
    
#Import to use in your own scripts:
execfile("/path/to/file/byte-converter-2.py")
"""