import re

race_details = open("./puzzle.txt").read().split("\n")
race_details = race_details[:-1]
time_list = []
distance_list = []
for num, line in enumerate(race_details):
    res = re.findall(r"\d", line, re.M)
    if num == 0:
        time_list = res
    else:
        distance_list = res

can_beat_val = 1
time_total = ""
distance_total = ""
for i in time_list:
    time_total += i

for i in distance_list:
    distance_total += i

time_val = int(time_total)
distance_val = int(distance_total)

can_beat = 0
if time_val % 2 == 0:
    range_val = time_val // 2
else:
    range_val = time_val // 2 + 1
for n in range(range_val):
    holding_time = n
    driving_time = time_val - n
    # print("Holding time", holding_time)
    # print("driving_time", driving_time)
    distance_travelled = driving_time * holding_time
    if distance_travelled > distance_val:
        # print(distance_travelled)
        can_beat += 1
if time_val % 2 == 0:
    can_beat = can_beat * 2 + 1
else:
    can_beat = can_beat * 2
can_beat_val = can_beat_val * can_beat

print(can_beat_val)
