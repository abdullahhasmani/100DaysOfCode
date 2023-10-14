age = input("What is your current age? ")

months = (90-int(age)) *12
days = (90-int(age))*365
weeks = days//7
print(f'You have {days} days, {weeks} weeks, and {months} months left.')