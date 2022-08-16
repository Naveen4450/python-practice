#guess my number
import random
x=random.randint(1,20)
print("guess a number between 1 to 20")
for guesstaken in range(0,7):
    print("enter your guess")
    guess=int(input())

    if(x>guess):
        print("your guess is too low")
    elif (x<guess):
        print("your guess is too high")
    else:
        break
if (guess==x):
    print("good job you guessed my number in"+str(guesstaken)+"guesses")
else:
    print("better luck next time my guess is"+str(x))
