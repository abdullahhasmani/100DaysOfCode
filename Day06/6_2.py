def prime_checker(number):
    for x in range(2,number//2+1):
        if(number % x ==0):
            print("It's not a prime number.")
            return
    print("It's a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)
