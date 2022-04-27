def value_of_card(card):
    if card == 'A':
        return 1
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return int(card)
    


def higher_card(card_one, card_two):
    primera = value_of_card(card_one)
    segunda = value_of_card(card_two)
    
    if primera > segunda:
        return card_one
    elif primera < segunda:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    primera = int(value_of_card(card_one))
    segunda = int(value_of_card(card_two))
    suma = primera + segunda

    if suma <= 10:
        return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    primera = int(value_of_card(card_one))
    segunda = int(value_of_card(card_two))

    if "A" in (card_one + card_two):
        if card_one == "A":
            primera = 11
        if card_two == "A":
            segunda= 11
    
    return primera + segunda == 21


def can_split_pairs(card_one, card_two):
    primera = int(value_of_card(card_one))
    segunda = int(value_of_card(card_two))

    return primera == segunda


def can_double_down(card_one, card_two):
    primera = int(value_of_card(card_one))
    segunda = int(value_of_card(card_two))
    resp = primera + segunda in [9, 10, 11]
    return resp

