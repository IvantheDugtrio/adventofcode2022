#!/usr/bin/env python3

# Ivan De Dios - Day 4 part 1 Advent of Code 2022

contain_counter = 0
with open('assignments.txt', 'r') as at:
    for pairs in at:
        if pairs == '\n':
            break
        pairs = pairs.rstrip()
        range1 = pairs.split(',')[0]
        range2 = pairs.split(',')[1]
        r1_lb = int(range1.split('-')[0])
        r1_ub = int(range1.split('-')[1])
        r2_lb = int(range2.split('-')[0])
        r2_ub = int(range2.split('-')[1])
        if ((r1_lb <= r2_lb and r1_ub >= r2_ub) or
                (r2_lb <= r1_lb and r2_ub >= r1_ub)):
            contain_counter += 1
print(contain_counter)
