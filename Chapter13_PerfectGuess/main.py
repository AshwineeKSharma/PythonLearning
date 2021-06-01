# WAP that generates the random number and ask the user to guess it.
# if the user guess higher than the actual number the program displays
# "Lower Number Please." and if the user guess it too low then the program 
# displays "Higher Number Please."  When a user guess the correct number, 
# the program displays the number of guesses the user used to reach at that Number.
# Hint---------------------> Use the random Module.-----------------------------



import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("D:\\Python Learning\\Chapter13_PerfectGuess\\hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("D:\\Python Learning\\Chapter13_PerfectGuess\\hiscore.txt", "w") as f:
        f.write(str(guesses))




