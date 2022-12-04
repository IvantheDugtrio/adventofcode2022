#!/usr/bin/env python3

# Ivan De Dios - Day 3 part 1 Advent of Code 2022

ascii_lc_const = -96
ascii_uc_const = -64 + 26
common_items = []
with open('rucksack.txt', 'r') as rst:
    for rucksack in rst:
        rucksack = rucksack.rstrip()
        num_items = len(rucksack)
        num_half_items = int(num_items/2)
        compartment1 = rucksack[0:num_half_items]
        compartment2 = rucksack[num_half_items:num_items+1]
        for item in compartment1:
            if item in compartment2:
                common_items += [item]
                break # exit rucksack once common item is found
sum_priority = 0
for item in common_items:
    if item.isupper():
        sum_priority += ord(item) + ascii_uc_const
    else:
        sum_priority += ord(item) + ascii_lc_const
print(sum_priority)
