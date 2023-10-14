import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

userChoice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerChoice = rd.randint(0,2)
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("User Choice:")
    print(game_images[userChoice])
    print("Computer Choice:")
    print(game_images[computerChoice])
    if(userChoice==computerChoice):
        print("Its a draw.")
    elif(userChoice == 0 and computerChoice==1):
        print("you win!")
    elif(userChoice == 1 and computerChoice==2):
        print("you win!")
    elif(userChoice == 2 and computerChoice==0):
        print("you win!")
    else:
        print("You lose.")
