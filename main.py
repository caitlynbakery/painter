import pygame

screenwidth = 1280
screenheight = 720
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)

pink = (252, 151, 240)
white = (255, 255, 255)
blue = (30, 116, 255)
lightblue = (38, 251, 255)

drawingRect = pygame.Rect(200, 0, screenwidth-200, screenheight)
pygame.draw.rect(screen, white, drawingRect)

eraser = pygame.image.load("img/eraser.png")
eraserRect = pygame.Rect(20, 20, 80, 80)

# create color menu
pinkRect = pygame.Rect(120, 230, 50, 50)
pygame.draw.rect(screen, pink, pinkRect)

blueRect = pygame.Rect(20, 230, 50, 50)
pygame.draw.rect(screen, blue, blueRect)

lightblueRect = pygame.Rect(20, 310, 50, 50)
pygame.draw.rect(screen, lightblue, lightblueRect)

# set default brush size and color
brushColor = pink
brushSize = 10

smallbrushRect = pygame.Rect(10, 140, 40, 40)
# pygame.draw.rect(screen, pink, smallbrushRect)
pygame.draw.circle(screen, white, smallbrushRect.center, 5)

mediumbrushRect = pygame.Rect(55, 140, 40, 40)
pygame.draw.circle(screen, white, mediumbrushRect.center, 10)

largebrushRect = pygame.Rect(100, 140, 40, 40)
pygame.draw.circle(screen, white, largebrushRect.center, 15)

xlargebrushRect = pygame.Rect(150, 140, 40, 40)
pygame.draw.circle(screen, white, xlargebrushRect.center, 20)

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
            pygame.draw.circle(screen, brushColor, mousepos, brushSize)
        if eraserRect.collidepoint(mousepos):
            brushColor = white
        if pinkRect.collidepoint(mousepos):
            brushColor = pink
        if blueRect.collidepoint(mousepos):
            brushColor = blue
        if lightblueRect.collidepoint(mousepos):
            brushColor = lightblue
        if smallbrushRect.collidepoint(mousepos):
            brushSize = 5
        if mediumbrushRect.collidepoint(mousepos):
            brushSize = 10
        if largebrushRect.collidepoint(mousepos):
            brushSize = 15
        if xlargebrushRect.collidepoint(mousepos):
            brushSize = 20
        
    pygame.display.update()
