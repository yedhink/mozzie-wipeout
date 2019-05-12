import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 8
BOARDHEIGHT = 6
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0 #Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

GRAY     = (100, 100, 100)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)

BGCOLOR = GRAY
LIGHTBGCOLOR = BLACK
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLACK

PIC1 = pygame.image.load("1.jpg")
PIC1 = pygame.transform.scale(PIC1,(BOXSIZE,BOXSIZE))
PIC2 = pygame.image.load("2.jpg")
PIC2 = pygame.transform.scale(PIC2,(BOXSIZE,BOXSIZE))
PIC3 = pygame.image.load("3.jpg")
PIC3 = pygame.transform.scale(PIC3,(BOXSIZE,BOXSIZE))
PIC4 = pygame.image.load("4.jpg")
PIC4 = pygame.transform.scale(PIC4,(BOXSIZE,BOXSIZE))
PIC5 = pygame.image.load("5.jpg")
PIC5 = pygame.transform.scale(PIC5,(BOXSIZE,BOXSIZE))
PIC6 = pygame.image.load("6.jpg")
PIC6 = pygame.transform.scale(PIC6,(BOXSIZE,BOXSIZE))
PIC7 = pygame.image.load("7.jpg")
PIC7 = pygame.transform.scale(PIC7,(BOXSIZE,BOXSIZE))

POSS = (1, 1, 1, 1, 1, 1, 1)
ALLPICS = (PIC1, PIC2, PIC3, PIC4, PIC5, PIC6, PIC7)
assert len(ALLPICS) * 7 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def getRandomizedBoard():
    # to get more possibilities
    icons = []
    for poss in POSS:
        for pic in ALLPICS:
            icons.append( (pic, poss) )

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawPic(pic, boxx, boxy):

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords

    if pic == PIC1:
        DISPLAY.blit(PIC1,(left,top))
    elif pic == PIC2:
        DISPLAY.blit(PIC2,(left,top))
    elif pic == PIC3:
        DISPLAY.blit(PIC3,(left,top))
    elif pic == PIC4:
        DISPLAY.blit(PIC4,(left,top))
    elif pic == PIC5:
        DISPLAY.blit(PIC5,(left,top))
    elif pic == PIC6:
        DISPLAY.blit(PIC6,(left,top))
    elif pic == PIC7:
        DISPLAY.blit(PIC7,(left,top))

def getPic(board, boxx, boxy):
    return board[boxx][boxy][0]


def drawBoxCovers(board, boxes, cover):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAY, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        pic = getPic(board, box[0], box[1])
        drawPic(pic, box[0], box[1])
        if cover > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAY, BOXCOLOR, (left, top, cover, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxes(board, boxesToReveal):
    # Do the "box reveal" animation.
    for cover in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, cover)


def coverBoxes(board, boxesToCover):
    # Do the "box cover" animation.
    for cover in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, cover)


def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAY, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the (revealed) icon.
                pic = getPic(board, boxx, boxy)
                drawPic(pic, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAY, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


def startGame(board):
    # Randomly reveal the boxes 5 at a time.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(5, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxes(board, boxGroup)
        coverBoxes(board, boxGroup)


def gameWon(board):
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAY.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            return False # return False if any boxes are covered.
    return True


global FPSCLOCK, DISPLAY
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event
pygame.display.set_caption('Memory Game')

mainBoard = getRandomizedBoard()
revealedBoxes = generateRevealedBoxesData(False)

firstSelection = None # stores the (x, y) of the first box clicked.

DISPLAY.fill(BGCOLOR)
startGame(mainBoard)

while True: # main game loop
    mouseClicked = False

    DISPLAY.fill(BGCOLOR)
    drawBoard(mainBoard, revealedBoxes)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True

    boxx, boxy = getBoxAtPixel(mousex, mousey)
    if boxx != None and boxy != None:
        if not revealedBoxes[boxx][boxy]:
            drawHighlightBox(boxx, boxy)
        if not revealedBoxes[boxx][boxy] and mouseClicked:
            revealBoxes(mainBoard, [(boxx, boxy)])
            revealedBoxes[boxx][boxy] = True # "revealed" box
            if firstSelection == None: # the current box was the first box clicked
                firstSelection = (boxx, boxy)
            else: # if the current box was the second box clicked
                # Check if there is a match between the two boxes selected.
                icon1pic = getPic(mainBoard, firstSelection[0], firstSelection[1])
                icon2pic = getPic(mainBoard, boxx, boxy)

                if icon1pic != icon2pic:
                    # if Icons don't match. Re-covering up both selections.
                    pygame.time.wait(1000) # 1000 milliseconds
                    coverBoxes(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                    revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                    revealedBoxes[boxx][boxy] = False
                elif hasWon(revealedBoxes): # check if all pairs found
                    gameWon(mainBoard)
                    pygame.quit()
                    quit()


                    # Reset the board
                    mainBoard = getRandomizedBoard()
                    revealedBoxes = generateRevealedBoxesData(False)

                    # Show the fully unrevealed board for a second.
                    drawBoard(mainBoard, revealedBoxes)
                    pygame.display.update()
                    pygame.time.wait(1000)

                    # Replay the start game animation.
                    startGame(mainBoard)
                firstSelection = None # reset firstSelection variable

    # Redraw the screen and wait a clock tick.
    pygame.display.update()
    FPSCLOCK.tick(FPS)



if __name__ == '__main__':
    main()
