#!/usr/bin/env python3

# Ivan De Dios - Day 2 part 2 of Advent of Code 2022

score_dict = {
        'B X':['A',1],
        'C X':['B',2],
        'A X':['C',3],
        'A Y':['A',4],
        'B Y':['B',5],
        'C Y':['C',6],
        'C Z':['A',7],
        'A Z':['B',8],
        'B Z':['C',9]
        }
my_total_score = 0
with open('strategy.txt', 'r') as st:
    for line in st:
        if line == '\n':
            break
        line = line.rstrip()
        my_total_score += score_dict[line][1]
print(my_total_score)
