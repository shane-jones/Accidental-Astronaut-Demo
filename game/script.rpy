## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define f = Character('Frank')
define PC = Character('...')

## The game starts here.



label start:
    
    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg room

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show Frank

    ## These display lines of dialogue.

    f "Ughh....."
    stop music
    play music "breathing.mp3" fadein 2 fadeout 2
    
    f "W....where..am I..??."

    f "How did i get here?...."
    
    
    f "Oh no!! That red flashing light isnt a good sign, the oxygen levels are low. I... I need to get up.., ive got to bring up these oxygen
       levels." 
    
    
    
    play sound "Beep-Sound.mp3" loop
       
    PC "**beep**"
    
    stop music
    
    f "Ahh.. thats better, I can breathe better now"
    
    f "I need to get out of here, but how?"
    
    menu:
        "Do nothing, wait for help":
            "I just hope help arrives soon"
        
        "Force airlock":
            "I dont want to die.."
        
        "Maybe that strange device on the wall can help":
            "Oh look its a recording..."
         

    ## This ends the game.

    return
