label episode1:
    scene bg classroom
    
    teacher "Time to get started! Students, please take out your textbooks and open to page 16."
    entire_class "*groan*"
    teacher "We’re going to talk about the scientific method today, what it is and how to…"
    phone "Riiiiiiing!" # TODO: Add sfx
    "While our teacher answered the phone, the class started chatting."
    bernard "Didn’t everyone learn about this in Junior High? I don’t get why he thinks he needs to teach it again."

    menu: 
        "I know.":
            pc "I know! Blah blah, scientific method, blah blah, hypothesis, control, results, and so on!"
        "Well, it is important...":
            pc "The scientific method is the basis for all science. It makes sense to review it every so often."
            pc "Without proper controls and experiment design, your data means nothing."

    teacher "[player_name] and Bernard? Come up here for a moment."
    teacher "We have a gamma-level situation. Since you're confident enough to chat during class, you two can advise our hero on what to do."
    bernard "I can handle a gamma; I've been ready for months!"
    teacher "We'll see. I'll be ready to step in if you screw it up. You'll be working with Mammoth. He's got super strength and is very gullible, so he'll try anything you suggest."
    
    mammoth "Hello? Are you my advisor?"
    
    menu:
        "Yes, that's me.":
            pc "Yes, sir! What seems to be the problem?"
        "Isn't Bernard the advisor?":
            pc "Uhmmm..."
            bernard "Yeah we're here. Go ahead and tell us what's going on."
    
    
    mammoth "I chased some evil minions to the building they're using as a hideout, but I can't get in."
    mammoth "There's a force field blocking me from getting too close, and they have weapon that pushes me away when I try. I'm stuck."
    
    menu:
        "Let's think about this.":
            pc "Let's think about what you could do differently."
        "Are there any other obstacles in the way?":
            pc "Are there any other obstacles in the way?"
        "What else is around?":
            pc "What else is around?"
        "What city is this in?":
            pc "What city is this in, anyway?"
        "Sounds frustrating.":
            pc "Man, that is so lame! You're probably really frustrated right now."
        "I have no idea what to do.":
            pc "I have no idea what to do. Bernard, do you have any ideas?"
            bernard "Pfft. You didn't even try. Mammoth, are there any other entrances?"
            mammoth "Maybe...? There's not any other doors."
            bernard "How about windows?"
            mammoth "Oh yeah, there's lots of windows, but they're all up high."
            bernard "Use your super strength to pick up a dumpster or a truck or something and climb on top of it to get in the window."
            mammoth "I don't see any dumpsters or trucks. Just little trash cans and cars."
            bernard "Can you stack those up?"
            
    
    
    
    return
