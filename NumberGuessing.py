from random import randint 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_number, turns):
    if user_guess > actual_number:
        print("Too high")
        return turns -1
    elif user_guess < actual_number:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! {actual_number}")

def set_difficulties():
    """Check and rweturn the number of turns remaining"""
    level = input("Choose difficulties level: easy or hard ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    if level == "hard":
        return HARD_LEVEL_TURNS

def game():
    print("Welcome To Our Number Guessing!")
    print("Please wait! I'm thinking a number")
    answer = randint(1,100)


    turns= set_difficulties()
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} left.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            break;

game()