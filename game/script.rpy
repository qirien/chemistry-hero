# Chemistry Hero
#

# For definitions of variables, characters, etc, see definitions.rpy

# The game starts here.
label start:

    $ input_text = renpy.input("Your Name:", default="Jay")
    $ player_name = input_text or "Jay"

    call episode1
    
    return
