from turtle import Turtle, Screen
import random


def continue_race(all_turtles, user_bet):
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            color = turtle.pencolor()
            if color == user_bet:
                print(
                    f"You've won! The {color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {color} turtle is the winner!")
                return False
        turtle.forward(random.randint(0, 10))

    return True


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=500, height=400)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    while True:
        user_bet = screen.textinput(
            title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
        if user_bet in colors:
            break
        print('Invalid input')
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    # Create 6 turtles
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    while continue_race(all_turtles, user_bet):
        pass

    screen.exitonclick()
