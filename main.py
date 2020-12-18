import pygame

# Initialize game
pygame.init()

# Create Game Window (pixels x-axis, pixels y-axis)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
# pygame.display.set_caption("Study Dungeon Warrior")
# icon = pygame.image.load("RoundBeaver-Logo.png")
# pygame.display.set_icon(icon)

# RoomBackground
roombackground = pygame.image.load('Images/BasicRoom.png')

# Player
playerIMG = pygame.image.load('Images/actor.png')
playerX = 370
playerY = 370
playerX_change = 0
playerY_change = 0


def player():
    screen.blit(playerIMG, (playerX, playerY))


def collision():
    pass


def movement_controls():
    pass


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # Room Boundaries
    if playerX < 30:
        playerX = 30
    if playerX > 540:
        playerX = 540
    if playerY < 30:
        playerY = 30
    if playerY > 520:
        playerY = 520
    screen.blit(roombackground, (0, 0))
    player()
    pygame.display.update()
