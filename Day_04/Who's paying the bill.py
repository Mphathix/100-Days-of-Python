import random

names = input("Enter everybody's names, separated by a comma. ").split(",")

name = random.choice(names)
print(f"{name} is going to pay the bill today!")
