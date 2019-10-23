import pygame

# Intialise the pygame - NB
pygame.init()

# Create the screen size, 800 - w, 600 - h
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceicon.png')
pygame.display.set_icon(icon)


# Game Loop
running = True
while running:
    # Change background color using RBG - Red, Green, Blue
    screen.fill((246, 36, 89))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update() #NB always update your game window


