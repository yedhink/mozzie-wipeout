import pygame,time,random,sys
from pygame.locals import *
from background import time_beg
pygame.init()
width = 800
height = 600
flag_bat_game=0
score=0
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("BUZZ KILL")
icon = pygame.image.load("images/imagesbat/icon.png")
background = pygame.image.load("images/imagesbat/background.png")
end=pygame.image.load("images/imagesbat/end.png")
front=pygame.image.load("images/imagesbat/front.png")
swatter = pygame.image.load("images/imagesbat/swatter.png")
instruction=pygame.image.load("images/imagesbat/instruction.png")
pygame.display.set_icon(icon)
black=(0,0,0)
# setup mixer to avoid sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

clock = pygame.time.Clock()
verysmallfont = pygame.font.SysFont('shonar bangla', 19)
medsmallfont = pygame.font.SysFont(None, 25)
smallfont = pygame.font.SysFont(None, 35)
medfont = pygame.font.SysFont("font/Slim Joe.otf", 70)
largefont = pygame.font.SysFont(None, 100)
verylargefont = pygame.font.SysFont(None, 120)

def text_objects(msg, color, size):
    if size == "verysmall":
        textSurface = verysmallfont.render(msg, True, color)
    elif size == "medsmall":
        textSurface = medsmallfont.render(msg, True, color)
    elif size == "small":
        textSurface = smallfont.render(msg, True, color)
    elif size == "medium":
        textSurface = medfont.render(msg, True, color)
    elif size == "large":
        textSurface = largefont.render(msg, True, color)
    elif size == "verylarge":
        textSurface = verylargefont.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def text_display(msg, color, x_displace, y_displace, size):
    textSurf,textRect = text_objects(msg, color, size)
    textRect.center = (width/2)+x_displace,(height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def text_display_side(msg, color, x_displace, y_displace, size):
    textSurf,textRect = text_objects(msg, color, size)
    textRect.center = x_displace, y_displace
    gameDisplay.blit(textSurf, textRect)

def batgame():
    score = 0
    flag_bat_game=1
    collection_true=1
    mosx=1000
    mosy=1000
    mos = (mosx,mosy)
    kill= True
    while kill:
                gameDisplay.blit(background,(0,0))
                pygame.mouse.set_visible(0)
                check = True
                while check:
                    time_cur=int(time.time())
                    time_end=time_cur - time_beg
                    for event in pygame.event.get():
                        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                            print "a"
                            #pygame.quit()
                            #sys.exit()
                    if time_end >= 40:
                        kill= False
                        gameDisplay.blit(end,(0,0))
                        pygame.display.update()
                        text=str(score)
                        text_display(text,(255,255,255),135,0,"medium")
                        text_display_side("Time Left:"+str(40-time_end),black,700,65,"small")
                        #text_display_side("Time Left:"+str((40000-pygame.time.get_ticks())/1000),black,700,65,"small")
                        pygame.mouse.set_visible(1)
                        pygame.display.update()
                        cur = pygame.mouse.get_pos()
                        time.sleep(5)
                        check=False

                    cur = pygame.mouse.get_pos()
                    gameDisplay.blit(background,(0,0))
                    gameDisplay.blit(swatter,(cur[0],cur[1]))
                    gameDisplay.blit(icon,(mos[0],mos[1]))
                    text_display_side("Score:"+str(score),black,700,25,"small")
                    text_display_side("Time Left:"+str(40-time_end),black,700,65,"small")
                    #text_display_side("Time Left:"+str((40000-pygame.time.get_ticks())/1000),black,700,65,"small")
                    pygame.display.update()
                    if collection_true == 1:
                        mosx=random.randint(0,750)
                        mosy=random.randint(0, 550)
                        mos = (mosx,mosy)
                        pygame.display.update()
                        collection_true=0
                        gameDisplay.blit(icon,(mos[0],mos[1]))
                    if -75 < mos[0] - cur[0] < 75 and -75 < mos[1] - cur[1] < 75:
                        #Sound
                            pygame.mixer.music.load('sound\moskill.wav')
                            pygame.mixer.music.play(0)#0 to play the file only once
                            gameDisplay.blit(background,(0,0))
                            gameDisplay.blit(swatter,(cur[0],cur[1]))
                            score=score+10
                            text_display_side("Score:"+str(score),black,700,25,"medsmall")
                            pygame.display.update()
                            collection_true=1
                            pygame.display.update()
                            check = False
gameDisplay.blit(front,(0,0))
pygame.display.update()
time.sleep(1)
instruction_true= True
while instruction_true:
    gameDisplay.blit(instruction,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RETURN:
            instruction_true = False
batgame()
