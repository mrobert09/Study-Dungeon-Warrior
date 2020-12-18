import pygame

#Initialize game
pygame.init()

#Create Game Window (pixels x-axis, pixels y-axis)
screen = pygame.display.set_mode((800, 600))


#Title and Icon
# pygame.display.set_caption("Study Dungeon Warrior")
# icon = pygame.image.load("RoundBeaver-Logo.png")
# pygame.display.set_icon(icon)

#RoomBackground
roombackground = pygame.image.load('Images/BasicRoom.png')

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)
    
    screen.blit(roombackground, (0,0))
    pygame.display.update()




######### Outline ##########

#Generate Dungeon

    #Generate starting room

    #Generate Path to Boss (Series of Rooms minimum # of rooms)

    #Generate Side Rooms (have maximum # of rooms)

    #Fill rooms with Monsters/Traps

    #Fill rooms with Powerups

    #Generate Checkpoints (after minimum # rooms from start)

    #Generate Boss

#Generate Mini-Map

    #Create mini-map of dungeon

    #Hide all of mini-map except for rooms player has explored

#Start dungeon

    #Initialize Character (If new player)

    #Place Character in starting room

    #Display Dungeon screen

#Combat (for monsters and traps)

    #Combat music?

    #Intro to combat text ('It's an angry Andrew Bear!')

    #Transition to combat screen

    #Initialize instance of Monster

    #Attack

        #Text ("The hobgoblin is attacking with 'What is the square root of 196?' How will you respond?")

        #Multiple choice random generation and display ("A)12, B)16, C)14, D)RandomSarcasticAnswer, E)Use Items/Powers")

        #Get input

        #If Wrong input:

            #Oh no! text, monster attack animation

            #Reduce character HP

            #Check player is alive

                #If not, go to failure screen

            #Attack

        #If Correct input:

            #Epic attack animation ("Wow! The correct answer was super effective")

            #Reduce monster hp

            #Check if monster hp == 0

                #If yes, End of Combat

            #Attack

        #If Use PowerUp/Skill:

            #Display list of stuff to use

            #Get input

            #Apply Benefit

            #Attack

    #End of Combat

        #Victory Text

        #Experience Text

            #Modify Player exp

        #Transition back to dungeon

#Move Rooms

    #Open door animation

    #Transition screen (screen wipe to new room?)

    #Display room moved into (monsters, powerups, checkpoints)

    #Previously visited room

        #Update mini-map

    #First time room

        #If monster

            #Auto move 1/4 into room

            #Combat

        #If no monster:

            #Update minimap

#IF walk over powerup

#If click on checkpoint

#Failure Screen

    #Oh no you died text and options

    #Get input

    #Try Again

        #Respawn player at checkpoint using player stats from when they last visited the checkpoint

    #Quit

        #Return to title screen

#Combat Screen

    #Pokemon style? Character on lower left, enemy on upper right?

#Pause Screen

    #Interrupt current process?

    #Display options

        #Quit to Main Menu

        #Quit to Desktop

        #Return to last Checkpoint

        #Resume (Or press the same button that was used to open pause screen, usually "Esc")

    #Get input

    #Do the thing
