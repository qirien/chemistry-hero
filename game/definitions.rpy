init -1:

    #
    # VARIABLES
    #
    define player_name = "Jay"
    
    #
    # CHARACTERS
    #
    define teacher = Character('Teacher', color="#c8ffc8")
    define entire_class = Character("Class")
    define phone = Character("Phone")
    define mammoth = Character("The Mammoth")

    define pc = DynamicCharacter("player_name", color="#84b766")
    define bernard = Character("Bernard")

    
    #
    # BACKGROUNDS
    #
    image bg classroom = "bg/classroom.jpg"
   
    #
    # SPRITES
    #
    
    # Automatically import all sprites in the 'sprites' subdirectory 
    # Thanks JinzouTamashii, http://www.renpy.org/wiki/renpy/doc/cookbook/Automatically_Defining_Images    
init python:
    import os
    for fname in os.listdir(config.gamedir + '/sprites'):
        if fname.endswith(('.jpg', '.png')):
            tag = fname[:-4]
            fname =  'sprites/' + fname
            renpy.image(tag, fname)

    #
    # POSITIONS
    #
    define.move_transitions('move', 0.5)
    define.move_transitions('quickmove', 0.25)    
init -1:
    define midleft = Position(xpos=0.35, xanchor=0.5)        
    define midright = Position(xpos=0.65, xanchor=0.5)
    define quarterleft = Position(xpos=0.22, xanchor=0.5)
    define quarterright = Position(xpos=0.78, xanchor=0.5)
    define farleft = Position(xpos=-0.30, xanchor=0)
    define farright = Position(xpos=1.0, xanchor=0)    
    define sitting = Position(ypos=0.45, yanchor=0)
    define squatting = Position(ypos=0.25, yanchor=0)
    define standing = Position(ypos= 1.0, yanchor = 1.0)
    
    # 
    # TRANSITIONS
    #
    define punch_long = Move((20, 15), (-20, -15), .10, bounce=True, repeat=True, delay=1.5)
    define vpunch_long = Move((0, 15), (0, -15), .10, bounce=True, repeat=True, delay=1.5)
    define hpunch_long = Move((20, 0), (-20, 0), .10, bounce=True, repeat=True, delay=1.5)
    
    define fade = Fade(0.3, 0.3, 0.3) # TODO: Tweak these times for our game?
    define slowfade = Fade(0.5, 0.5, 0.5)
    define veryslowfade = Fade(2.0, 0.5, 2.0)
    define flash = Fade(.25, 0, .75, color="#fff")
    define magic_flash = Fade(.25, 0, .75, color="#acf")
    define red_flash = Fade(.25, 0, .75, color="#a90000")
    define golden_flash = Fade(.25, 0, .75, color="#f9a900")
    define blood = Fade(.25, 0, .25, color="#f00")
    define dissolve = Dissolve(0.4, alpha=True)
        
    transform exit_left:
        linear 3.0 xpos -600
        
    transform exit_right:
        linear 3.0 xpos +600
        
    transform hop:
        yalign 0.0
        linear 0.5 ypos +30
        pause 0.5
        linear 0.5 ypos 0
        repeat

    transform basicfade:
        on show:
            linear 0.5 alpha 1.0
#        on hide:
#            linear 0.5 alpha 0.0
#        on replace:
#            linear 0.5 alpha 1.0
        on replaced:
            linear 0.5 alpha 0.0        
    
    #
    # MUSIC
    # 
