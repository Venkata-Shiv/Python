import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry! Try again, number is too small")
        elif guess > random_number:
            print("Sorry! Try again, number is too large")

    print(f'yay congrats! you guessed the number {random_number} correctly ')


guess(10)
