plays = []

for line in open("./puzzle.txt"):
    hand, bid = line.split(" ")
    plays.append((hand, int(bid)))

letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}


def classify_hand(hand):
    # print("got here", hand)
    counts = [hand.count(card) for card in hand]
    # print(counts)

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def strength_of_hand(hand):
    return (
        classify_hand(hand),
        [letter_map.get(hand_val, hand_val) for hand_val in hand],
    )


plays.sort(key=lambda play: strength_of_hand(play[0]))

score = 0
for rank, (hand, bid) in enumerate(plays, 1):
    score += rank * bid

print(score)
