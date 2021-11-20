import random

dice_simulation = True

while dice_simulation:
    dice_another_roll = input("Want to roll this dice again? (Yes / No) ")
    if dice_another_roll.capitalize() == "Yes":
        print(random.randint(1, 6))
        continue
    else:
        break