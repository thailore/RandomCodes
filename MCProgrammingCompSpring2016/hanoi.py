#! usr/bin/env python
# -*- coding: utf-8 -*-


a = []

def move(num_disks, from_post, spare_post, to_post):
    if num_disks ==0:
        return
    move(num_disks - 1, from_post, to_post, spare_post)
    #print("Move disk {0} from {1} to {2}".format(num_disks, from_post, to_post))
    a.append("Move disk {0} from {1} to {2}".format(num_disks, from_post, to_post))
    move(num_disks-1, spare_post, from_post, to_post)


f = open("input.txt", "r+")
g = open("output.txt","r+")
count = 1

for line in f:
    if line == "0 0 \n":
        break
    numbers = line.split(" ")
    print(numbers)
    reals = []
    reals.append(int(numbers[0]))
    reals.append(int(numbers[1]))
    #print(reals)
    move(reals[1],"A","B","C")
    print(reals)
    #print(a)
    added = a[reals[0]-1]
    added = added.split(" ")
    #print(added)
    g.write("Case {0}: {1} {2} {3}\n".format(count, added[2],added[4],added[6]))
    count+=1
    if not not a:
        a.clear()

f.close()
g.close()


"""
8 4
1 3
2 3
3 3
4 3
8192 14
"""
    




