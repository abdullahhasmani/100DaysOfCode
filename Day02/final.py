print('Welcome to the tip calculator!')
InBill = float(input('What was the total bill?'))
PercentTip = int(input('How much tip would you like to give? 10, 12, or 15?'))
SplitPersons = int(input('How many people to split the bill?'))
Tip = InBill * PercentTip/100
TotalBill = Tip + InBill
SplitBill = round(TotalBill/SplitPersons,2)
print(f'Each person should pay: ${SplitBill}')