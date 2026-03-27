import random
number = random.randint(1, 10)

attempt = input("I'll pick a random number, and you'll try guessing it! ")
attempt = int(attempt)

if attempt > 10 or attempt < 1:
    print ("You're supposed to pick between 1 and 10 ")

elif attempt == number:
    print ("Correct ")

elif attempt > number:
    print ("Your guess is too high") 
    
else:
    print ("Your guess is too low") 
