# Chemistry Hero
#

# Declare characters used by this game.
define teacher = Character('Teacher', color="#c8ffc8")
define entire_class = Character("Class")
define phone = Character("Phone")

define pc = DynamicCharacter("player_name", color="#84b766")
define smug_nerd = Character("Smug Nerd")


# Define other variables
define player_name = "Jay"

# The game starts here.
label start:

    $ input_text = renpy.input("Your Name:")
    $ player_name = input_text or "Jay"

    call episode1
    
    return
