#! usr/bin/env python
# -*- coding: utf-8 -*-
import math
f = open("input.txt", "r+")
g = open("output.txt","r+")
numbers = f.readline()
nums = []
nums = numbers.split(" ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.remove(nums[0])
nums = sorted(nums)
print(nums)


if len(nums) % 2 == 1:
    print("y")
    print(nums[int((len(nums)/2)-0.5)])
    g.write(str(nums[int((len(nums)/2)-0.5)]))

else:
    print("n")
    a = (len(nums)/2)
    b = (len(nums)/2) - 1
    c = (nums[int(a)] + nums[int(b)]) / 2.0
    g.write(str(math.floor(c)))

f.close()
g.close()
