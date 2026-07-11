import random 

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#Now, we are going to choicesa random words

Game_Words = random.choice(word_list)
print(Game_Words)

#total lives numbers
lives = 6

gameOver = False
FINAL_GAME_WORD_LIST = []

#check the input with gues latters
while not gameOver:
    #Ask user to enter a letter to gues
    Gues_latters = input("enter your gues letters: ").lower()

    Display =""

    for each in Game_Words:
        if each == Gues_latters:
            Display+=each
            FINAL_GAME_WORD_LIST+=each
        elif each in FINAL_GAME_WORD_LIST:
            Display+=each
        else:
            Display+= "_"

    print(Display)

    if Gues_latters not in Game_Words:
        lives -= 1
        print(HANGMANPICS[lives])
        if lives == 0:
            gameOver = True
            print("You Lose")


    if "_" not in Display:
        gameOver = True
        print("YOU HAVE WON THE GAME")

    