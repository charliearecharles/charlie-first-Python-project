"""
File: StepUp.py
Name: CHARLIE
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *
def turn_right():
    """
    pre condition:
    facing North
    post condition:
    facing East
    """
    turn_left()
    turn_left()
    turn_left()

def main():
    pass
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    move()
    put_99()
    move()

def put_99():
    """
        pre condition:
        no beeper
        post condition:
        99 beeper
        """
    for i in range(99):
        put_beeper()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
