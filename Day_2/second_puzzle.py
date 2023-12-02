import re

cube_list = []
with open("./puzzle.txt") as file:
    for num, line in enumerate(file.readlines(), 1):
        res = re.findall(r"(\d{1,3})( blue\.?| red\.?| green\.?)", line, re.M)
        max_val = {"red": 0, "blue": 0, "green": 0}
        for val, color in res:
            color = color[1:]
            max_val[color] = max(int(val), max_val[color])

        cube_list.append(max_val["red"] * max_val["green"] * max_val["blue"])


sum_n = 0
for num in cube_list:
    sum_n += num

print(sum_n)
