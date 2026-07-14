alphabet = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#take all the needs here
YourNeed = input("What you want to do?\n For encrypt, type'encode' and For decrypt, type'decode': ").lower()
msg = input("Type your msg here: ").lower()
ShiftNumber = int(input("Enter the shift number, you want: "))

def encode(msg, ShiftNumber):
    final_msg = ""
    for char in msg:
        Shift_value = alphabet.index(char) + ShiftNumber
        Shift_value %= len(alphabet)
        final_msg += alphabet[Shift_value]
    print(final_msg)

def decode(msg, ShiftNumber):
    final_msg = ""
    for char in msg:
        Shift_value = alphabet.index(char) - ShiftNumber
        Shift_value %= len(alphabet)
        final_msg += alphabet[Shift_value]
    print(final_msg)

if YourNeed == "encode":
    encode(msg, ShiftNumber)
else:
    decode(msg, ShiftNumber)

