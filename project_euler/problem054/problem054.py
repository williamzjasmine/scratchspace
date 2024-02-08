def convert_hand(hand):
    new_hand = []
    for card in hand:
        suit = card[1]
        if card[0] == 'T':
            num = 10
        elif card[0] == 'J':
            num = 11
        elif card[0] == 'Q':
            num = 12
        elif card[0] == 'K':
            num = 13
        elif card[0] == 'A':
            num = 14
        else:
            num = int(card[0])
        new_hand.append([num, suit])
    return new_hand


def calc_flush(hand):
    nums = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    if len(set(suits)) == 1:
        return max(nums)
    else:
        return 0

def calc_straight(hand):
    nums = [card[0] for card in hand]
    print(nums)
    if max(nums) - min(nums) == 4:
        return max(nums)
    else:
        return 0


def calc_straight_flush(hand):
    is_flush = calc_flush(hand)
    is_straight = calc_straight(hand)
    if is_flush > 0  and is_straight > 0:
        return is_straight
    else:
        0


def calc_royal_straight_flush(hand):
    is_straight_flush = calc_straight_flush(hand)
    if is_straight_flush == 14:
        return True
    else:
        return False


def calc_lower_hands(hand):
    counter = {}
    for card in hand:
        if card[0] not in counter:
            counter[card[0]] = 0
        counter[card[0]] += 1

    counts = sorted([v for k, v in counter.items() if v != 1])
    if counts == 2
    return counts

sample_hand = ['JD', 'JD', 'JS', '8D', '9D']

check = convert_hand(sample_hand)
flush_check = calc_flush(check)
straight_check = calc_straight(check)
counts_check = calc_pairs(check)
print(flush_check, straight_check, counts_check)