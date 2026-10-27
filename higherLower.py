import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \\/ _ \\/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\\__, /_/ /_/\\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \\ | /| / / _ \\/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\\____/|__/|__/\\___/_/        

"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""
data = [
  {
    "name": "Instagram",
    "follower_count": 346,
    "description": "Social media platform",
    "country": "United States",
  },
  {
    "name": "Cristiano Ronaldo",
    "follower_count": 215,
    "description": "Footballer",
    "country": "Portugal",
  },
  {
    "name": "Ariana Grande",
    "follower_count": 183,
    "description": "Musician and actress",
    "country": "United States",
  },
  {
    "name": "Dwayne Johnson",
    "follower_count": 181,
    "description": "Actor and professional wrestler",
    "country": "United States",
  },
  {
    "name": "Selena Gomez",
    "follower_count": 174,
    "description": "Musician and actress",
    "country": "United States",
  },
  {
    "name": "Kylie Jenner",
    "follower_count": 172,
    "description":
      "Reality TV personality and businesswoman and Self-Made Billionaire",
    "country": "United States",
  },
  {
    "name": "Kim Kardashian",
    "follower_count": 167,
    "description": "Reality TV personality and businesswoman",
    "country": "United States",
  },
  {
    "name": "Lionel Messi",
    "follower_count": 149,
    "description": "Footballer",
    "country": "Argentina",
  },
  {
    "name": "Beyoncé",
    "follower_count": 145,
    "description": "Musician",
    "country": "United States",
  },
  {
    "name": "Neymar",
    "follower_count": 138,
    "description": "Footballer",
    "country": "Brasil",
  },
  {
    "name": "National Geographic",
    "follower_count": 135,
    "description": "Magazine",
    "country": "United States",
  },
  {
    "name": "Justin Bieber",
    "follower_count": 133,
    "description": "Musician",
    "country": "Canada",
  },
  {
    "name": "Taylor Swift",
    "follower_count": 131,
    "description": "Musician",
    "country": "United States",
  },
  {
    "name": "Kendall Jenner",
    "follower_count": 127,
    "description": "Reality TV personality and Model",
    "country": "United States",
  },
  {
    "name": "Jennifer Lopez",
    "follower_count": 119,
    "description": "Musician and actress",
    "country": "United States",
  },
  {
    "name": "Nicki Minaj",
    "follower_count": 113,
    "description": "Musician",
    "country": "Trinidad and Tobago",
  },
  {
    'name': "Nike",
    "follower_count": 109,
    "description": "Sportswear multinational",
    "country": "United States",
  },
  {
    "name": "Khloé Kardashian",
    "follower_count": 108,
    "description": "Reality TV personality and businesswoman",
    "country": "United States",
  },
  {
    "name": "Virat Kohli",
    "follower_count": 555,
    "description": "Cricketer",
    "country": "India",
  },
  
  {
    "name": "Priyanka Chopra Jonas",
    "follower_count": 53,
    "description": "Actress and musician",
    "country": "India",
  }
]


#program to compare the followers of two accounts and guess which one has more followers and keep track of the score and display the score at the end of the game and if use gaues true then always a become b

print(logo)

def format_data(account):
  """Format account data into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Takes the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data) 

while game_should_continue:
  # Generate a random account from the data
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Give user feedback on their guess
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")