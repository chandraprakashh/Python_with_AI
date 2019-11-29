# Tower of Hanoi(TOH) Problem in Python
#Recursive Tower of Hanoi Problem in Python for 3Pegs & user defined Disks

"""The rules of the game are very simple, but the solution is not so obvious. 

The game "Towers of Hanoi" uses three rods. 

A number of disks is stacked in decreasing order from the bottom to the top of one rod,

i.e. the largest disk at the bottom and the smallest one on top. The disks build a conical tower.

Amount of movements to find the solution of the Hanoi Tower puzzle: it is 2^n -1.e.g. for 3 disks, 9-1=8 

& for 4 disks, 16-1=15 moves

The aim of the game is to move the tower of disks from one rod to another rod.

The following rules have to be obeyed:

*Only one disk may be moved at a time.

*Only the most upper disk from one of the rods can be moved in a move

*It can be put on another rod, if this rod is empty or if the most upper disk of 

this rod is larger than the one which is moved.
"""



def hanoi(ndisks, startPeg=1, endPeg=3):

    if ndisks:

        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)

        print("Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))

        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

 

hanoi(ndisks=3)

#Change the value of ndisks and get the results.