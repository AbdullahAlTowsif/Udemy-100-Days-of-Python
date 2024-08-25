import random
from art import logo
print(logo)
print("Welcome to the NUMBER GUESSING GAME!")

print("I'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1,100)
print(f"Pssst, the correct answer is {correct_answer}")

opinion = input("Choose a difficulty. Type 'easy' or 'hard': ")

if opinion == 'easy':
    attempt = 10
    print(f"You have {attempt} attempts remaining to guess the number.")
    while(attempt):
        guess = int(input("Make a guess: "))
        if guess > correct_answer:
            print("Too high")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif guess < correct_answer:
            print("Too low")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer is {correct_answer}")
else:
    attempt = 5
    print(f"You have {attempt} attempts remaining to guess the number.")
    while(attempt):
        guess = int(input("Make a guess: "))
        if guess > correct_answer:
            print("Too high")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif guess < correct_answer:
            print("Too low")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer is {correct_answer}")