#!/usr/bin/env python3

# Ivan De Dios - Day 2 part 1 of Advent of Code 2022

score_dict = {
        'B X':1,
        'C Y':2,
        'A Z':3,
        'A X':4,
        'B Y':5,
        'C Z':6,
        'C X':7,
        'A Y':8,
        'B Z':9
        }
my_total_score = 0
with open('strategy.txt', 'r') as st:
    for line in st:
        if line == '\n':
            break
        line = line.rstrip()
        my_total_score += score_dict[line]
print(my_total_score)
