import pygame
import random
import math

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

# Enemy List
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('monster.png'))
    # Random respawning
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(25)

# Bullet
# Ready - can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
# bullet states at the tip of player's Y axis
bulletY = 480
bulletX_change = 0
bulletY_change = 30
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 50)
textX = 10
textY = 10


def ShowScore(x, y):
    # render text on screen first, then blit
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def Player(x, y):
    # blit - to draw
    screen.blit(playerImg, (x, y))


def Enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def Fire_Bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # x + 16, y + 10 -> centers the bullet to the center of the player image
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    # the distance btw 2 coordinate - mathplanet.com
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop - all persistent statement most be in the while loop
running = True
while running:
    # Change background color using RBG - Red, Green, Blue
    screen.fill((46, 49, 49))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cooridnates of the spaceship
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
        # 800 - 64 for the boundary size = 736
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # enemy respawn
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        Enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    # Reset the bullet to the player for multiple bullet
    if bulletY <= 40:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        Fire_Bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    Player(playerX, playerY)  # will always show on the screen as in the while loop
    ShowScore(textX, textY)
    pygame.display.update()  # NB always update your game window
