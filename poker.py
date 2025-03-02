from collections import Counter
import copy

def best_hands(hands):

    original_hands = hands.copy()
    
    single_hand = []

    # Dividir as mãos em listas de cartas
    for hand in hands:
        single_hand.append(hand.split())

    Values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    different_hands = []

    for hand in single_hand:
        formatted_hand = []
        for card in hand:
            formatted_hand.append([Values[card[:-1]], card[-1]])
        different_hands.append(sorted(formatted_hand))

    print(f"simple_hand: {different_hands}")

    best_hand = get_royal_straight_flush_hand(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]
        
    best_hand = get_straight_flush(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]

    best_hand = get_poker(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]
    
    best_hand = get_full_house(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]

    best_hand = get_flush(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]

    best_hand = get_straight(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]
        
    best_hand = get_three_of_a_kind(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]

    best_hand = get_two_pairs(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]
    
    best_hand = get_one_pair(different_hands)
    if best_hand:
        return [' '.join(f"{card[0]}{card[1]}" for card in best_hand)]
    
    best_hand = get_high_card(different_hands)
    if best_hand is not None:
        return [original_hands[best_hand]]

    else:
        print("Something went wrong!!")

def get_royal_straight_flush_hand(hands):
    
    for hand in hands:
        value = [card[0] for card in hand]
        suit = [card[1] for card in hand]

        if sum(value) == 60 and len(set(suit)) == 1:
            return hand
    return None
    
def get_straight_flush(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]
        
        result = (max(value) - min(value) == 4) and len(set(suit)) == 1
        
        if result:
            return hand
    return None
    
def get_poker(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        count = Counter(value)

        for k in count.values():
            if k == 4:
                return hand
    return None

def get_full_house(hands):
    
    for hand in hands:    
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        count = Counter(value)
        count_values = list(count.values())

        if len(count_values) != 2:
            return None

        if (count_values[0] == 3 and count_values[1] == 2) or (count_values[0] == 2 and count_values[1] == 3):
            return hand
    return None
    
def get_flush(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        if len(set(value)) == len(value) and len(set(suit)) == 1:
            return hand
    return None

def get_straight(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        if ((value[-1] - value[0]) == 4 and len(set(suit)) != 1) or ((value[-1] - value[0]) == -9 and len(set(suit)) != 1):
            return hand
    return None
    
def get_three_of_a_kind(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        count = Counter(value)

        for k in count.values():
            if k == 3:
                return hand
    return None

def get_two_pairs(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        result = len(set(value)) == 3

        if result:
            return hand
    return None

def get_one_pair(hands):
    for hand in hands:
        value = [int(card[0]) for card in hand]
        suit = [card[1] for card in hand]

        result = len(set(value)) == 4
        
        if result:
            return hand
    return None

def get_high_card(hands):

    indice = None
    max_value = 0 
    
    for i,hand in enumerate(hands):
        value = [card[0] for card in hand]
        suit = [card[1] for card in hand]

        if (max(value)) > max_value:
            indice = i
            max_value = max(value)
            
    return indice

result = best_hands(["4S 5S 7H 8D JC"])
print(result)
