import art
import random
import game_data
print(art.logo)
continue_game = True
no1 = random.randint(0, 49)
no2 = random.randint(0, 49)
while continue_game is True:
    print(
        f"Compare A: {game_data.data[no1]['name']}, a {game_data.data[no1]['description']} from {game_data.data[no1]['country']}")
    print(art.vs)
    print(
        f"Against B: {game_data.data[no2]['name']}, a {game_data.data[no2]['description']} from {game_data.data[no2]['country']} \n\n\n")
    selection = input(f"Who has more followers 'A' or 'B' ")
    if game_data.data[no1]['follower_count'] > game_data.data[no2]['follower_count']:
        real_winner = "A"
    else:
        real_winner = "B"
    if selection == real_winner:
        print(f"Good now choose between")
    else:
        print(f"Oops! wrong choice, Play again.")
        continue_game = False
    if real_winner == "A":
        no2 = random.randint(0, 49)
    if real_winner == "B":
        no1 = random.randint(0, 49)
