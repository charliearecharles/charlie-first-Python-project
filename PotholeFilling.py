"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *
def go_in():
    """
    pre condition:
    karel is at the upper left of the puthole, facing East
    post condition:
    Karel is in the puthole, facing South
    """
    turn_right()
    move()

def go_out():
    """
    pre condition:
    Karel is in the puthole, facing South
    post condition:
    karel is at the upper left of the puthole, facing North
    """
    turn_left()
    turn_left()
    move()
def main():
    pass
    for i in range(3):
        move()
        go_in()
        put_99()
        go_out()
        turn_right()
        move()
    """
        TODO:
        """


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
