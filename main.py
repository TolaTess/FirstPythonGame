import pygame
import random

# Intialise the pygame - NB
pygame.init()

# Create the screen size, 800 - w, 600 - h
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceicon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('monster.png')
# Random respawning
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 5
enemyY_change = 30

def Player(x, y):
    # blit - to draw
    screen.blit(playerImg, (x, y))

def Enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:
    # Change background color using RBG - Red, Green, Blue
    screen.fill((46, 49, 49))
    #backgroun image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
                # If key released then stop player.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking that player does not go out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
        #800 - 64 for the image size
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -5
        enemyY += enemyY_change

    Player(playerX, playerY) # will always show on the screen as in the while loop
    Enemy(enemyX, enemyY)
    pygame.display.update() #NB always update your game window


