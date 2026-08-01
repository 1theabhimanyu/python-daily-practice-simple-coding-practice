from random import randint 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_number):
    if user_guess > actual_number:
        print("Too high")
    elif user_guess < actual_number:
        print("Too low")
    else:
        print(f"You got it! {actual_number}")

def set_difficulties():
    level = input("Choose difficulties level: easy or hard ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    if level == "hard":
        return HARD_LEVEL_TURNS

print("Welcome To Our Number Guessing!")
print("Please wait! I'm thinking a number")
answer = randint(1,100)


turns = set_difficulties()
print(f"You have {turns} left.")

guess = 0
while guess != answer:

    guess = int(input("Make a guess: "))
    check_answer(guess, answer)