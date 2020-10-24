

import random

environment = ["Dirty", "Clean"]
perform = ["Cleaned", "Failed"]
score = 0
numberOfSimulation = input("Enter number of time for simulation: ")
i=0

while i < int(numberOfSimulation):
    print("Simulation:", i+1)
    state = random.choice(environment)
    if state == "Clean":
        score += 0
        print("The room was clean, 0 score added")
    else:
        action = random.choice(perform)
        if action == "Cleaned":
            score += 1
            print("the room was dirty and cleaned successfully. 1 score added.")
        else:
            score = score - 1
            print("the room was dirty and failed to clean. 1 score deducted")
    i = i+1


print("Total Score:", score)
