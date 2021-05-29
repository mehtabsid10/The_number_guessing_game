import random


randnum=random.randint(1,100)
guesses=0
userguess=0
while(randnum != userguess):
    try:
        userguess=int(input("Enter your guess :"))
        guesses+=1 
        if(randnum < userguess):
            if(userguess - randnum  <= 10):
                print("You are close. guess a slight smaller number.", end="")
                
            else:
                print("Enter smaller number :", end="")

        elif (randnum==userguess):
            print(f"You guessed the right number in {guesses} attempt.")
                
        else:
            if(randnum - userguess <= 10):
                print("You are close. Enter a slightly bigger number :", end="") 
                
            else:
                print("Enter bigger number :", end="") 
    except Exception as e:
        print("You have entered the invalid input :", e)

#file operation to store the high score

with open ("highscore.txt", "r") as f:
    hiscore = int(f.read())

if (hiscore > guesses ):
    print("You just broke the high score.")
    with open("highscore.txt", "w") as f: 
        f.write(str(guesses))