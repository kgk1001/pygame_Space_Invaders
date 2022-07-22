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

# enemy
enIm = pygame.image.load("alien.png")
enX = 0
enY = 0
enChgX = 0.2
enChgY = 0.25

# bullet
bulIm = pygame.image.load("bullet.png")
bulX = 0
bulY = 580
bulChgX = 0.2
bulChgY = 0.511
bulState = "ready"
score = 0


def player(x, y):
    screen.blit(plyIm, (x, y))


def enemy(x, y):
    screen.blit(enIm, (x, y))


def bullet(x, y):
    # global bulState
    # bulState = "fire"
    screen.blit(bulIm, (x + 16, y - 10))


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
                plyChg = -0.2
                print("left")
            if event.key == pygame.K_RIGHT:
                plyChg = 0.2
                print("right")
            if event.key == pygame.K_UP:
                if bulState == "ready":
                    bulState = "fire"
                    bulX = plyX
                    bullet(bulX, bulY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                plyChg = 0

    plyX += plyChg
    # set the player boundary
    if plyX < 0:
        plyX = 0
    elif plyX > 736:
        plyX = 736

    enX += enChgX
    if enX < 0:
        enChgX = 0.2
        enY += 32
    elif enX > 736:
        enChgX = -0.2
        enY += 32
    # bullet movement
    if bulState == "fire":
        bullet(bulX, bulY)
        bulY -= bulChgY
        if (enY <= bulY <= enY + 60 and enX - 22 <= bulX <= enX + 22):
            bulState = "ready"
            bulY = 580
            score += 1
            print(score)

        elif bulY <= 0:
            bulState = "ready"
            bulY = 580

    player(plyX, plyY)
    if score == 5:
        enX = 0
        enY = 0
        score = 0
    enemy(enX, enY)
    pygame.display.update()
