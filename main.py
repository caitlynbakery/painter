import pygame

size = (800, 600)
screen = pygame.display.set_mode(size)

pink = (252, 151, 240)

gameon = True

mousedown = False
while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        mousepos = pygame.mouse.get_pos()
    if mousedown == True:
        pygame.draw.circle(screen, pink, mousepos, 10)
    pygame.display.update()
