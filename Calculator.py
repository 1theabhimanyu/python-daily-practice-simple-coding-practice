logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

"""

def add (n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

def Calculator():
    num1 = float(input("What is your First Number?: "))
    should_continues = True

    while should_continues:
        operators = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }

        for op in operators:
            print(op)
        cal_need = input("Pick a operations: ")
        num2 = float(input("enter your second number: "))

        results = operators[cal_need](num1, num2)
        print(f"{num1} {cal_need} {num2} = {results}")

        continue_operations = input(f"Type 'y', if you want to continue operations with {results}, otherwise type 'n': ")

        if continue_operations == 'y':
            num1 = results
        else:
            should_continues = False
            print("\n" * 100)
            next_work = input("If youn want to continue new calculation type, 'y', otherwise type 'n': ")
            if next_work == 'y':
                Calculator()
            else:
                print("Thank You")


Calculator()
