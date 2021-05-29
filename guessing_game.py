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

#file operation to get the previous highscore.

with open ("highscore.txt", "r") as f:
    strhiscore = (f.read())
    hiscorelist =[int(i) for i in strhiscore.split() if i.isdigit()]
    hiscore=hiscorelist[0]

if (hiscore >= guesses ):
    print("You just broke the high score. Enter your name to update highscore: ")
    name=input()
    with open("highscore.txt", "w") as f: 
        f.write(str(f" {name} is the high scorer with a score of {guesses}"))