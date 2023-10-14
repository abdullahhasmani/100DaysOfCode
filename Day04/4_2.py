import random as rd

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#x = rd(0,len(names)-1)
#using random.choice
x=rd.choice(names)
print(f'{x} is going to buy meal today!')