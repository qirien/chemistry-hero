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
            mammoth "Well, when I ran at the building, I got knocked away by some force field. It's got to be really strong."
            mammoth "Maybe I could run less directly at the building? Or go at a different speed? Think it might help to charge faster?"
        "Are there any other obstacles in the way?":
            pc "Are there any other obstacles in the way?"
            mammoth "Well now that you mention it, it looks like there's a robot in there. It's probably waiting for me to get past the other defenses."
        "What else is around?":
            pc "What else is around?"
            mammoth "Well there's a few power poles, some cars, trash cans, and a little iron fence around the building."
        "What city is this in?":
            pc "What city is this in, anyway?"
            mammoth "Toronto."
        "Sounds frustrating.":
            pc "Man, that is so lame! You're probably really frustrated right now."
            mammoth "You have no idea. These guys just robbed a bank, and they're going to get away if I don't stop 'em."
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
