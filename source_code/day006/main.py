def turn_right():
    for _ in range(3):
        turn_left()


while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    elif right_is_clear():
        turn_right()
        move()
