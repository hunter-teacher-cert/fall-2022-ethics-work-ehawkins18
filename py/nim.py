# filename: nim.py
# Ed Hawkins
# CSCI 77800 Fall 2022
# collaborators: me, myself, I
# consulted: ThinkPython
#
# Game of Nim
#
from random import random
stones = 12
stonesTaken = 0
# loop until game ends
while (stonesTaken < stones) :
    print("Number of stones to take: ")
    nStones = input()
    numStones = int(nStones)
    stonesTaken += numStones
    print("Number of stones remaining: " + str((stones - stonesTaken)))
    # check for win
    if (stonesTaken >= stones) :
        print("User wins!")
        break
    # machine turn
    #r =  java.util.Random()
    numStones = int(3 * random() + 1)
    print("Computer takes " + str(numStones) + " stones.")
    # calc number of stones remaining and print
    stonesTaken += numStones
    print("Number of stones remaining: " + str((stones - stonesTaken)))
    # check for win
    if (stonesTaken >= stones) :
        print("Computer wins!")
        break
print("Game over!")