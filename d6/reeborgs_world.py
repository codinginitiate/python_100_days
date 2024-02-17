# hurdle #4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_north():
    while not is_facing_north():
        turn_left()

def face_east():
    face_north()
    turn_right()

def face_west():
    face_north()
    turn_left()

def face_south():
    face_north()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif turn_left():
        move()
