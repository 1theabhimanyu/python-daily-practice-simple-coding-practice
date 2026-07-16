print("""

                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\

""")

print("\n" *2)

def Find_Max_bid (bidder_dict):
  winner = ""
  highest_bid = 0

  for person in bidder_dict:
    amounts = bidder_dict[person]
    if amounts > highest_bid:
      highest_bid = amounts
      winner = person

  print(f"The winner of this Auction is {winner} with amount ${highest_bid}")

bids ={}
should_continues = True

while should_continues:
  name = input("What's your name? :")
  price = int(input("Add amount you want to bid: $"))
  bids[name] = price
  isMoreBidder = input("Is there someone to bid, please type 'yes' or 'no'.").lower()

  if isMoreBidder == 'no':
    should_continues = False
    Find_Max_bid(bids)
  elif isMoreBidder == 'yes':
    print("\n" * 100)
    print("Thank you! Please continue")
