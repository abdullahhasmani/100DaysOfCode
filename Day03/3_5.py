print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

st = name1+name2
st= st.lower()
true=st.count('t')+st.count('r')+st.count('u')+st.count('e')
love=st.count('l')+st.count('o')+st.count('v')+st.count('e')
score = (10*true)+love


if(score<10 or score>90):
    print(f'Your score is {score}, you go together like coke and mentos.')
elif(score>40 and score<50):
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')