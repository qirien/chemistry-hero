label episode1:
    
    teacher "Time to get started! Students, please take out your textbooks and open to page 16."
    entire_class "*groan*"
    teacher "We’re going to talk about the scientific method today, what it is and how to…"
    phone "Riiiiiiing!" # TODO: Add sfx
    "While our teacher answered the phone, the class started chatting."
    smug_nerd "Didn’t everyone learn about this in Junior High? I don’t get why he thinks he needs to teach it again."

    menu: 
        "I know.":
            pc "I know! Blah blah, scientific method, blah blah, hypothesis, control, results, and so on!"
        "Well, it is important...":
            pc "The scientific method is the basis for all science. It makes sense to review it every so often."
            pc "Without proper controls and experiment design, your data means nothing."

    teacher "[player_name] and Bernard? Come up here for a moment."
    teacher "We have a gamma-level situation. Since you're confident enough to chat during class, you two can advise our hero on what to do."
    smug_nerd "I can handle a Gamma; I've been ready for months!"
    teacher "We'll see. I'll be ready to step in if you screw it up. "
    
    mammoth "Hello? Are you my advisor?"
    
    menu
        "Yes, that's me."
            pc "Yes, sir! What seems to be the problem?"
        "Uhhhhh, I think Bernard is."
            pc "Uhmmm..."
            smug_nerd "Yeah we're here. Go ahead and tell us what's going on."
    
    
    mammoth "I chased some evil minions to the building they're using as a hideout, but I can't seem to get in."
    mammoth "There's a force field blocking me from getting too close, and they have weapon that pushes me away when I try. I'm stuck."
    
    
    
    return
