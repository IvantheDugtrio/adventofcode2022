#!/usr/bin/env python3

# Ivan De Dios - Day 1 - part 1
elf_dict = {}
calories = 0
greatest_calories = 0
index = 1
with open('calories.txt','r') as ct:
    for line in ct:
        if (line == '\n'):
            elf_dict[index] = calories
            if (greatest_calories < calories):
                greatest_calories = calories
                greatest_elf = index
            calories = 0
            index += 1
        else:
            calories += int(line.rstrip())
sorted_elves = dict(sorted(elf_dict.items(), key=lambda x:x[1], reverse=True))
counter = 0
sum_calories = 0
for elf in sorted_elves:
    if counter < 3:
        print(elf, sorted_elves[elf])
        sum_calories += sorted_elves[elf]
        counter += 1
print(sum_calories)
