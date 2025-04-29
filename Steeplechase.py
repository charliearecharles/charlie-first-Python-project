"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre condition: Karel is on the left side of the wall, face East
    Post condition: Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    Pre condition: Karel is on the left side of the wall, face East
    Post condition: Karel is on upper right of the wall
    """
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    #alternative:
    #while not front_is_clear():
    #    turn_left()
    #    move()
    #   turn_right()


def cross():
    """
    Pre condition: Karel is on upper right of the wall
    Post condition: Karel is on upper left of the wall
    """
    move()
    turn_right()


def down():
    move()
    while front_is_clear():
        move()
    turn_left()




def turn_right():
    """
    Pre condition: Karel face North
    Post condition: Karel face East
    """
    turn_left()
    turn_left()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
