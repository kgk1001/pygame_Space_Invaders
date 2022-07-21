import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# titlle and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")  # load the image
pygame.display.set_icon(icon)  # place the icon

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((80, 80, 150))
        pygame.display.update()
