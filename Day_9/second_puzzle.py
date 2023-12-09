def recursive_difference_extrapolator(sequence):
    if all(x == 0 for x in sequence):
        return 0
    differences = [y - x for x, y in zip(sequence, sequence[1:])]
    diff = recursive_difference_extrapolator(differences)
    return sequence[-1] + diff


sum_n = 0
for sequence_v in open("./puzzle.txt"):
    sequence = list(map(int, sequence_v.split()))
    split_val = recursive_difference_extrapolator(sequence[::-1])
    sum_n += split_val
    # print(split_val)


print(sum_n)
