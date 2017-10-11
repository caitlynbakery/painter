import pygame

screenwidth = 1280
screenheight = 720
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)

pink = (252, 151, 240)
white = (255, 255, 255)

drawingRect = pygame.Rect(200, 0, screenwidth-200, screenheight)
pygame.draw.rect(screen, white, drawingRect)

eraser = pygame.image.load("img/eraser.png")
eraserRect = pygame.Rect(20, 20, 80, 80)
pinkRect = pygame.Rect(120, 20, 50, 50)
pygame.draw.rect(screen, pink, pinkRect)
brushColor = pink

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
    screen.blit(eraser, eraserRect)
    if mousedown == True:
        if drawingRect.collidepoint(mousepos):
            pygame.draw.circle(screen, brushColor, mousepos, 10)
        if eraserRect.collidepoint(mousepos):
            brushColor = white
        if pinkRect.collidepoint(mousepos):
            brushColor = pink
    pygame.display.update()
