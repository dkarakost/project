from random import randrange
from random import seed


# declare a card with 2 attributes
number = {"ace",2,3,4,5,6,7,8,9,10, "jack","queen","king"}
kind = {"heart", "diamond", "spade", "club"}
deck = [(k,n) for n in number for k in kind]
# two persons at the beginning with a empty set that hold in persons hand

player1 = set()
player2 = set()

list_deck = list(deck)
for _ in range(5):
    pos1 = randrange(len(list_deck))
    player1.add(list_deck.pop(pos1))
    pos2 = randrange(len(list_deck))
    player2.add(list_deck.pop(pos2))

print(player1)
print(player2)


i = 0
j = 0
for card in player1:
    if card[1] == 'ace':
        i += 1
for card in player2:
    if card[1] == 'ace':
        j += 1

if i == 4:
    print("player1 has won")
elif j == 4:
    print("player2 has won")

# if a player has kenta
hand_numbers = []
for card in player1:
    if card[1] == "ace":
        hand_numbers.append(1)
    elif card[1] == "jack":
        hand_numbers.append(11)
    elif card[1] == "queen":
        hand_numbers.append(12)
    elif card[1] == "king":
        hand_numbers.append(13)
    else:
        hand_numbers.append(card[1])
hand_numbers.sort()

print(hand_numbers)
for pos in range(4):
    if hand_numbers[pos] != hand_numbers[pos + 1] - 1:
        break
else:
    print("player1 has strike")
hand_numbers2 = []
for card in player2:
    if card[1] == "ace":
        hand_numbers2.append(1)
    elif card[1] == "jack":
        hand_numbers2.append(11)
    elif card[1] == "queen":
        hand_numbers2.append(12)
    elif card[1] == "king":
        hand_numbers2.append(13)
    else:
        hand_numbers2.append(card[1])
hand_numbers2.sort()

print(hand_numbers2)
for pos in range(4):
    if [pos] != hand_numbers2[pos + 1] - 1:
        break
else:
    print("player2 has strike")









