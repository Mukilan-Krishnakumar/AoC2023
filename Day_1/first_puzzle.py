num_list = []
with open("puzzle.txt") as file:
    for line in file.readlines():
        temp_list = []
        for char in line:
            if char.isnumeric():
                temp_list.append(char)
        num_list.append(temp_list)

sum = 0
for line in num_list:
    first_digit = line[0]
    second_digit = line[-1]
    final_digit = int(f"{first_digit}{second_digit}")
    sum += final_digit

print(sum)
