import re

sum_n = 0
games = open("./small_puzzle.txt").read().split("\n")
for game in games[:-1]:
    res = re.split(": | \| ", game)
    winning_set = set()
    observation_set = set()
    for i in res[1].split(" "):
        if i != "":
            winning_set.add(i)
    for i in res[2].split(" "):
        if i != "":
            observation_set.add(i)
    common_set = winning_set.intersection(observation_set)
    power_val = len(common_set) - 1
    if power_val >= 0:
        sum_n += pow(2, power_val)

print(sum_n)
