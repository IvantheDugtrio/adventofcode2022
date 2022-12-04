#!/usr/bin/env python3

# Ivan De Dios - Day 3 part 2 Advent of Code 2022

ascii_lc_const = -96
ascii_uc_const = -64 + 26
badge_items = []
elf_counter = 0
group_id = 0
elf_group = {}
elf_group[group_id] = []
with open('rucksack.txt', 'r') as rst:
    for rucksack in rst:
        rucksack = rucksack.rstrip()
        if elf_counter < 3:
            elf_group[group_id] += [rucksack]
            elf_counter += 1
        else:
            print(group_id, elf_group[group_id])
            two_elf_common_items = set(elf_group[group_id][0]).intersection(set(elf_group[group_id][1]))
            common_item = two_elf_common_items.intersection(set(elf_group[group_id][2]))
            badge_items += common_item
            group_id += 1
            elf_group[group_id] = [rucksack]
            elf_counter = 1
print(group_id)
sum_priority = 0
for item in badge_items:
    if item.isupper():
        sum_priority += ord(item) + ascii_uc_const
    else:
        sum_priority += ord(item) + ascii_lc_const
print(sum_priority)
