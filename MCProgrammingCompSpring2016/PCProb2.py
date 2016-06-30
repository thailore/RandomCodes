#! usr/bin/env python
# -*- coding: utf-8 -*-

f = open("input.txt", "r+")
g = open("output.txt","r+")
next(f)
for line in f:
    number = list(line)
    number = number[:-1]
    number = "".join(str(x) for x in number)
    number = int(number)
    print(number)
    total = 0
    for i in range(1,number):
        if number/i % 1 == 0:
            total+=i
    if total > number:
        g.write(str(number) + " superb" + "\n")
        print("superb")
    else:
        g.write(str(number) + " non-superb" + "\n")
        print("non")

g.close()
f.close()
