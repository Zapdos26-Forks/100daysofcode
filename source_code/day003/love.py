import re

print("Love Calculator")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()
true_score = len(re.findall('[true]', name1 + name2))
love_score = len(re.findall('[love]', name1 + name2))
score = int(str(true_score) + str(love_score))
if score < 10 or score > 90:
    print(f'Your score is {score} , you go together like coke and mentos.')
elif score < 50 and score > 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
