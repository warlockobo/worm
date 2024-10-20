
# The script of the game goes in this file.

# Declare characters used by this game

define pov = Character("[povname]")
define e = Character("Eileen")
define l = Character("Lorenzo")
define t = Character("Tammy")
define a = Character("Alex")
define mf = Character("Ms. Fennec")

# The game starts here.

label start:

    # Plays BGM
    play music "audio/BGM/day1_bgm.ogg" fadein 1 volume 0.05 loop

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg monty bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #This shows a character sprite
    show monty noglasses

    #These display lines of dialogue.
    "The luminescent mushrooms shine through your window. Their glow is a common indicator that it's time to start the day."

    "Today is Friday, and you've got school. You live in the bustling city of Wormopolis, renowned for its academics and nightlife."
    
    play sound "audio/SoundFX/clothes.ogg" 

    "You get dressed and head to class at Sedimentary High School, which has the highest scores in the county."

    show monty plain

    "Right before you leave, you remember something... you remember that you forgot your name!"

    $ povname = renpy.input("What is your name?", length=32)    #allows for a custom name for the main character
    $ povname = povname.strip()
    "That's right, your name is [povname]! How could you forget?"

    "After remembering your name, you resume your adventure."


label school:

    scene bg classroom

    play sound "audio/SoundFX/hallway.ogg"

    "The classroom is alive with the chatter of your peers. You take your seat and bring out your book. As you're looking down, someone approaches you..."

    show lorenzo plain with dissolve
    l "Ciao [povname]! Glad you made it on time, you sleepyhead."

    "You recognize the leech as your old friend Lorenzo, a transfer student from Italy."

    l "Those Worm of Duty matches last night were crazy, I had so much fun."

    l "You usually miss first period, but hey since you're here on time...  I forgot my book, mind if I sit next to you and use yours?"

    menu:
        "Sure, I don't mind.":
            jump lorenzochoice1A

        "No way man.":
            jump lorenzochoice1B

label lorenzochoice1A:

    show lorenzo blush
    l "Awesome! Thanks [povname], you're the best."
    "Lorenzo takes the seat next to yours and leans uncomfortably close over your shoulder to look at your book."
    
    hide lorenzo blush with dissolve
    jump classbegin

label lorenzochoice1B:

    show lorenzo disappointed
    l "Oh... alright, I thought we were cool like that..."
    "Lorenzo takes a seat a moderate distance away, looking sorely disappointed"

    hide lorenzo disappointed with dissolve
    jump classbegin

label classbegin:
    
    show fennec plain with dissolve:
        ypos -0.05    #sets a custom position for the sprite  
        xpos 0.27
    "The teacher gets started punctually and begins discussing the chapter you read last night."

    hide fennec plain with dissolve
    show fennec plain with dissolve:
        ypos -0.05
        xpos 0.5
    show alex plain at left with dissolve
    mf "And so let's discuss the main conflict of the chapter you all should've read last night - Alex, can you tell me why Juliet said 'O Wormeo wormeo, wherefore art thou Wormeo' and what she meant by that?"
    show alex dramatic
    a "Of course Ms. Fennec. Juliet was expressing her sorrow over the Wormeo family name. The Montagues and Capulets were feuding, so their love was forbidden. Truly, there is no greater melancholy than love that cannot be..."

    mf "Excellent work, Alex. The teacher continues to ramble on."
    hide alex dramatic with dissolve
    hide fennec plain with dissolve
    "The student that answered that was Alex, the earthworm. He's always been the poetic and mysterious type, and you don't know him all that well."

    play sound "audio/SoundFX/bell.ogg" 

    "As some time passes, the bell rings and indicates that it’s time for your favorite part of the day – lunch!"
    
    scene bg cafeteria with fade
    "You are sitting at a table by yourself enjoying the meal of the day, pizza, when a colorful and spicy hammerhead worm approaches you."
    show tammy plain with dissolve
    t "What’s up dweeb, sitting all by yourself?"

    "This worm’s name was Tammy, and she was... abrasive, to say the least."

    t "You look lonely, so I’m gonna sit next to you, ‘kay?"

    menu:
        "Get lost.":
            jump tammychoice1A

        "Okay...":
            jump tammychoice1B

label tammychoice1A:
    show tammy angry
    t "Figures, don’t come crying to me when you have no friends."
    "You enjoy the rest of your lunch alone in peaceful solitude."
    hide tammy angry with dissolve
    jump afterlunch

label tammychoice1B:
    show tammy blush
    t "O-oh, I didn’t think you’d actually say yes... it’s not like I enjoy hanging out with you or anything... idiot."
    "You enjoy the rest of your lunch in the company of Tammy."
    hide tammy blush with dissolve
    jump afterlunch

label afterlunch:
    scene bg cave 2
    "Lunch ends and the students make their way back to class. Nothing eventful happens as the day passes on, and eventually school is let out."

    "The rest of the students are talking in groups about plans for the weekend, but you notice three worms hoping to catch your gaze."

    "Who do you approach?"

label afterlunchchoice:
    menu:
        "Alex":
            jump alexplans

        "Tammy":
            jump tammyplans

        "Lorenzo":
            jump lorenzoplans

label tammyplans:
    show tammy plain with dissolve
    "Hey dweeb, let’s go shopping at the mall. I’m not asking."
    menu:
        "If you insist.":
            jump tammyacceptance
        "Let me think about it.":
            jump tammydenial

label tammyacceptance:
    t "Carry my bag, please and thank you."
    "Tammy hands you her bag and walks off"
    hide tammy plain with dissolve
    jump mallstart

label tammydenial:
    show tammy angry
    t "Ugh, whatever."
    hide tammy angry with dissolve
    jump afterlunchchoice

label lorenzoplans:
    show lorenzo plain with dissolve
    "Bienvenido [povname]! I’m going to head to the cafe for some coffee and relaxation, wanna come?"
    menu:
        "Sure, sounds fun.":
            jump lorenzoacceptance
        "No thanks.":
            jump lorenzodenial

label lorenzodenial:
    show lorenzo disappointed
    l "Ah.. perhaps some other time then, friend."
    hide lorenzo disappointed with dissolve
    jump afterlunchchoice

label lorenzoacceptance:
    show lorenzo blush
    l "Fantastico! Let’s head there now, shall we?"
    hide lorenzo blush with dissolve
    jump cafestart

label alexplans:
    show alex plain with dissolve
    "Oh, hey [povname], didn’t notice you there... I was about to go to the library to ponder life’s greatest mysteries... care to join me?"
    menu:
        "That sounds fun.":
            jump alexacceptance
        "Not right now.":
            jump alexdenial
label alexacceptance:
    show alex blush
    "Cool, I’m curious to probe your mind."
    hide alex blush with dissolve
    jump librarystart

label alexdenial: 
    "That’s alright, everything is brief and unimportant in the grand scheme of the universe."
    hide alex plain with dissolve
    jump afterlunchchoice

label cafestart:

    play music "audio/BGM/cafe_bgm.ogg" volume 0.05 loop

    scene bg cafe
    show lorenzo plain with dissolve

    "The cafe is dimly lit and smells of roasted coffee. There’s quiet chatter muffled by a smooth jazz track."

    "You and Lorenzo take a seat at a table. He orders a coffee and a biscotti, and gazes longingly at your lips."

    l "It’s been too long since we’ve hung out like this, mio amico."

    "Lorenzo puts his chin on his hands and looks at you."

    show lorenzo hands

    l "The biscotti is taking so long, and I am famished..."

    l "[povname], would you mind if I... had a bite of you? Like when we were kids?"

    menu:
        "That wouldn't hurt too bad, I guess...":
            jump lorenzochoice2A

        "Absolutely not.":
            jump lorenzochoice2B

label lorenzochoice2A:
    l "La ringazio molto, mio amore..."

    show lorenzo blush with hpunch

    "You feel a twinge of pain as Lorenzo digs his circular rows of teeth into your side, and he begins sucking your blood."

    scene bg black with fade

    "The world begins to blur and the edges of your vision begin to darken. The jazz and the voices blend together in a cacophany of confusion, and you can’t stay upright any longer."

    play sound "audio/SoundFX/fall.ogg"

    "You faint."

    scene bg cafe daze with fade

    "You awaken to a sharp cutting jab in your side. The familiar smell of coffee and sound of the jazz floods back in to your senses."

    show lorenzo plain

    "Lorenzo is staring at you with almost no concern in his eyes, almost like he is simply pleased that he got what he wanted."

    jump cafemid

label lorenzochoice2B:
    show lorenzo disappointed
    l "Ah, my soul aches, but I understand. We are older now, and things aren’t the way they were back then."

    l "Truthfully [povname], not having you around has left a mole-sized hole in my heart. The fun adventures we used to have, the time we spent, the blood I used to gorge... my life is meaningless without them"

    jump cafemid

label cafemid:
    scene bg cafe with fade
    show lorenzo plain
    "The waitress brings Lorenzo his coffee and biscotti, and you both sit in awkward silence for the rest of the afternoon."
    "As the mushrooms dim and the cafe clears out, Lorenzo speaks up."

    l "What a wonderful time I had with you, we must do this more often! I have missed your presence. Until then, mio amico."

    stop music fadeout 5

    "Lorenzo slithers off into the night, fading from view until he disappears completely.."

    jump day1end

label mallstart:

    play music "audio/BGM/mall.ogg" volume 0.15

    scene bg mall
    show tammy plain with dissolve

    t "Ugh, shopping has got to be one of my favorite things in life. Retail therapy, you know?"
    t "I wish I had a guy that would pay for everything... I guess you’ll have to do for today."
    t "Okay [povname], be honest, how does this look?"

    menu:
        "You look delicious.":
            jump tammychoice2A
        "You look like a worm in a dress.":
            jump tammychoice2B
label tammychoice2A:
    "*Tammy blushes*"
    show tammy blush
    t "[povname], you idiot! You’re not supposed to be so bold!"

    "Tammy timidly continues walking to the next shop, hoping that you’ll follow her."

    jump mallmid
label tammychoice2B:
    show tammy angry
    t "A WORM??? YOU’VE SAID A LOT OF STUPID THINGS [povname], BUT THAT REALLY TAKES THE CAKE."

    "Tammy storms off in a huff but looks over her shoulder, expecting you to still follow her."

    jump mallmid
label mallmid:
    scene bg cave 1 with fade
    "The shopping spree continues, with your bank account growing lighter by the second."

    stop music fadeout 5 

    "Eventually, after your fashion expertise was questioned multiple times, you walk Tammy home."

    "It’s a small and quaint place, not what’d you expect from her boisterous attitude."

    show tammy gentle with dissolve

    t "This is my tunnel... it’s not much, but it’s home, y’know?"

    t "Thanks for coming with me, [povname]. It’s not like you had anything better to do though."

    show tammy plain

    t "Maybe next time we’ll buy you some clothes that make you look less like a dork, ‘kay?"

    "Tammy wiggles into her tunnel and disappears."

    hide tammy plain with dissolve

    jump day1end

label librarystart:

    play music "audio/BGM/library_bgm.ogg" volume 2

    scene bg library

    "The library is somewhat filled with book enthusiasts, students, and other scholars. There is a serene hum coming from and unknown source, and giant bookshelves collectively housing the greatest knowledge of our time"

    show alex plain with dissolve

    a "I’ve always loved the vibes here. Quiet, peaceful, sophisticated... the perfect place for a couple of philosophers like us, right?"

    a "There’s something different about you. I noticed it in class today. It’s almost like you’re above all of this. Controlled by something greater than any of us."

    show alex dramatic

    a "I think that there’s more for us, [povname]. More than just living underground and going with our base instincts."

    a "I know I’m just a worm, but does that mean I can’t aspire to great things? That I can’t have hopes and dreams far beyond the scope of any worm before me?"

    a "I’m not content to just wriggle around in the dirt until I shrivel up and die. I want to experience everything this world has to offer, worm or not."

    show alex plain

    a "“What do you think, [povname]?"

    menu:
        "I think that you can be whatever you want to be, Alex. You’re a smart worm.":

            show alex blush

            a "Thanks [povname], I knew chatting with you was a good idea. You really understand."

            jump librarymid
        
        "I think you're a worm.":

            show alex plain

            a "That’s okay if you don’t believe in me, [povname]. It just gives me more motivation to prove the world wrong."

            jump librarymid

label librarymid:

    show alex plain

    a "This is why I invited you out. I knew, at the least, that’d you be interesting to talk to. And you’re a great listener, has anyone ever told you that?"

    a "Thanks for hearing me out, [povname]. I’ll see you around."

    stop music fadeout 5

    "With that, Alex crawls his way out of the library and worms into the unsuspecting night."


    jump day1end

label day1end:
    scene bg cave 3

    "The mushrooms are barely visible, and it’s only due to your superior mole senses that you can find your way home in the dark. The nocturnal creatures are just waking up, and the spirits of the night are coming alive."

    "After a long day with more social interaction than you’ve had in the past several months, you find yourself completely exhausted."

    scene bg monty bedroom with fade

    play sound "audio/SoundFX/growl.ogg"

    "Your bed is warm and inviting, but your stomach roars, reminding you that you haven’t eaten since lunch..."

    "Despite your hunger, you plop on to your bed and are awash with feelings of lethargy."

    scene bg black with fade

    "Your eyelids weigh as elephants, and it’s not long before the sweet embrace of sleep takes you."

    jump day2start

label day2start:
    scene bg monty bedroom

    "You’re rudely awoken by the shine of a mushroom through your window, constricting your pupils before you’ve had a chance to wipe the dust from your eyes."
    scene bg monty bedroom with vpunch

    play sound "audio/SoundFX/angry_knock.ogg"

    "You were barely conscious when your ears were assaulted by a banging at your door."

    show snail allletters with dissolve:
        ypos -0.1       #sets a custom position for the sprite
        xpos 0.2

    "You clambered out of bed and open your front door where you are greeted by... a snail."

    "Ah, the snail mail. This small fellow has three letters taped to his back, all addressed to you."

    hide snail allletters with dissolve

    "You take the letters off of his shell and he begins squirming away without another word, leaving a trail of slime in his wake."

    "You examine the letters and find them all addressed to you with different senders. Tammy, Lorenzo, and Alex."

    jump letterchoice

label letterchoice:
    menu:
        "Tammy":
            jump tammyletter
        "Lorenzo":
            jump lorenzoletter
        "Alex":
            jump alexletter

label tammyletter:
    "Sup nerd. Thought you’d like to tone up with me at the gym today. See you there."

    menu:
        "Meet Tammy":
            jump tammygym
        "Read the other letters":
            jump letterchoice

label lorenzoletter:
    "Ciao [povname]! Hanging out with you at the cafe was so nostalgic, I was wondering if you wanted to come over and play some video games, like old times? We could talk too."

    menu:
        "Meet Lorenzo":
            jump lorenzohouse
        "Read the other letters":
            jump letterchoice

label alexletter: 
    "Dear [povname], I had an excellent time yesterday talking with you. I’d like to show you my favorite place to sit and think, if that’s cool with you? Meet me at Wormwood Park."

    menu:
        "Meet Alex":
            jump alexpark
        "Read the other letters":
            jump letterchoice

label alexpark:

    play music "audio/BGM/alex_date.ogg" volume 0.10 fadein 2

    scene bg cave 1

    "You go to the park and see Alex coiled on a bench, his pink worm skin glistening in the mushroomlight."
    show alex plain
    a "Ah, [povname]! Excellent to see you. I was just enjoying some fresh air and nature. It truly is wonderful, isn’t it?"
    a "I want to show you to my favorite spot, perhaps we can have some more intellectual discussions there."
    "Alex guides you through a winding path of rock and moss. There are twists and turns that would be difficult to navigate without repeated exposure."
    "After some time, you and Alex come into a clearing with the most beautiful sight you’ve ever seen."
    scene bg special place with fade
    "There is a pond, with bright blue mushrooms illuminating the entire area, and luminescence reflecting off the water to create a mesmerizing ripple effect."
    show alex blush with dissolve
    a "I always come here to think and get away from the bustle of the city, and I thought I’d share it with you, my scholar in arms."
    "The environment was amazing. You’d never experienced beauty like this. But there was one thing clawing at the back of your mind, making its way to the forefront of all of your thoughts."
    "You were hungry. Ravenously hungry. And you needed to eat NOW."
    "The only thing edible nearby was... a worm. You eat worms."
    show alex betrayed with hpunch
    "Alex had his eyes on the scenery as you came from behind and grappled him into your mouth."

    play sound "audio/SoundFX/chewing.ogg" 

    "His pleads and screams were cut short by the gnashing of your teeth."
    hide alex betrayed with pixellate
    "You had been satiated. And now, you could enjoy a nap in the most gorgeous place you’d ever been."

    return

label tammygym:

    play music "audio/BGM/gym.ogg" fadein 1 

    scene bg gym
    show tammy plain with dissolve

    t "O-oh, [povname]! I didn’t think you’d actually come- uhh I mean um I’m glad you came!"
    t "You showed up right on time, I was just about to start some arm exercises. You’re kinda scrawny in that area, but I think you’ve got potential."
    "You sit down in the alien looking machine as Tammy sets the weight and positions your arms."
    show tammy gentle
    t "Alright [povname], just curl the bar here, and then let it down. You should feel it in your biceps."
    "Tammy was being gentler than usual, with what seemed like a glint of admiration in her eyes."
    "You managed to do a few reps on the machine before the fabled ‘burn’ set in."
    t "That wasn’t bad at all for your first time!"
    
    stop music fadeout 3

    "Suddenly..."

    play music "audio/BGM/bad_ending.ogg" fadein 2

    "Tammy’s words sounded muffled, and along with that, the ambient noises of the gym began to fade. Only one sense remained in your entire body."
    "Your ravenous hunger."
    "You didn’t eat dinner last night, and you skipped breakfast because of all the mail."
    "You look at Tammy - the sudden kindness in her eyes - it means nothing to you."
    "Tammy is a worm. Moles eat worms."

    show tammy betrayed with hpunch

    play sound "audio/SoundFX/chewing.ogg"

    "You grab Tammy and shove her into your mouth without hesitation, so swiftly that there was no resistance."
    "Her screams and pleads are promptly cut short by the chomp of your jaw."
    hide tammy betrayed with pixellate
    "At first there is complete silence... but then, you hear your blood rushing through your veins."
    scene bg gym daze with hpunch
    "You cough and there’s... blood?"

    play sound "audio/SoundFX/fall.ogg"

    scene bg gym daze with vpunch

    "Your legs can’t support you anymore and give out. You fall to the floor with loud THUD"
    "Various other animals in the gym begin to rush to you – whether it was from the murder or your own weakness, you’re unsure."
    scene bg black with fade
    "Your vision fades to black and you remember."
    "Hammerhead worms are toxic."

    return
label lorenzohouse:

    play sound "audio/SoundFX/normal_knock.ogg"

    scene bg cave 4

    "You arrive at Lorenzo’s house and knock on the door. You hear a bump and a curse from inside, but then the door is opened."
    show lorenzo blush with dissolve
    l "Che figata! I did not fully expect you to arrive, but I am so glad you did."
    scene bg lorenzo bedroom with fade
    show lorenzo plain with dissolve
    "Lorenzo gives you a small tour of his house, but not much has changed since you were last here many, many years ago."
    "Eventually you wind up in his room, adorned with several band posters, a computer, his bed, and a game console."
    "Lorenzo turns on the game console and you’re greeted by the title screen for Worm Kart 7."
    l "Mio amico, what say we have a little wager?"
    show lorenzo blush
    l "If I beat you in Worm Kart, you let me suck your blood! If you win... you can have anything you’d like from my room."
    "The PC is worth a pretty penny, as is the game console, and you know yourself to be a bit of a Worm Kart savant..."
    show lorenzo plain
    "Before you can give your answer, Lorenzo hands you a controller and sits next to you."

    play music "audio/BGM/bad_ending.ogg" fadein 2

    "The matches were neck and neck with both of you gaining and losing the lead. Sometimes he’d win, sometimes it’d be you, until something strange started happening..."
    "His kart began speeding up. Faster than you know anything to be possible. Even in the fastest times on the internet, you’d never seen a kart move this fast."
    "Was Lorenzo... cheating?"
    "His lead began to get further and further ahead until eventually it was insurmountable. You had lost the deal."
    show lorenzo hands
    l "I am sorry, mio amore, but a deal is a deal."
    show lorenzo frenzy with vpunch
    "Before you could even react, Lorenzo was upon you."

    play sound "audio/SoundFX/suck.ogg"

    "He positioned himself behind your back, in a place you couldn’t reach with your hands, and began sucking your blood."
    scene bg lorenzo bedroom daze with fade
    show lorenzo frenzy
    "You could feel his teeth gnash and shred through your flesh, and your life essence began to flow out of the wound."
    "You were shocked to be drained of energy so quickly, but then you remembered... you hadn’t eaten in quite a while."
    scene bg black with pixellate
    "You fell to your knees and your vision began to fade to black. Lorenzo showed no signs of stopping his feast."
    "The last thing you remembered as your face made contact with the floor was... Lorenzo is a leech."

    return
