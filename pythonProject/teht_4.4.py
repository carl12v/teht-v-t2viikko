import random
attempts = 0
secret_number = random.randint(1,10)
isCorrect = False
guess = int(input("Arvaa: "))

while secret_number != guess:
    if guess < secret_number:
        print("Korkeampi...")
        guess = int(input("Arvaa: "))
        attempts+= 1
    elif guess > secret_number:
        print("Alempi...")
        guess = int(input("Arvaa: "))
        attempts+= 1
    else:
        print("\nArvasit oikein numero oli " ,secret_number)