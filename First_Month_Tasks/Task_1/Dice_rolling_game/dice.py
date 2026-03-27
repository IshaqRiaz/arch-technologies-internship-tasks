import random
again = True
count = 0   # Counter to track number of rolls
while again:
    # Input validation for number of dice
    try:
        num = int(input("How many dice do you want to roll?: "))
        if num <= 0:
            print("Please enter a number greater than 0.\n")
            continue
    except:
        print("Invalid input! Please enter a number.\n")
        continue
    print("Rolling dice...")
    # Loop to roll multiple dice
    for i in range(num):
        print("Dice", i+1, ":", random.randint(1, 6))
    count += 1   # Increase roll count
    another_roll = input("Do you want to roll dice again y/n?: ")
    if another_roll.lower() == "y":
        continue
    else:
        print("You are quitting the game, Game Closed!")
        print("Total times you rolled the dice:", count)
        break
