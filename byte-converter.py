#!/usr/bin/env python3
#Created by PepeBigotes

class data():
    def __init__(self, num, unit):
        self.num = num
        self.unit = unit.upper()
        self.bytes = 0
                
        if self.unit == "BYTES" or self.unit == "BYTE" or self.unit == "B": self.bytes = self.num
        if self.unit == "BITS" or self.unit == "BIT": self.bytes = self.num / 8
        
        if self.unit == "KIB": self.bytes = self.num * 1024**1
        if self.unit == "MIB": self.bytes = self.num * 1024**2
        if self.unit == "GIB": self.bytes = self.num * 1024**3
        if self.unit == "TIB": self.bytes = self.num * 1024**4
        if self.unit == "PIB": self.bytes = self.num * 1024**5
        
        if self.unit == "KB": self.bytes = self.num * 1000**1
        if self.unit == "MB": self.bytes = self.num * 1000**2
        if self.unit == "GB": self.bytes = self.num * 1000**3
        if self.unit == "TB": self.bytes = self.num * 1000**4
        if self.unit == "PB": self.bytes = self.num * 1000**5
        #if unit is any other value, self.bytes will still be 0,
        #and any other unit will also be 0
        
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
    target_unit = input("Type the unit you want to convert it to ('MB', 'Gb', 'KiB', ...):\n> ")
    pars = start_var.split(' ')
    predata = f"data({pars[0]}, '{pars[1]}').{target_unit}"
    print(eval(predata))
    print()
    
#Import to use in your own scripts:
execfile("/path/to/file/byte-converter-2.py")
"""