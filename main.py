import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")  # load the image
pygame.display.set_icon(icon)  # place the icon

# player
plyIm = pygame.image.load("spaceship.png")
plyX = 368
plyY = 536
plyChg = 0


def player(x, y):
    screen.blit(plyIm, (x, y))


# game loop
running = True
while running:
    screen.fill((80, 80, 150))

    # check all the events
    for event in pygame.event.get():

        # function to quit the game
        if event.type == pygame.QUIT:
            running = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plyChg = -0.1
                print("left")
            if event.key == pygame.K_RIGHT:
                plyChg = 0.1
                print("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                plyChg = 0

    plyX += plyChg
    player(plyX, plyY)
    pygame.display.update()