# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

Bill=0
if size=='S':
    Bill+=15
    if add_pepperoni=='Y':
        Bill+=2
else:
    Bill +=20
    if add_pepperoni=='Y':
        Bill+=3
    if size=='L':
        Bill+=5
if extra_cheese=='Y':
    Bill+=1
print(f'Your final bill is: ${Bill}.')