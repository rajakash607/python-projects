# Black jack game
'''
1. array of cards from 1 to 10 and 10 occuring 4 times
2. player will be given 2 cards at the beginning and computer 1
3. you will chose if you want to get another card or not
4. if not continue then computer will select cards and if sum will go above 21 of any side that side lost.
'''
import random
cards_collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_performance = False
player_cards = []
player_cards.append(random.choice(cards_collection))
player_cards.append(random.choice(cards_collection))
print(f"Player's cards are {player_cards}")
computer_cards = []
computer_cards.append(random.choice(cards_collection))
print(f"Computer's cards are {computer_cards}")
n_selected = False
while (sum(player_cards) < 21 and n_selected == False):
    user_selection = input("press y to choose another card and n to stand ")
    if (user_selection == "y"):
        player_cards.append(random.choice(cards_collection))
        print(f"Now Player's cards are {player_cards}")
    else:
        n_selected = True

if (sum(player_cards) > 21):
    print(
        f"Player one loses as the sum of the cards of player is {sum(player_cards)} which is well over 21")
    player_performance = False

else:
    while (sum(computer_cards) < 21 and sum(computer_cards) < sum(player_cards)):
        computer_cards.append(random.choice(cards_collection))
    print(f"Now computer's cards are {computer_cards}")
    print(f"Player has card sum of {sum(player_cards)}")

if (sum(computer_cards) > 21):
    player_performance = True

if (player_performance == True):
    print(f"Player won")
else:
    print("computer won")
