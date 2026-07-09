NumLetters = int(input("How many letters you would like to use in your password?\n"));
SymNumbers = int(input("How many symbols you would like to use in your password?\n"));
NumOfNum = int(input("How many numbers you would like to use in your password?\n"));

latters = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M',
]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '_', '-', '+', '=',
    '[', ']', '{', '}', '|',
    ';', ':', ',', '.',
    '<', '>', '/', '?', '~'
]
numbers =['0','1','2','3','4','5','6','7','8','9']

import random;

passwords =""

for i in range(0, NumLetters):
    passwords = passwords+(random.choice(latters))

for i in range(0, SymNumbers):
    passwords = passwords +(random.choice(symbols))

for i in range(0, NumOfNum):
    passwords = passwords + (random.choice(numbers))

print("Yours easy and first lavel password is : " + passwords)

pass_lists = []
for i in range(0, NumLetters):
    pass_lists.append(random.choice(latters))

for i in range(0, SymNumbers):
    pass_lists.append(random.choice(symbols))

for i in range(0, NumOfNum):
    pass_lists.append(random.choice(numbers))

random.shuffle(pass_lists)

finalPassword = ""
for eachchar in pass_lists:
    finalPassword += eachchar

print(f"Finally the hardest password is : {finalPassword}")