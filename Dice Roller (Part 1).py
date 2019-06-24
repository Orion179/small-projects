#Dice Roller is designed to repeat the set die type until user restarts program, but will ask for different die amounts after initial roll
from random import randint
#Setting up while loop for dice
repeat = True
die_type = input("Which die will you roll with: ")

#Sets up die roll process
while repeat:
    if die_type== "d4" or "D4" or 4:
        die_number = input("How many dice?: ")
        print("You Rolled: ",randint(1,int(die_number)*4))
    elif die_type== "d6" or "D6" or 6:
        die_number = input("How many dice?: ")
        print("You Rolled: ",randint(1,int(die_number)*6))
    elif die_type== "d8" or "D8" or 8:
        die_number = input("How many dice?: ")
        print("You Rolled: ",randint(1,int(die_number)*8))
    elif die_type== "d10" or "D10" or 10:
        die_number = input("How many dice?: ")
        print("You Rolled: ",randint(1,int(die_number)*10))
    elif die_type== "d12" or "D12" or 12:
        die_number = input("How many dice?: ")
        print("You Rolled: ",randint(1,int(die_number)*12))
    elif die_type== "d20" or "D20" or 20:
        die_number = input("How many dice?: ")
        print("You Rolled: ",randint(1,int(die_number)*20))