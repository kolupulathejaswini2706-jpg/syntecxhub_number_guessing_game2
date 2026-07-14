import random
print("welcome to number guessing game!")
secret_number=random.randint(1,100)
attempts=0
while True:
    guess=int(input("enter your guess(1-100):"))
    attempts += 1
    if guess<secret_number:
        print("too low! try again")
    elif guess>secret_number:
        print("too high! try again")    
    else:
        print("congratulations!")
        print("you guessed the number in",attempts,"attempts(s).")
        break    