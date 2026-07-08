print("Welcome To Play Rock, Paper, Scissors Game");
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! Rock beats scissors.")
    else:
        print("You lose! Paper beats rock.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! Paper beats rock.")
    else:
        print("You lose! Scissors beats paper.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("You lose! Rock beats scissors.")