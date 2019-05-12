import pygame, pygame.font, pygame.event, pygame.draw, string
import time
import py_compile
from pygame.locals import *
import py_compile
py_compile.compile('room_1.py')


x = pygame.init()
width = 800;
height = 600;
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOZZIE WIPEOUT")
icon = pygame.image.load("images/intro/icon.png")
pygame.display.set_icon(icon)

menu_wallpaper = pygame.image.load("images/intro/menu new.png")
menu_new = pygame.image.load("images/intro/menu ikon1.png")
menu_continue = pygame.image.load("images/intro/menu ikon2.png")
menu_settings = pygame.image.load("images/intro/menu ikon3.png")
menu_about = pygame.image.load("images/intro/menu ikon4.png")
menu_quit = pygame.image.load("images/intro/menu ikon5.png")
quit_img = pygame.image.load("images/intro/quit.png")
quit_yes = pygame.image.load("images/intro/quit ikon yes.png")
quit_no = pygame.image.load("images/intro/quit ikon no.png")
about1 = pygame.image.load("images/intro/about 1.png")
about2 = pygame.image.load("images/intro/about 2.png")
about3 = pygame.image.load("images/intro/about 3.png")
about1_menu = pygame.image.load("images/intro/about choice 1.png")
about1_next = pygame.image.load("images/intro/about choice 2.png")
about2_menu = pygame.image.load("images/intro/about choice 3.png")
about2_back = pygame.image.load("images/intro/about choice 4.png")
about2_next = pygame.image.load("images/intro/about choice 5.png")
about3_menu = pygame.image.load("images/intro/about choice 6.png")
about3_back = pygame.image.load("images/intro/about choice 7.png")
settings_stmt = pygame.image.load("images/intro/settings new1.png")
settings_stmf = pygame.image.load("images/intro/settings new2.png")
settings_sfmf = pygame.image.load("images/intro/settings new3.png")
settings_sfmt = pygame.image.load("images/intro/settings new4.png")
settings_back = pygame.image.load("images/intro/settings new5.png")
dis = pygame.image.load("images/intro/frame for job.png")
intro1 = pygame.image.load("intro_1.png")
intro2 = pygame.image.load("images/intro/intro_2.png")
intro3 = pygame.image.load("images/intro/intro_3.png")
flag=0
#doc = pygame.image.load("doctor.png")

intros = [pygame.image.load("images/intro/1.png"), pygame.image.load("images/intro/2.png"), pygame.image.load("images/intro/3.png"), pygame.image.load("images/intro/4.png"),
          pygame.image.load("images/intro/5.png"), pygame.image.load("images/intro/6.png"), pygame.image.load("images/intro/7.png"), pygame.image.load("images/intro/8.png"), pygame.image.load("images/intro/9.png"),
          pygame.image.load("images/intro/10.png"), pygame.image.load("images/intro/11.png"), pygame.image.load("images/intro/12.png"), pygame.image.load("images/intro/13.png"), pygame.image.load("images/intro/14.png"),
          pygame.image.load("images/intro/15.png"), pygame.image.load("images/intro/16.png"), pygame.image.load("images/intro/17.png")]
char = pygame.image.load("images/intro/1234.png")
char_bright = pygame.image.load("images/intro/123.png")

white = (255,255,255)
black = (0,0,0)
light_red = (255,0,0)
red = (235,0,0)
green = (0,255,0)
dark_green = (0,150,0)
grey = (200,200,200)
light_grey = (211,211,211)
dark_grey = (105,105,105)
yellow = (255,255,0)
light_yellow = (255,255,102)
dark_orange = (255,127,80)
orange = (255,140,0)

clock = pygame.time.Clock()
verysmallfont = pygame.font.SysFont('shonar bangla', 19)
medsmallfont = pygame.font.SysFont(None, 25)
smallfont_adj = pygame.font.SysFont(None, 33)
smallfont = pygame.font.SysFont(None, 35)
medfont = pygame.font.SysFont(None, 70)
largefont = pygame.font.SysFont(None, 100)
verylargefont = pygame.font.SysFont(None, 120)

def text_objects(msg, color, size):
    if size == "verysmall":
        textSurface = verysmallfont.render(msg, True, color)
    elif size == "medsmall":
        textSurface = medsmallfont.render(msg, True, color)
    elif size == "smalladj":
        textSurface = smallfont_adj.render(msg, True, color)
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

def intro():
    game_intro = True
    i = 0
    while game_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_intro = False
                pygame.quit()
                quit()
        for j in range(0, 17):
            gameDisplay.blit(intros[j],(0,0))
            time.sleep(0.25)
            pygame.display.update()
        game_intro = False
    time.sleep(5)

def menu():
    game_menu = True
    while game_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_menu = False
                pygame.quit()
                quit()
        gameDisplay.blit(menu_wallpaper,(0,0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if width*(63.625/100) > cur[0] > width*(35.0/100) and height*(36.83334/100) > cur[1] > height*(27.6667/100):
            gameDisplay.blit(menu_new,(0,0))
            if click[0] == 1:
               entername()
        elif width*(63.625/100) > cur[0] > width*(35.0/100) and height*(50.16667/100) > cur[1] > height*(41.0/100):
            gameDisplay.blit(menu_continue,(0,0))
        elif width*(63.625/100) > cur[0] > width*(35.0/100) and height*(65.0/100) > cur[1] > height*(55.6667/100):
            gameDisplay.blit(menu_settings,(0,0))
            if click[0] == 1:
                    settings()
        elif width*(63.625/100) > cur[0] > width*(35.0/100) and height*(79.0/100) > cur[1] > height*(69.6667/100):
            gameDisplay.blit(menu_about,(0,0))
            if click[0] == 1:
                about_page1()
        elif width*(63.625/100) > cur[0] > width*(35.0/100) and height*(92.6667/100) > cur[1] > height*(83.5/100):
            gameDisplay.blit(menu_quit,(0,0))
            if click[0] == 1:
                game_quit_menu()
        else:
            gameDisplay.blit(menu_wallpaper,(0,0))
        clock.tick(25)
        pygame.display.update()

def intro_game():
    introgame = True
    global flag
##    count = 0
##    a = ["Hi ","DID YOU KNOW?"]
##    b = ["In 2016 alone, there were 1,11,880 cases of dengue fever","and 227 deaths due to dengue.",
##         "Dengue is a viral disease, transmitted by the infective ","bite of a particular mosquito known as Aedes Aegypti.",
##         "They bite us during daytime without our awareness."]
##    c = ["IS YOUR HOUSE AEDES FREE?"]
##    d = ["You are ", "You are in your house during a hot summer afternoon.",
##         "As you move around the house, you will be given some objectives",
##         "to complete. The objectives are sure to entertain you with lots of", "fun and learning.",
##         "So why wait? Let's begin our adventure together!!"]
    while introgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introgame = False
                pygame.quit()
                quit()
        gameDisplay.blit(intro1,(0,0))
        pygame.display.update()
        time.sleep(5)
        gameDisplay.blit(intro2,(0,0))
        pygame.display.update()
        time.sleep(5)
        gameDisplay.blit(intro3,(0,0))
        pygame.display.update()
        cur = pygame.mouse.get_pos()
        print cur[0], cur[1]
        count=0
        while count < 25:
            time.sleep(0.25)
            text_display("Click Enter to continue....", dark_orange, 0, (height/2)*(85.0/100), "medsmall")
            pygame.display.update()
            time.sleep(0.25)
            text_display("Click Enter to continue....", orange, 0, (height/2)*(85.0/100), "medsmall")
            pygame.display.update()
            count= count+1
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return 0
                                        #gameDisplay.fill(black)
                    #pygame.draw.rect(gameDisplay, grey, [width*(1.1628/100),height*(1.6667/100),width*(97.6745/100),height*(96.6667/100)])
                    #pygame.draw.rect(gameDisplay, black, [width*(1.74419/100),height*(2.5/100),width*(96.51163/100),height*(95.0/100)])





#        time.sleep(10)
 #       clock.tick(10)
#        pygame.display.update()

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(gameDisplay, message):
  gameDisplay.blit(dis,(0,0))
  pygame.draw.rect(gameDisplay, grey, [width*(43.75/100),height*(40.83334/100),width*(37.5/100),height*(6.6667/100)])
  if len(message) != 0:
    gameDisplay.blit(smallfont.render(message, True, orange),(128, 251))
  pygame.display.flip()

def ask(gameDisplay, question):
  current_string = []
  display_box(gameDisplay, question + ":    " + string.join(current_string,""))
  while True:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(gameDisplay, question + ":    " + string.join(current_string,""))
  return string.join(current_string,"")

def char_sel():
    char_trans = pygame.transform.scale(char,(250,450))
    char_bright_trans = pygame.transform.scale(char,(250,450))
    gintro = True
    while gintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gintro = False
                pygame.quit()
                quit()
        gameDisplay.blit(dis,(0,0))
        text_display("SELECT  A  CHARACTER", orange, 0, -(height/2)*(75.0/100), "medium")
        pygame.draw.rect(gameDisplay, black, [width*(49.6875/100),height*(20.83334/100),width*(0.625/100),height*(73.3334/100)])
        gameDisplay.blit(char_trans,(width*(59.375/100),height*(20.83334/100)))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print cur[0], cur[1]
        if width*(61.875/100) < cur[0] < width*(88.125/100) and height*(19.16667/100) < cur[1] < height*(92.5/100):
            gameDisplay.blit(char_bright_trans,(width*(59.375/100),height*(20.83334/100)))
            if click[0] == 1 and flag ==0:
                intro_game()
        import room_1
        pygame.display.update()

def entername():
    global l
    l = ask(gameDisplay, "Enter your Name")
    char_sel()

def settings():
    game_settings = True
    music = True
    sound  = True
    while game_settings:
        check = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_settings = False
                pygame.quit()
                quit()
        gameDisplay.blit(settings_stmt,(0,0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if width*(97.25/100) > cur[0] > width*(85.75/100) and height*(95.6667/100) > cur[1] > height*(86.83334/100):
            check = False
            if click[0] == 1:
                menu()

        if width*(76.625/100) > cur[0] > width*(67.125/100) and height*(67.3334/100) > cur[1] > height*(59.16667/100):
            if click[0] == 1:
                music = True
        elif width*(87.875/100) > cur[0] > width*(78.375/100) and height*(67.3334/100) > cur[1] > height*(59.16667/100):
            if click[0] == 1:
                music = False
        elif width*(76.625/100) > cur[0] > width*(67.125/100) and height*(45.83334/100) > cur[1] > height*(37.83334/100):
            if click[0] == 1:
                sound = True
        elif width*(87.875/100) > cur[0] > width*(78.375/100) and height*(45.83334/100) > cur[1] > height*(37.83334/100):
            if click[0] == 1:
                sound = False

        if music == True and sound == True:
            gameDisplay.blit(settings_stmt,(0,0))

        elif music == False and sound == True:
            gameDisplay.blit(settings_stmf,(0,0))

        elif music == False and sound == False:
            gameDisplay.blit(settings_sfmf,(0,0))

        elif music == True and sound == False:
            gameDisplay.blit(settings_sfmt,(0,0))

        if check == False:
            gameDisplay.blit(settings_back,(0,0))
        clock.tick(10)
        pygame.display.update()

def about_page1():
    game_aboutpage_1 = True
    while game_aboutpage_1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_aboutpage_1 = False
                pygame.quit()
                quit()
        gameDisplay.blit(about1,(0,0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if width*(15.0/100) > cur[0] > width*(3.5/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about1_menu,(0,0))
            if click[0] == 1:
                  menu()
        elif width*(96.5/100) > cur[0] > width*(84.75/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about1_next,(0,0))
            if click[0] == 1:
               about_page2()
               continue
        else:
             gameDisplay.blit(about1,(0,0))
        clock.tick(10)
        pygame.display.update()


def about_page2():
    game_aboutpage_2 = True
    while game_aboutpage_2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_aboutpage_2 = False
                pygame.quit()
                quit()
        gameDisplay.blit(about2,(0,0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if width*(15.0/100) > cur[0] > width*(3.5/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about2_menu,(0,0))
            if click[0] == 1:
               menu()
        elif width*(83.0/100) > cur[0] > width*(71.25/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about2_back,(0,0))
            if click[0] == 1:
                about_page1()
                continue
        elif width*(96.5/100) > cur[0] > width*(84.75/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about2_next,(0,0))
            if click[0] == 1:
                about_page3()
                continue
        else:
             gameDisplay.blit(about2,(0,0))
        clock.tick(10)
        pygame.display.update()

def about_page3():
    game_aboutpage_3 = True
    while game_aboutpage_3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_aboutpage_3 = False
                pygame.quit()
                quit()
        gameDisplay.blit(about3,(0,0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if width*(15.0/100) > cur[0] > width*(3.5/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about3_menu,(0,0))
            if click[0] == 1:
                  menu()
        elif width*(96.5/100) > cur[0] > width*(84.75/100) > width*(79.0698/100) and height*(96.83334/100) > cur[1] > height*(88.83334/100):
            gameDisplay.blit(about3_back,(0,0))
            if click[0] == 1:
               about_page2()
               continue
        else:
            gameDisplay.blit(about3,(0,0))
        clock.tick(10)
        pygame.display.update()


def game_quit_menu():
    global check
    game_quit = True
    while game_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = False
                pygame.quit()
                quit()
        gameDisplay.blit(quit_img,(0,0))
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if width*(33.0/100) > cur[0] > width*(19.5/100) and height*(65.83334/100) > cur[1] > height*(53.5/100):
            gameDisplay.blit(quit_yes,(0,0))
            if click[0] == 1:
                pygame.quit()
                quit()
        elif width*(78.625/100) > cur[0] > width*(65.0/100) and height*(65.83334/100) > cur[1] > height*(53.5/100):
            gameDisplay.blit(quit_no,(0,0))
            if click[0] == 1:
                menu()

        else:
            gameDisplay.blit(quit_img,(0,0))
        clock.tick(10)
        pygame.display.update()

#intro()
menu()
pygame.quit()
quit()
