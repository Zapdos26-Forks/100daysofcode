import random


def game():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    images = [rock, paper, scissors]

    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        return
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{images[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")
        return
    if (computer_choice == 0 and user_choice == 2):
        print('You lose')
        return
    if (user_choice == 0 and computer_choice == 2) or user_choice > computer_choice:
        print("You win!")
        return
    print("You lose")


if __name__ == "__main__":
    game()
