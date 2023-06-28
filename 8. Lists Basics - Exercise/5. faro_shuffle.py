deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_list = []
    middle_of_deck = len(deck_of_cards) // 2
    left_side_of_deck = deck_of_cards[0:middle_of_deck]
    right_side_of_deck = deck_of_cards[middle_of_deck:]
    for current_card in range(len(left_side_of_deck)):
        final_list.append(left_side_of_deck[current_card])
        final_list.append(right_side_of_deck[current_card])
    deck_of_cards = final_list

print(deck_of_cards)
