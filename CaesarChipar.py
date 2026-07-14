logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(original_text, Shift_Value, Encode_or_decode):
    final_msg = ""
    if Encode_or_decode == "decode":
        Shift_Value *= -1

    for char in original_text:
        if char not in alphabet:
            final_msg +=char
        else:
           
            Shift_values = alphabet.index(char) + Shift_Value
            Shift_values %= len(alphabet)
            final_msg += alphabet[Shift_values]
    print(f"Here is the {Encode_or_decode}d result: {final_msg}")

Shuold_more = True

while Shuold_more:
    #take all the needs here
    YourNeed = input("What you want to do?\n For encrypt, type'encode' and For decrypt, type'decode': ").lower()
    msg = input("Type your msg here: ").lower()
    ShiftNumber = int(input("Enter the shift number, you want: "))

    caesar(original_text = msg, Shift_Value = ShiftNumber, Encode_or_decode = YourNeed)

    againFor = input("If you want again to decode or encode your text, please type'yes'. Otherwise type 'no'")

    if againFor == "no":
        Shuold_more = False
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Hey! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Thank you, GoodBye!")


