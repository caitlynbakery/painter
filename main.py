import pygame

screenwidth = 1280
screenheight = 720
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)

pink = (252, 151, 240)
white = (255, 255, 255)
blue = (30, 116, 255)
lightblue = (38, 251, 255)
red = (255, 0, 0)
orange = (255, 157, 0)
yellow = (246, 255, 86)
green = (38, 239, 61)
purple = (165, 68, 244)

drawingRect = pygame.Rect(200, 0, screenwidth-200, screenheight)
pygame.draw.rect(screen, white, drawingRect)

eraser = pygame.image.load("img/eraser.png")
eraserRect = pygame.Rect(20, 20, 80, 80)

wipescreen = pygame.image.load("img/wipescreen.png")
wipescreenRect = pygame.Rect(120, 20, 80, 80)

pandastamp = pygame.image.load("img/panda.png")
pandastampRect = pygame.Rect(20, 650, 80, 80)

pusheenstamp = pygame.image.load("img/pusheen.png")
pusheenstampRect = pygame.Rect(120, 650, 80, 80)

pandatransparent = pygame.image.load("img/pandatransparent.png")

# create color menu
orangeRect = pygame.Rect(120, 230, 50, 50)
pygame.draw.rect(screen, orange, orangeRect)

redRect = pygame.Rect(20, 230, 50, 50)
pygame.draw.rect(screen, red, redRect)

yellowRect = pygame.Rect(20, 310, 50, 50)
pygame.draw.rect(screen, yellow, yellowRect)

greenRect = pygame.Rect(120, 310, 50, 50)
pygame.draw.rect(screen, green, greenRect)

lightblueRect = pygame.Rect(20, 380, 50, 50)
pygame.draw.rect(screen, lightblue, lightblueRect)

blueRect = pygame.Rect(120, 380, 50, 50)
pygame.draw.rect(screen, blue, blueRect)

pinkRect = pygame.Rect(20, 450, 50, 50)
pygame.draw.rect(screen, pink, pinkRect)

purpleRect = pygame.Rect(120, 450, 50, 50)
pygame.draw.rect(screen, purple, purpleRect)

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

stamp = False
stamptype = ""

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
    screen.blit(wipescreen, wipescreenRect)
    screen.blit(pandastamp, pandastampRect)
    screen.blit(pusheenstamp, pusheenstampRect)

    if mousedown == True:
        if pandastampRect.collidepoint(mousepos):
            stamp = True
            stamptype = "panda"
        if pusheenstampRect.collidepoint(mousepos):
            stamp = True
            stamptype = "pusheen"
        
        if not stamp:
            if drawingRect.collidepoint(mousepos):
                pygame.draw.circle(screen, brushColor, mousepos, brushSize)
        else:
            if stamptype == "panda":
                if drawingRect.collidepoint(mousepos):
                    screen.blit(pandatransparent, mousepos)
            if stamptype == "pusheen":
                if drawingRect.collidepoint(mousepos):
                    screen.blit(pusheenstamp, mousepos)

        if eraserRect.collidepoint(mousepos):
            brushColor = white
            stamp = False
        if wipescreenRect.collidepoint(mousepos):
            pygame.draw.rect(screen, white, drawingRect)
            stamp = False
        if pinkRect.collidepoint(mousepos):
            brushColor = pink
            stamp = False
        if blueRect.collidepoint(mousepos):
            brushColor = blue
            stamp = False
        if lightblueRect.collidepoint(mousepos):
            brushColor = lightblue
            stamp = False
        if redRect.collidepoint(mousepos):
            brushColor = red
            stamp = False
        if orangeRect.collidepoint(mousepos):
            brushColor = orange
            stamp = False
        if yellowRect.collidepoint(mousepos):
            brushColor = yellow
            stamp = False
        if greenRect.collidepoint(mousepos):
            brushColor = green
            stamp = False
        if purpleRect.collidepoint(mousepos):
            brushColor = purple
            stamp = False
        if smallbrushRect.collidepoint(mousepos):
            brushSize = 5
            stamp = False
        if mediumbrushRect.collidepoint(mousepos):
            brushSize = 10
            stamp = False
        if largebrushRect.collidepoint(mousepos):
            brushSize = 15
            stamp = False
        if xlargebrushRect.collidepoint(mousepos):
            brushSize = 20
            stamp = False

    pygame.display.update()
