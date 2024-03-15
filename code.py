#Input user difficulty
import random

def angka():
    return random.randint(1, 101)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def lifepoint():
    if difficulty == 'easy':
        return 10 
    elif difficulty == 'hard':
        return 5
    
lives = lifepoint()
def compare(target, user):
    if target > user:
        return "Too Low"
    elif target < user: 
        return "Too High"
    elif target == user:
        return f'You guess right, the number is {user}'
number = angka()
game_over = False
while not game_over:
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    status = compare(number, guess)
    if status == "Too Low" or status == "Too High":
        lives -= 1
    print(status)
    if lives == 0:
        game_over = True
    elif number == guess:
        game_over = True
