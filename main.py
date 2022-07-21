import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# titlle and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")  # load the image
pygame.display.set_icon(icon)  # place the icon

# player
plyIm = pygame.image.load("spaceship.png")
plyX =368
plyY = 536


def player():
    screen.blit(plyIm, (plyX, plyY))


# game loop
running = True
while running:
    screen.fill((80, 80, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player()
        pygame.display.update()
