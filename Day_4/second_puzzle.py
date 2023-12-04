import re

games = open("./puzzle.txt").read().split("\n")
games_n = len(games)

card_dict = {str(x): 1 for x in range(1, games_n)}
for num, game in enumerate(games[:-1], 1):
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
    power_val = len(common_set)
    if power_val >= 0:
        current_val = card_dict[str(num)]

        for val in range(num + 1, num + power_val + 1):
            card_dict[str(val)] = current_val + card_dict[str(val)]
sum_n = 0
for k, v in card_dict.items():
    sum_n += v

print(sum_n)
