import pygame

# Intialise the pygame - NB
pygame.init()

# Create the screen size, 800 - w, 600 - h
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceicon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def Player(x, y):
    #blit - to draw
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    # Change background color using RBG - Red, Green, Blue
    screen.fill((246, 36, 89))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 4.5
                # If key released then stop player.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
        #800 - 64 for the image size
    elif playerX >= 736:
        playerX = 736
    Player(playerX, playerY) # will always show on the screen as in the while loop
    pygame.display.update() #NB always update your game window


