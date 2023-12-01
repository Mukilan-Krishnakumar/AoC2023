num_list = []
three_letter = {
    "one": "1",
    "two": "2",
    "six": "6",
}
four_letter = {
    "four": "4",
    "five": "5",
    "nine": "9",
}
five_letter = {
    "three": "3",
    "seven": "7",
    "eight": "8",
}
with open("puzzle.txt") as file:
    for line in file.readlines():
        temp_list = []
        for num, char in enumerate(line, 1):
            if char.isnumeric():
                temp_list.append(char)
            if num >= 3:
                if line[num - 3 : num] in three_letter:
                    temp_list.append(three_letter[line[num - 3 : num]])
            if num >= 4:
                if line[num - 4 : num] in four_letter:
                    temp_list.append(four_letter[line[num - 4 : num]])
            if num >= 5:
                if line[num - 5 : num] in five_letter:
                    temp_list.append(five_letter[line[num - 5 : num]])

        num_list.append(temp_list)

sum = 0
for line in num_list:
    first_digit = line[0]
    second_digit = line[-1]
    final_digit = int(f"{first_digit}{second_digit}")
    sum += final_digit

print(sum)
