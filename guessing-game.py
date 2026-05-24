from random import randint
# computer picks a random number and you pick and the program will tell whether its high or low.
comp_pick = randint(1,100)
guess = int(input("guess a number between 1 to 100 : "))
attempts = 1
while comp_pick != guess:
    Difference = abs(comp_pick - guess)
    print("Wrong")
    if Difference <= 3:
        print("Extremely close🔥")
    elif Difference <= 9:
        print("close")
    elif Difference <= 20:
        print("Near")
    elif guess > comp_pick:
        print("Very high")
    else:
        print("Very Low")
    attempts += 1
    guess = int(input("Try again :"))
print("You got it in",attempts,"attempts🔥")