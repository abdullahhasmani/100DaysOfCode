import os

def declareWinner():
    maxBid=0
    maxBidder=''
    for x in biddersList:
        if biddersList[x]>maxBid:
            maxBid = biddersList[x]
            maxBidder=x
    print(f"The winner is {maxBidder} with a bid of ${maxBid}")

takingBids=True
biddersList={}
print("Welcome to the secret auction program.")

while (takingBids == True):
    name=input("What is your name? :")
    amount=int(input("What's your bid? :"))
    isNext = input("Are there any other bidders? Type 'yes' or 'no'.")
    biddersList[name]=amount
    if isNext == 'no':
        takingBids = False
    os.system("clear")
declareWinner()
