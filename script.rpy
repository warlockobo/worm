# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define pov = Character("[povname]")
define e = Character("Eileen")
define l = Character("Lorenzo")
define t = Character("Tammy")
define a = Character("Alex")
define mf = Character("Ms. Fennec")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show monty noglasses

    # These display lines of dialogue.

    "The luminescent mushrooms shine through your window. Their glow is a common indicator that it's time to start the day."

    "Today is Friday, and you've got school. You live in the bustling city of Wormopolis, renowned for its academics and nightlife."
    
    "You get dressed and head to class at Sedimentary High School, which has the highest scores in the county."

    "Right before you leave, you remember something... you remember that you forgot your name!"

    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()
    "That's right, your name is [povname]! How could you forget?"

    "After remembering your name, you resume your adventure."


label school:

    scene bg school
    show monty neutral

    "The classroom is alive with the chatter of your peers. You take your seat and bring out your book. As you're looking down, someone approaches you..."

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

    l "Awesome! Thanks [povname], you're the best."
    "Lorenzo takes the seat next to yours and leans uncomfortably close over your shoulder to look at your book."
    
    jump classbegin

label lorenzochoice1B:
    l "Oh... alright, I thought we were cool like that..."
    "Lorenzo takes a seat a moderate distance away, looking sorely disappointed"

    jump classbegin

label classbegin:

    "The teacher gets started punctually and begins discussing the chapter you read last night."

    mf "And so let's discuss the main conflict of the chapter you all should've read last night - Alex, can you tell me why Juliet said 'O Wormeo wormeo, wherefore art thou Wormeo' and what she meant by that?"

    a "Of course Ms. Fennec. Juliet was expressing her sorrow over the Wormeo family name. The Montagues and Capulets were feuding, so their love was forbidden. Truly, there is no greater melancholy than love that cannot be..."

    mf "Excellent work, Alex. The teacher continues to ramble on."

    "The student that answered that was Alex, the earthworm. He's always been the poetic and mysterious type, and you don't know him all that well."

    "As some time passes, the bell rings and indicates that it’s time for your favorite part of the day – lunch!"

    "You are sitting at a table by yourself enjoying the meal of the day, pizza, when a colorful and spicy hammerhead worm approaches you."

    t "What’s up dweeb, sitting all by yourself?"

    "This worm’s name was Tammy, and she was... abrasive, to say the least."

    t "You look lonely, so I’m gonna sit next to you, ‘kay?"

    menu:
        "Get lost.":
            jump tammychoice1A

        "Okay...":
            jump tammychoice1B

label 
    return
