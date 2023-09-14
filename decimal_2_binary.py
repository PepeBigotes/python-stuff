#!/usr/bin/env python3
#Created by PepeBigotes
#  Our teacher was explaining how to convert decimal numbers to binary,
#  I got bored and decided to make a script to do it for me instead.

input = 32
bits = 8

nums = list()
result = list()
nums.append(1)

for i in range(1, bits):
    nums.append(nums[i-1] * 2)
    
nums = nums[::-1]
print(nums)

for i in range(0 , bits):
    if input >= nums[i]:
        result.append(1)
        input = input-nums[i]
    else:
        result.append(0)
        
print(result)