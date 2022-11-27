import random
import time

print("Hello Buddy !!\\nLet's play a Game. It is called as a Dice game.")
print("You Enter a Number , I will roll the dice.\nif both matches , You will get 5 points.")
print("Lets GET STARTED ")

score = 0
while(True):
    print("Enter a number between 1 and 6")
    print("Enter 0 to exit ")
    inp_num = int(input())
    if(inp_num==0):
        print("Game Over ")
        break 
    elif(inp_num > 6 or inp_num < 1):
        print("Invalid User Input ")
        continue 
    print("Rolling the dice....")
    time.sleep(2)
    rand_num=random.randint(1,6)
    print("Dice generated :", rand_num)
    if(inp_num==rand_num):
        score=score+5
        print("Both number Matched")
    else:
        print("LOL... It did not match ...Try Again")
    print("score: ",score)