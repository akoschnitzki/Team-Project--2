# Name - Alexander and Vanessa
# Date- 11-3-21
# CSS- 225

# In this program, we were able to create a game that
# you have to try and guess the number. The program will let
# you know if you get the number or if you have to guess higher
# or lower. It allows you to keep playing until you do not want
# to play no more.


while True:
    import random

    num = random.randrange(1, 10)
    guess = int(input("Enter your number"))
    if guess == num:
        print("Hit, Well Done")

    else:
        if guess > num:
            print("Please Guess Lower")
        else:
            print("Please Guess Higher")

    guess = input("Enter your Number")
    if guess == num:
        print("Well done, you did it")
    else:
        print("That is not the right answer")

    print("Would You Like to guess again?")
    answer = input("Enter your option")
    if answer == "no":
        break
print("Thank you for Playing!!")

