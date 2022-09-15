# import randint from random module
from random import randint

# declaration variables for counting and storing scores
computer_wins = 0
user_wins = 0
rk = 0
pr = 0
sr = 0
t = 0

while True:
    choice = ["r", "p", "s"]
    # computer will choice any random weapon from predefined choice
    computer = choice[randint(0, 2)]
    print("")
    print("\tWelcome to Rock,Paper,Scissor Game\n")
    print("\tROCK(R,r),PAPER(P,p) OR SCISSOR(S,s)\n")
    # take the input from user and convert it into lowercase
    user = input("Your Choice : ").lower()
    # if user enter invalid input
    if user not in choice:
        print("Invalid Entry,make Another Choice")
        continue
    print("Computers choice :" + computer)

    if user == computer:
        print("\ntie")
        t += 1

    # conditions for program main loop
    elif user == "r" and computer == "s":
        print("\nyou win")
        # if user wins,user_wins variable will increase by 1
        user_wins += 1
    elif user == "s" and computer == "p":
        print("\nyou win")
        user_wins += 1
    elif user == "p" and computer == "r":
        print("\nyou win")
        user_wins += 1
    # conditions for computer winning

    elif user == "s" and computer == "r":
        print("\ncomputer wins ")
        computer_wins += 1
    elif user == "p" and computer == "s":
        print("\ncomputer wins")
        computer_wins += 1
    elif user == "r" and computer == "p":
        print("\ncomputer wins")
        computer_wins += 1
    # Printing either you or computer wins or tie
    print("\n")
    print("player   :", user_wins)
    print("computer :", computer_wins)
    print("tie :", t)
    # store how many times user used rock,paper and scissor
    # for each game it will increase by 1
    if user == "r":
        rk += 1
    elif user == "p":
        pr += 1
    elif user == "s":
        sr += 1
    # print how many times weapons have been used
    print("\nYou used Rock ", rk, " times")
    print("\nYou used Scissor ", sr, " times")
    print("\nYou used Paper ", pr, " times")
    print("\npress 'Enter' to continue or (Q/q) to quit the game")
    # if user input Q or q the game will stop And print the line
    answer = input()
    if answer == 'q' or answer == 'Q':
        print("Thanks for playing")
        break
    # or else the game will continue
    else:
        continue
    # if user wins 5 to 9 times
if user_wins < randint(5, 9):
    # compare the number of times the user selected each weapon
    if rk > pr and rk > sr:
        # if user used rock more than times of paper and scissor used
        # computer will select rock as preferred weapon
        computer = choice[0]
    elif pr > rk and pr > sr:
        # if user used paper more than times of rock and scissor used
        # computer will select paper as preferred weapon
        computer = choice[1]
    elif sr > rk and sr > pr:
        # if user used scissor more than times of rock and paper used
        # computer will select scissor as preferred weapon
        computer = choice[2]
        # else computer will choose random weapon
    else:
        computer = choice[randint(0, 2)]
