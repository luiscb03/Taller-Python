"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [*range(number, number + 3)]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    avg = card_average(hand)
    return avg == float(hand[len(hand) // 2]) or avg == (hand[0] + hand[-1]) / 2


def average_even_is_average_odd(hand):
    evens = []
    odds = []
    for i in hand:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return card_average(evens) == card_average(odds)


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand