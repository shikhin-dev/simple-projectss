# Number Guessing game
# Author: Unknown
# Description: A Simple Number Guessing Game 

import random

def playgame():
    print("welcome to the number guessing game\n" \
"You have 10 chances to guess the number")

    low=int(input("Choose the lower limit:"))
    high=int(input("Choose the higher limit:"))

    print("Welcome to the Number game!!\n" \
"You can guess between",low,"and",high,"\n" \
"Let's Start the Game!")

    rnum=random.randint(low,high)
    ch=8
    gus=1

    while gus<=ch:
        gnum=int(input(f"guess {gus}:"))
        if(gnum==rnum):
            print("Congrats You Guessed the number correct!\n" \
            "Total guess Taken=",gus)
            break
        elif(gnum<rnum):
            print("Too Low,Try a Higher Number")
        elif(gnum>rnum):
            print("Too high,Try a Lower Number")
        gus +=1
    if(gus>ch):
        print(f"Sorry You couldnt Guess the number\n" \
                f"The Number was {rnum}")

def main():
    while True:
        playgame()
        again=input("Do You want to continue Y/n ?").strip().lower()
        if(again!='y'):
            print("Thanks For Playing Our Game")
            break
if(__name__=="__main__"):
    main()