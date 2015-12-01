#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Wanted to simulate the odds of the Powerball Lottery:
In order to reduce runtime, as it would have had to be at least 100 x 200million+ runs to get some results, 
I reduced it to 100 x 100,000 runs, and only checked for 5 numbers instead of 6. 
Code can certainly be better, but is altered specifically to get results for project
"""
import time
import random

def get_random_set():
    random_nums = list()
    # add first 5 numbers
    for _ in range(5):
        success = False
        # while loop to account for no replacement
        while success is not True:
            num = random.randint(1,59)
            if num in random_nums: #check if in list
                pass
            else:
                random_nums.append(num) #if not, add to list
                success = True
    # add last number representing red ball
    # can be repeat of first 5 numbers.
    random_nums.append(random.randint(1,25))

    return set(random_nums)                   


def compare_sets(winning, drawn):
    # check if numbers are similar, order not mattering, only checking for 5 matching
    if len(set(winning) & set(drawn)) == 5:
           return True
    else:
           return False


def main():
    for _ in range(100):
        match = 0
        no_match=0
        winning = get_random_set()
        # Should be 200 Million plus, cut down to 100000
        # in order to rerun numerous times
        # Print out test number
        print("test{}".format(_))
        for _ in range(100000):
            drawn = get_random_set()
            same_set = compare_sets(winning, drawn)
            if same_set == True:
                match+=1
            else:
                no_match+=1

        print("Matches:{0}, Non Matches:{1}".format(match, no_match))


if __name__ == '__main__':
    main()
