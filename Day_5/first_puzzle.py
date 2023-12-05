import re

# from operator import itemgetter

seed_nums = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
conversion_list = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location,
]
conversion_list = conversion_list[::-1]
l_con = len(conversion_list)
with open("./puzzle.txt") as file:
    for line_n, line in enumerate(file.readlines()):
        if line_n == 0:
            res = re.findall(r"\d+", line, re.M)
            seed_nums = res
        else:
            if line == "\n" and l_con >= len(conversion_list) >= 1:
                temp = conversion_list[-1]
                conversion_list = conversion_list[:-1]
                continue
            res = re.findall(r"\d+", line, re.M)
            if res != []:
                temp.append(res)


def check_in_range(looping_list, check_val):
    check_num = 0
    for res in looping_list:
        if check_val in range(int(res[1]), int(res[1]) + int(res[2])):
            check_num = check_val + int(res[0]) - int(res[1])
    if check_num == 0:
        check_num = check_val
    return check_num


location_list = []
for seed_num in seed_nums:
    seed_val = int(seed_num)
    soil_num = check_in_range(seed_to_soil, seed_val)
    fertilizer_num = check_in_range(soil_to_fertilizer, soil_num)
    water_num = check_in_range(fertilizer_to_water, fertilizer_num)
    light_num = check_in_range(water_to_light, water_num)
    temperature_num = check_in_range(light_to_temperature, light_num)
    humidity_num = check_in_range(temperature_to_humidity, temperature_num)
    location_num = check_in_range(humidity_to_location, humidity_num)
    location_list.append(location_num)

print(min(location_list))
