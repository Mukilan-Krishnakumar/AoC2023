import re

num_list = []
with open("./puzzle.txt") as file:
    for num, line in enumerate(file.readlines(), 1):
        res = re.findall(r"(\d{1,3})( blue\.?| red\.?| green\.?)", line, re.M)
        max_val = {"red": 0, "blue": 0, "green": 0}
        for val, color in res:
            color = color[1:]
            max_val[color] = max(int(val), max_val[color])

        if max_val["red"] <= 12 and max_val["blue"] <= 14 and max_val["green"] <= 13:
            num_list.append(num)

sum_n = 0
for num in num_list:
    sum_n += num

print(sum_n)
