from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    FIVE_OF_A_KIND = 9

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


@dataclass
class Hand:
    type: HandType
    bid: int = 0
    cards: list = None
    rank: int = 0


cards_ordered = '23456789TJQKA'
cards_ordered_part2 = 'J23456789TQKA'


def get_hand_type(cards):
    found_triplet = False
    found_pair = False
    triplet_card = ''
    pair_card = ''
    for card in cards:
        if cards.count(card) == 5:
            return HandType.FIVE_OF_A_KIND
        elif cards.count(card) == 4:
            return HandType.FOUR_OF_A_KIND
        elif cards.count(card) == 3 and triplet_card != card:
            found_triplet = True
            triplet_card = card
        elif cards.count(card) == 2 and triplet_card != card and triplet_card != '':
            return HandType.FULL_HOUSE
        elif cards.count(card) == 2 and pair_card == '':
            found_pair = True
            pair_card = card
        elif cards.count(card) == 2 and pair_card != card:
            return HandType.TWO_PAIR
    if found_triplet and found_pair:
        return HandType.FULL_HOUSE
    elif found_triplet:
        return HandType.THREE_OF_A_KIND
    elif found_pair:
        return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD
    
def get_hand_type_part2(cards):
    found_triplet = False
    found_pair = False
    triplet_card = ''
    pair_card = ''
    num_jokers = cards.count('J')
    for card in cards:
        if card == 'J':
            if num_jokers == 5:
                return HandType.FIVE_OF_A_KIND
            continue
        if cards.count(card) == 5:
            return HandType.FIVE_OF_A_KIND
        elif cards.count(card) == 4:
            if num_jokers == 1:
                return HandType.FIVE_OF_A_KIND
            return HandType.FOUR_OF_A_KIND
        elif cards.count(card) == 3 and triplet_card != card:
            if num_jokers == 2:
                return HandType.FIVE_OF_A_KIND
            elif num_jokers == 1:
                return HandType.FOUR_OF_A_KIND
            found_triplet = True
            triplet_card = card
        elif cards.count(card) == 2 and triplet_card != card and triplet_card != '':
            return HandType.FULL_HOUSE
        elif cards.count(card) == 2 and pair_card == '':
            if num_jokers == 3:
                return HandType.FIVE_OF_A_KIND
            elif num_jokers == 2:
                return HandType.FOUR_OF_A_KIND
            elif num_jokers == 1:
                found_triplet = True
                triplet_card = card
            else:
                found_pair = True
                pair_card = card
        elif cards.count(card) == 2 and pair_card != card:
            if num_jokers == 1:
                return HandType.FULL_HOUSE
            return HandType.TWO_PAIR
    if found_triplet and found_pair:
        return HandType.FULL_HOUSE
    elif found_triplet:
        return HandType.THREE_OF_A_KIND
    elif found_pair:
        return HandType.ONE_PAIR
    else:
        if num_jokers == 4:
            return HandType.FIVE_OF_A_KIND
        elif num_jokers == 3:
            return HandType.FOUR_OF_A_KIND
        elif num_jokers == 2:
            return HandType.THREE_OF_A_KIND
        elif num_jokers == 1:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD


def parse_input(filename, part2 = False):
    with open(filename) as f:
        lines = f.readlines()
    hands = []
    for line in lines:
        cards = line.split(' ')[0]
        bid = int(line.split(' ')[1])
        if part2:
            type = get_hand_type_part2(cards)
        else:
            type = get_hand_type(cards)
        hands.append(Hand(type, bid, cards))
    return hands


def compare_hands(hand1, hand2):
    if hand1.type > hand2.type:
        return 1
    elif hand1.type < hand2.type:
        return -1
    else:
        for card1, card2 in zip(hand1.cards, hand2.cards):
            if cards_ordered_part2.index(card1) > cards_ordered_part2.index(card2):
                return 1
            elif cards_ordered_part2.index(card1) < cards_ordered_part2.index(card2):
                return -1

def compare_hands_part2(hand1, hand2):
    if hand1.type > hand2.type:
        return 1
    elif hand1.type < hand2.type:
        return -1
    else:
        for card1, card2 in zip(hand1.cards, hand2.cards):
            if cards_ordered.index(card1) > cards_ordered.index(card2):
                return 1
            elif cards_ordered.index(card1) < cards_ordered.index(card2):
                return -1


def sort_hands_part1(hands, part2 = False):
    best_rank = len(hands)
    if part2:
        cmp_function = cmp_to_key(compare_hands_part2)
    else:
        cmp_function = cmp_to_key(compare_hands)
    hands.sort(key=cmp_function, reverse=True)
    for hand in hands:
        hand.rank = best_rank
        best_rank -= 1
    return hands


if __name__ == '__main__':
    hands = parse_input('input.txt')
    hands = sort_hands_part1(hands)
    sol_part1 = 0
    for hand in hands:
        sol_part1 += hand.rank * hand.bid
    print(f'Solucion parte 1: {sol_part1}')
    hands_part2 = parse_input('input.txt', True)
    hands_part2 = sort_hands_part1(hands_part2, False)
    sol_part2 = 0
    for hand in hands_part2:
        sol_part2 += hand.rank * hand.bid
    print(f'Solucion parte 2: {sol_part2}')