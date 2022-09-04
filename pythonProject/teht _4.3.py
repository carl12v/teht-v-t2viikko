UserInput = input("Sano luku: ")
maxValue = minValue = int(UserInput)

while UserInput != "":
    UserInputInt = int(UserInput)
    if UserInputInt < minValue:
        minValue = UserInputInt
    if UserInputInt > maxValue:
        maxValue = UserInputInt
        UserInput = input("Sano luku: ")
print(f"Pienin arvo: {minValue}, suurin arvo: {maxValue}")