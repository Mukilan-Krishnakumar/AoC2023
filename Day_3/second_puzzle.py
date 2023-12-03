grid = open("./puzzle.txt").read().split("\n")

sum_n = 0
for row_n, row in enumerate(grid):
    for col_n, col in enumerate(row):
        if col.isdigit() or col == ".":
            continue
        beginning_set = set()
        for col_r in [row_n - 1, row_n, row_n + 1]:
            for col_c in [col_n - 1, col_n, col_n + 1]:
                if (
                    col_r < 0
                    or col_c < 0
                    or col_r >= len(grid)
                    or col_c >= len(grid[col_r])
                    or not grid[col_r][col_c].isdigit()
                ):
                    continue
                # Not, getting to the beggining of the number
                while col_c > 0 and grid[col_r][col_c - 1].isnumeric():
                    col_c -= 1
                beginning_set.add((col_r, col_c))
        if len(beginning_set) != 2:
            continue

        num_list = []
        for coords in beginning_set:
            x, y = coords
            num = str(grid[x][y])
            while grid[x][y + 1].isnumeric():
                y += 1
                num += str(grid[x][y])
            num_list.append(num)

        mul_val = 1
        for num in num_list:
            mul_val *= int(num)
        sum_n += mul_val

print(sum_n)

#
# sum_n = 0
# for num in num_list:
#     sum_n += int(num)
#
# print(sum_n)
