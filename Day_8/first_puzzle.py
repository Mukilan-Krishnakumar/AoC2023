import re

instruction = open("./puzzle.txt").read().split("\n")[0]

mapping = open("./puzzle.txt").read().split("\n")
len_map = len(mapping)
haunted_map = {}
for map_n, mapping_line in enumerate(mapping, 1):
    if map_n > 2 and map_n < len_map:
        res = re.findall(r"\w{3}", mapping_line, re.M)
        haunted_map[res[0]] = (res[1], res[2])

instruction_map = {"L": 0, "R": 1}

n = 0
current_loc = "AAA"
while current_loc != "ZZZ":
    print("Current Iteration", n)
    for instruction_val in instruction:
        print("instruction_val", instruction_val)
        if current_loc == "ZZZ":
            exit(0)
        current_loc = haunted_map[current_loc][instruction_map[instruction_val]]
        print("Updated loc", current_loc)
        n += 1

print(n)
