from random import randint

difficulty_turns = {'easy': 10, 'hard': 5}


def check_answer(guess, answer, turns):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return
    elif guess > answer:
        print("Too high.")
    else:
        print("Too low.")
    return turns - 1


def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level in difficulty_turns.keys():
            return difficulty_turns[level]
        print('Not a valid difficulty')


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif turns == None:
            return
        print("Guess again.")


if __name__ == '__main__':
    game()
