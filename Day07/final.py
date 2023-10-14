import random as rd

word_list =["ardvark","baboon","camel"]
mysteryWord = rd.choice(word_list)
n = len(mysteryWord)
answer= [0]*n
x=0
def printBlanks(inp):
    for x in range (0,n):
        if answer[x] ==0:
            if inp == mysteryWord[x] :
                answer[x]=mysteryWord[x]
                print(answer[x],end=' ')
            else :
                print("_",end=' ')
        else :
            print(answer[x],end=' ')
printBlanks([0]*n)
while x<5:
    guess = input("Enter your guess")
    if guess in mysteryWord:
        printBlanks(guess)
    else :
        x=x-1