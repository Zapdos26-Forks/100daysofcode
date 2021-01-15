from game_data import data
import random
from art import logo, vs
from replit import clear


def get_random_account():
    return random.choice(data)


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(
            f"Compare A: {account_a['name']}, a { account_a['description']}, from { account_a['country']}.")
        print(vs)
        print(
            f"Against B: {account_b['name']}, a { account_b['description']}, from { account_b['country']}.")

        while True:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if guess in ['a', 'b']:
                break
            print('Not a valid input')
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == '__main__':
    game()
