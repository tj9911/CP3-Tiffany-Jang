# Note จิปาถะ

###########Code by gu#################

userPocket= int(input("How much you got? :"))
ticketPrice= int(input("How much for the ticket? :"))
if userPocket >= ticketPrice:
   print("You can buy the ticket!")
want = int(input("How many ticket you want to buy? :"))
wantPrice = want*ticketPrice
print("You want to buy: ", want, "ticket")
print("Total Ticket Price is: ",wantPrice)
if wantPrice > userPocket:
   print("Sorry, You have not enough money to buy ticket.")
if wantPrice < userPocket:
   print("Your purchase has succesfully done!")
balance=userPocket-wantPrice
print("Your balance is: ", balance)

########## This is clean code from OpenAi ##########

userPocket = int(input("How much you got? :"))
ticketPrice = int(input("How much for the ticket? :"))

if userPocket >= ticketPrice:
    print("You can buy the ticket!")
    
    want = int(input("How many tickets do you want to buy? :"))
    wantPrice = want * ticketPrice

    print(f"You want to buy: {want} ticket")
    print(f"Total Ticket Price is: {wantPrice}")

    if wantPrice > userPocket:
        print("Sorry, You don't have enough money to buy the ticket.")
    else:
        print("Your purchase has been successful!")
        balance = userPocket - wantPrice
        print(f"Your balance is: {balance}")
else:
    print("Sorry, you don't have enough money to buy the ticket.")
