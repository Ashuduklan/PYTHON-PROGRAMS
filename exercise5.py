# snake water gun
s = "snake"
w = "water"
g = "gun"
import random
myli= ["Snake", "Water", "Gun"]
# b = random.choice(myli)
# n= input("Choose between s,w and g \n")
i = 1
y = 0
c = 0
while(i<10):
    n = input("Choose between s,w and g \n")
    b = random.choice(myli)
    i=i+1
    chances = 10-i
    print("Your Remaining Chances:", chances)
    print("computer send=", b)

    if(n== "s"):
        if(b=="Snake"):
            print("Match draw play again \n")
        elif(b=="Water"):
            print("Hurray you won the match \n")
            y = y+2
            c = c-1
        else:
            print("Oops! you lost the match \n")
            y = y-1
            c = c+2

    elif (n == "w"):
        if (b == "Snake"):
            print("Oops! you lost the match \n")
            y = y - 1
            c = c + 2
        elif (b == "Water"):
            print("Match draw play again \n")
        else:
            print("Hurray you won the match \n")
            y = y + 2
            c = c - 1

    elif (n == "g"):
        if (b == "Snake"):
            print("Hurray you won the match\n")
            y = y + 2
            c = c - 1
        elif (b == "Water"):
            print("Oops! you lost the match \n")
            y = y - 1
            c = c + 2
        else:
            print("Match draw play again \n")
    continue
print("Your final score is: ", y)
print("Computer final score is: ", c)
print("Thanks for playing with us")

