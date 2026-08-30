import random
number = random.randint(1, 10)

def check_guess(attempt, number):
    if attempt > 10 or attempt < 1:
        print ("You're supposed to pick between 1 and 10 ")
    elif attempt == number:
        print ("Correct ")
    elif attempt > number:  
        print ("Your guess is too high") 
    else:
        print ("Your guess is too low") 

try:
    attempt = int(input("I'll pick a random number, and you'll try guessing it: "))
except ValueError:
    print("Error")
else:
    check_guess(attempt, number)
finally:
    print("Program finished.")
