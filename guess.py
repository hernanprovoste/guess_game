# This is a Guess the Number game.
import random

guessesTaken = 0

myName = input("Hello! Whats is your name?\n")

number = random.randint(1, 20)
print(f'Well, {myName}, I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    guess = int(input('Take a guess.\n'))

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(f"Good job, {myName}!! You guessed my number in {guessesTaken} guesses!")

if guess != number:
    number = str(number)
    print(f"Nope, The number I was thinking of was {number}.")