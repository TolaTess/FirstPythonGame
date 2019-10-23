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
enemyY_change = 25

# Bullet
# Ready - can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
# bullet states at the tip of player's Y axis
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"


def Player(x, y):
    # blit - to draw
    screen.blit(playerImg, (x, y))

def Enemy(x, y):
    screen.blit(enemyImg, (x, y))

def Fire_Bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # x + 16, y + 10 -> centers the bullet to the center of the player image
    screen.blit(bulletImg, (x + 16, y + 10))

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
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    Fire_Bullet(bulletX, bulletY)
                # If key released then stop player.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking that player does not go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
        #800 - 64 for the boundary size = 736
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

    # Bullet movement
    if bulletY <= 40:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        Fire_Bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    Player(playerX, playerY) # will always show on the screen as in the while loop
    Enemy(enemyX, enemyY)
    pygame.display.update() #NB always update your game window


