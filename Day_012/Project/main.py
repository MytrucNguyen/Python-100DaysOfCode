import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

easy = 10
hard = 5


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == 'easy':
        print (f"You have {easy} lives. Good luck!")
        return easy
    else:
        print (f"You have {hard} lives. Good luck!")
        return hard

def checking(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You win! The answer was {answer}")

def game():
    answer = random.randint(1,101)
    turns = difficulty()

    guess = 0
    while guess != answer:
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print(f"You have {turns} turns left")
        guess = int(input("Make a guess: "))

        turns = checking(guess, answer, turns)
        if turns == 0:
            print("You loose")
            return 
        elif guess != answer:
            print("Guess again")
game()
