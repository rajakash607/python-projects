# there will be two levels of this game, Hard and Easy. For Hard 5 guesses are allowed and 10 for Easy level
# you have to choose level at the start of the game.

import random
guess = False
logo = '''
   _____ _____  ______       _______    _____ _    _ ______  _____ _____ _____ _   _  _____    _____          __  __ ______ 
  / ____|  __ \|  ____|   /\|__   __|  / ____| |  | |  ____|/ ____/ ____|_   _| \ | |/ ____|  / ____|   /\   |  \/  |  ____|
 | |  __| |__) | |__     /  \  | |    | |  __| |  | | |__  | (___| (___   | | |  \| | |  __  | |  __   /  \  | \  / | |__   
 | | |_ |  _  /|  __|   / /\ \ | |    | | |_ | |  | |  __|  \___ \\___ \  | | | . ` | | |_ | | | |_ | / /\ \ | |\/| |  __|  
 | |__| | | \ \| |____ / ____ \| |    | |__| | |__| | |____ ____) |___) |_| |_| |\  | |__| | | |__| |/ ____ \| |  | | |____ 
  \_____|_|  \_\______/_/    \_\_|     \_____|\____/|______|_____/_____/|_____|_| \_|\_____|  \_____/_/    \_\_|  |_|______|
                                                                                                                            
                                                                                                                            
'''
print(logo)


def set_difficulty():
    if input("Choose your difficulty level from 'Easy' and 'Hard'. ") == "Hard":
        return 5
    else:
        return 10


no_of_attempts = set_difficulty()


actual_number = random.randint(1, 100)

print("Computer has guessed a number now its your turn.")

while guess is not True and no_of_attempts > 0:
    print(f"No. of guesses left is {no_of_attempts}")
    guessed_no = input("Enter guessed number according to you ")
    guessed_no = int(guessed_no)
    if guessed_no == actual_number:
        guess = True
    elif guessed_no < actual_number:
        print(f"Guessed number is Too small")
    elif guessed_no > actual_number:
        print(f"Guessed no is Too large")
    no_of_attempts -= 1
if guess == True:
    print(
        f"You guessed the right number which is {guessed_no} \nHey thanks for playing")
elif guess == False:
    print(f"You didn't guess the right number which was {actual_number}")
    print(f"You can try again if you wanna win! \nHey thanks for playing")
