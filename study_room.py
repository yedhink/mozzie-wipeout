import pygame
from time import sleep, time
import py_compile
from pygame.locals import *
import py_compile
py_compile.compile('background.py')


#******* HOPE IS A GOOD THING. AND NO GOOD THING EVER DIES ********#

#intaitlize Pygame library
pygame.init()

#creating a basic window for our work
window = pygame.display.set_mode((800,600))

#setting intial co-ordiantes for our character in the window
playerX=124
playerY=496

#Setting the range within which the character can move around
minT_x=20
maxT_x=704
#minR_x=120
minR_x=152
#maxR_x=604
maxR_x=544
#minR_y=408
minR_y=352
#minR_y=0
maxR_y=508

#while running check top of the screen in title bar
pygame.display.set_caption("Mozzi Kill")

#Colors are detected by these values..storing them to a variable
black = (0,0,0)
white = (255,255,255)
cream = (245,245,245)
red = (235,35,35)
light_red = (255,0,0)
green = (0,255,0)
dark_green = (0,150,0)

verysmallfont = pygame.font.SysFont(None, 20)
smallfont = pygame.font.SysFont(None, 35)
medfont = pygame.font.SysFont(None, 70)
largefont = pygame.font.SysFont(None, 100)
verylargefont = pygame.font.SysFont(None, 130)

#accesing in bulit pygame clock
clock = pygame.time.Clock()

#declaring cash and count as global
count=[]
with open("count.txt", "r") as f:
        for line in f:
            count.append(int(line.strip()))
f.close()
with open("cash.txt", "r") as f:
        for line in f:
            cash=int(line.strip())
if count==None:
    count = [0]*50
if cash==None:
    cash=5000

cue=-1
question=1

flag_back=0
flag_item1=0
flag_item2=0

def area(x1,y1,x2,y2,x3,y3):
    return abs(((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2)))/2.0)

area_t1 = area(minT_x,maxR_y,minR_x,maxR_y,minR_x,minR_y)
area_t2 = area(maxR_x,maxR_y,maxT_x,maxR_y,maxR_x,minR_y)

def text_objects(msg, color, size):
    if size == "verysmall":
        textSurface = verysmallfont.render(msg, True, color)
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
    textRect.center = (800/2)+x_displace,(600/2)+y_displace
    window.blit(textSurf, textRect)

def shop():
    global cash
    pygame.event.clear()
    t=0

    game_shop = True
    while game_shop:
        pygame.event.wait()
        if event.type == pygame.QUIT:
            game_shop = False
            exit(0)

        window.blit(shop_1,(0,0))
        window.blit(shop_cash,(0,0))

        cur_shop = pygame.mouse.get_pos()
        click_shop = pygame.mouse.get_pressed()
        #print "MX shop-",cur_shop[0],"MY shop-",cur_shop[1],"click_shop",click_shop
        text_display(str(cash),black,340,-263,"small")
        #Back option
        if 786 > cur_shop[0] > 697  and 590 > cur_shop[1] > 545 :
            if click_shop[0] == 1:
                return 0

        #Buy options
        if 55<cur_shop[0]<300 and 100<cur_shop[1]<150:
            if click_shop[0] == 1:
                scroll_shop(1)
                return 0

        if 55<cur_shop[0]<300 and 155<cur_shop[1]<210:
            if click_shop[0] == 1:
                scroll_shop(2)
                return 0

        if 55<cur_shop[0]<300 and 215<cur_shop[1]<270:
            if click_shop[0] == 1:
                scroll_shop(3)
                return 0

        if 55<cur_shop[0]<300 and 275<cur_shop[1]<330:
            if click_shop[0] == 1:
                scroll_shop(4)
                return 0

        if 55<cur_shop[0]<300 and 335<cur_shop[1]<390:
            if click_shop[0] == 1:
                scroll_shop(5)
                return 0

        if 55<cur_shop[0]<300 and 400<cur_shop[1]<450:
            if click_shop[0] == 1:
                scroll_shop(6)
                return 0

        if 55<cur_shop[0]<300 and 455<cur_shop[1]<510:
            if click_shop[0] == 1:
                scroll_shop(7)
                return 0

        if 55<cur_shop[0]<300 and 515<cur_shop[1]<570:
            if click_shop[0] == 1:
                scroll_shop(8)
                return 0

        if t==1:
            return 0

        pygame.display.update()


def scroll_shop(id):
    global cash
    pygame.event.clear()
    game_scr = True
    while game_scr:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            game_scr = False
            exit(0)

        window.blit(shop_1,(0,0))
        window.blit(shop_cash,(0,0))

        cur_scroll_shop = pygame.mouse.get_pos()
        click_scroll_shop = pygame.mouse.get_pressed()
        #print "MX scr-",cur_scroll_shop[0],"MY scr-",cur_scroll_shop[1],"click_scroll_shop",click_scroll_shop
        text_display(str(cash),black,340,-263,"small")
        #Back option
        if 786 > cur_scroll_shop[0] > 697  and 590 > cur_scroll_shop[1] > 545 :
            if click_scroll_shop[0] == 1:
                return 0

        if id==1:
            window.blit(shop_detail1,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=600:
                        cash=cash-600
                        count[0]=count[0]+1
                    return 0
        if id==2:
            window.blit(shop_detail2,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=1000:
                        cash=cash-1000
                        count[1]=count[1]+1
                    return 0
        if id==3:
            window.blit(shop_detail3,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=100:
                        cash=cash-100
                        count[2]=count[2]+1
                    return 0
        if id==4:
            window.blit(shop_detail4,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=250:
                        cash=cash-250
                        count[3]=count[3]+1
                    return 0


        if id==5:
            window.blit(shop_detail5,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=18:
                        cash=cash-18
                        count[4]=count[4]+1
                    return 0

        if id==6:
            window.blit(shop_detail6,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=300:
                        cash=cash-300
                        count[5]=count[5]+1
                    return 0

        if id==7:
            window.blit(shop_detail7,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=100:
                        cash=cash-100
                        count[6]=count[6]+1
                    return 0

        if id==8:
            window.blit(shop_detail8,(0,0))
            if 751 >cur_scroll_shop[0]> 670 and 500 >cur_scroll_shop[1]> 454:
                if click_scroll_shop[0]==1:
                    if cash>=10:
                        cash=cash-10
                        count[7]=count[7]+1
                    return 0

        pygame.display.update()

def inventory():
    use=0
    game_inventory = True
    pygame.event.clear()
    while game_inventory:
        event=pygame.event.wait()
        if event.type == pygame.QUIT:
            game_inventory = False

        window.blit(inventory1,(0,0))

        cur_inv = pygame.mouse.get_pos()
        click_inventory = pygame.mouse.get_pressed()
        #print "MX inv",cur_inv[0],"MY inv-",cur_inv[1]

        text_display(str(count[0]),black,60,-176,"small")
        text_display(str(count[1]),black,60,-116,"small")
        text_display(str(count[2]),black,60,-56,"small")
        text_display(str(count[3]),black,60,4,"small")
        text_display(str(count[4]),black,60,64,"small")
        text_display(str(count[5]),black,60,124,"small")
        text_display(str(count[6]),black,60,184,"small")
        text_display(str(count[7]),black,60,244,"small")
        #Back option
        if 786 > cur_inv[0] > 697  and 590 > cur_inv[1] > 545 :
            if click_inventory[0] == 1:
                return 0

        #Use options
        if 645<cur_inv[0]<725 and 100<cur_inv[1]<150:
            if click_inventory[0] == 1:
                if count[0]>0:
                    count[0]-=1
                    return 1
                else:
                    text_display("Buy from shop 1st",black,100,-90,"small")


        if 645<cur_inv[0]<725 and 161<cur_inv[1]<206:
            if click_inventory[0] == 1:
                text_display("Not usable in this room",black,100,20,"small")


        if 645<cur_inv[0]<725 and 220<cur_inv[1]<265:
            if click_inventory[0] == 1:
                if count[2] > 0:
                    count[2]=count[2]-1
                    return 3
                else:
                    text_display("Buy item from shop first",black,100,-90,"small")

        if  645<cur_inv[0]<725 and 275<cur_inv[1]<322:
            if click_inventory[0] == 1:
                text_display("Not usable in this room",black,100,20,"small")


        if 645<cur_inv[0]<725 and 340<cur_inv[1]<385:
            if click_inventory[0] == 1:
                text_display("Not usable in this room",black,100,20,"small")


        if 645<cur_inv[0]<725 and 400<cur_inv[1]<445:
            if click_inventory[0] == 1:
                text_display("Not usable in this room",black,100,20,"small")



        if 645<cur_inv[0]<725 and 460<cur_inv[1]<505:
            if click_inventory[0] == 1:
                if count[6] > 0:
                    count[6]=count[6]-1
                    return 2
                else:
                    text_display("Buy item from shop first",black,100,-90,"small")


        if 645<cur_inv[0]<725 and 515<cur_inv[1]<565:
            if click_inventory[0] == 1:
                text_display("Not usable in this room",black,100,20,"small")

        pygame.display.update()


def quiz11():
    m=0
    global cue
    global flag_back
    game_quiz = True
    while game_quiz:
        event = pygame.event.wait()
        if event.type == pygame.QUIT or m==1:
            game_quiz = False
            cue=8
            render()

        cur_quiz= pygame.mouse.get_pos()
        click_quiz = pygame.mouse.get_pressed()

        window.blit(quiz1,(0,0))
        if 237 > cur_quiz[0] > 41  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("CHOOSE BETTER",red,-260,225,"small")
                text_display("OPTION",red,-260,250,"small")
        if 491 > cur_quiz[0] > 303  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("CHOOSE BETTER",red,0,225,"small")
                text_display("OPTION",red,0,250,"small")
        if 751 > cur_quiz[0] > 557  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                flag_back=1


        if flag_back==1 or m!=0:
            window.blit(quiz1c,(0,0))

            cur_quiz= pygame.mouse.get_pos()
            #print "MX quiz1-",cur_quiz[0],"MY quiz1-",cur_quiz[1]

            if 778 > cur_quiz[0] > 674  and 590 > cur_quiz[1] > 542:
                    if click_quiz[0]==1:
                        m=quiz22()
                        return 1
            pygame.display.update()
	pygame.display.update()
    return 1
    #if m==1:
        #return 0

def quiz22():
    m=0
    global flag_back
    game_quiz = True
    pygame.event.clear()
    while game_quiz:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            game_quiz = False
            return 1


        cur_quiz= pygame.mouse.get_pos()
        click_quiz = pygame.mouse.get_pressed()

        window.blit(quiz2,(0,0))
        if 237 > cur_quiz[0] > 41  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                flag_back=2
        if 491 > cur_quiz[0] > 303  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("WRONG ANSWER",red,0,225,"small")
        if 751 > cur_quiz[0] > 557  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("WRONG ANSWER",red,255,225,"small")


        if flag_back==2:
            window.blit(quiz2c,(0,0))

            cur_quiz= pygame.mouse.get_pos()
            #print "MX quiz1-",cur_quiz[0],"MY quiz1-",cur_quiz[1]

            if 778 > cur_quiz[0] > 674  and 590 > cur_quiz[1] > 542:
                    if click_quiz[0]==1:
                          m=quiz33()
                          return 1
            pygame.display.update()
	pygame.display.update()
    #if m==1:
        #return 1

def quiz33():
    m=0
    global flag_back
    game_quiz = True
    pygame.event.clear()
    while game_quiz:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            game_quiz = False
            exit(0)

        cur_quiz= pygame.mouse.get_pos()
        click_quiz = pygame.mouse.get_pressed()

        window.blit(quiz3,(0,0))
        if 237 > cur_quiz[0] > 41  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("CHOOSE BETTER",red,-260,225,"small")
                text_display("OPTION",red,-260,250,"small")
        if 491 > cur_quiz[0] > 303  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("CHOOSE BETTER",red,0,225,"small")
                text_display("OPTION",red,0,250,"small")
        if 751 > cur_quiz[0] > 557  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                flag_back=3


        if flag_back==3:
            window.blit(quiz3c,(0,0))


            cur_quiz= pygame.mouse.get_pos()
            #print "MX quiz1-",cur_quiz[0],"MY quiz1-",cur_quiz[1]

            if 778 > cur_quiz[0] > 674  and 590 > cur_quiz[1] > 542:
                    if click_quiz[0]==1:
                          m=quiz44()
                          return 0
            pygame.display.update()
	pygame.display.update()


def quiz44():
    m=0
    global flag_back
    game_quiz = True
    pygame.event.clear()
    while game_quiz:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            game_quiz = False
            exit(0)

        cur_quiz= pygame.mouse.get_pos()
        click_quiz = pygame.mouse.get_pressed()

        window.blit(quiz4,(0,0))
        if 237 > cur_quiz[0] > 41  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("WRONG ANSWER",red,-260,225,"small")
        if 491 > cur_quiz[0] > 303  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                flag_back=4
        if 751 > cur_quiz[0] > 557  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("WRONG ANSWER",red,255,225,"small")


        if flag_back==4:
            window.blit(quiz4c,(0,0))


            cur_quiz= pygame.mouse.get_pos()
            #print "MX quiz1-",cur_quiz[0],"MY quiz1-",cur_quiz[1]

            if 778 > cur_quiz[0] > 674  and 590 > cur_quiz[1] > 542:
                    if click_quiz[0]==1:
                          m=quiz55()
                          return 0
	    pygame.display.update()
        pygame.display.update()
    #if m==1:
        #return 1



def quiz55():
    m=0
    global flag_back
    game_quiz = True
    pygame.event.clear()
    while game_quiz:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            game_quiz = False
            exit(0)


        cur_quiz= pygame.mouse.get_pos()
        click_quiz = pygame.mouse.get_pressed()

        window.blit(quiz5,(0,0))
        if 237 > cur_quiz[0] > 41  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("WRONG ANSWER",red,-260,225,"small")
        if 491 > cur_quiz[0] > 303  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                text_display("WRONG ANSWER",red,255,225,"small")
        if 751 > cur_quiz[0] > 557  and 386 > cur_quiz[1] > 251:
            if click_quiz[0]==1:
                flag_back=5


        if flag_back==5:
            window.blit(quiz5c,(0,0))
            cur_quiz= pygame.mouse.get_pos()
            #print "MX quiz1-",cur_quiz[0],"MY quiz1-",cur_quiz[1]

            if 778 > cur_quiz[0] > 674  and 590 > cur_quiz[1] > 542:
                    if click_quiz[0]==1:
                          return 1
	    pygame.display.update()
        pygame.display.update()


#Defining a class Sprite....not a Pygame library or anyhting..simply a class named Sprite
class Sprite:
    #DONT bother about the parameters...just iniatalizing
    def __init__(self,x,y,width,height):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.images=[]
        self.check=0
        self.check_net=0
        self.allow=0
    #Rendering
    #index    either:- 0 or 1 (index of list of character images)
    def render(self,index):
            global cue
            m=0
        #initially display the image of room at (0,0)
            window.blit(img_room,(0,0))
            click_render = pygame.mouse.get_pressed()

            #playerX, playerY are globally available cordiantes of character movement...
            window.blit(self.images[index],(playerX,playerY))


            if self.allow ==3 and cue !=8:
                pygame.draw.rect(window, red, [416,192,200,50])
                text_display("Objective",black,100,-80,"small")
                if 416<cur[0]<540 and 192<cur[1]<242:
                    pygame.draw.rect(window,black,[360,192,270,50])
                    text_display("Use Quiz Book From Shop",white,100,-80,"verysmall")

            if self.allow==7 and cue!=8:
                pygame.draw.rect(window, red, [416,192,200,50])
                text_display("Objective",black,100,-80,"small")
                if 416<cur[0]<540 and 192<cur[1]<242:
                    pygame.draw.rect(window,black,[360,192,270,50])
                    text_display("Go to the Table and Attempt The Quiz",white,100,-80,"verysmall")


            elif cue==8:
                pygame.draw.rect(window, red, [235,250,105,15])
                text_display("Next Objective",black,-112.5,-42.5,"verysmall")

            #Shop Option in Main
            text_display("SHOP",black,-300,-250,"small")
            if 20<cur[0]<170 and 20<cur[1]<70:
                pygame.draw.rect(window,cream,[20,20,150,50])
                text_display("SHOP",black,-300,-250,"small")
                if click_render[0] == 1:
                    shop()

            #Inventory Option in Main
            pygame.draw.rect(window,white,[630,20,150,50])
            text_display("INVENTORY",black,305,-250,"small")
            if 630<cur[0]<780 and 20<cur[1]<70:
                pygame.draw.rect(window,cream,[630,20,150,50])
                text_display("INVENTORY",black,305,-250,"small")
                if click_render[0] == 1:
                    self.check = inventory()

            #Blitting of images after we clcik on Use button
            if self.check!=0:

                #placing window net
                if self.check ==1 and self.allow == 0:
                    self.allow=1

                if self.check ==1 and self.allow==2:
                    self.allow=3

                if self.check ==1 and self.allow==4:
                    self.allow=5

                if self.check ==1 and self.allow == 6:
                    self.allow=7


                #placing Repellent
                if self.check == 3 and self.allow == 0:
                    self.allow=2

                if self.check ==3 and self.allow==1:
                    self.allow=3

                if self.check == 3 and self.allow == 4:
                    self.allow=6

                if self.check ==3 and self.allow == 5:
                    self.allow=7

                #placing bed net
                if self.check == 2 and self.allow == 0:
                    self.allow=4

                if self.check ==2 and self.allow==1:
                    self.allow=5

                if self.check == 2 and self.allow == 2:
                    self.allow=6

                if self.check ==2 and self.allow == 3:
                    self.allow=7


            if self.allow==1:
                    window.blit(net_right,(0,0))
                    window.blit(net_left,(0,0))

            if self.allow==2:
                    window.blit(rep1,(0,0))

            if self.allow==3:
                    window.blit(net_right,(0,0))
                    window.blit(net_left,(0,0))
                    window.blit(rep1,(0,0))

            if self.allow==4:
                    window.blit(book1,(0,0))

            if self.allow==5:
                    window.blit(net_right,(0,0))
                    window.blit(net_left,(0,0))
                    window.blit(book1,(0,0))

            if self.allow==6:
                    window.blit(book1,(0,0))
                    window.blit(rep1,(0,0))

            if self.allow==7:
                    window.blit(net_right,(0,0))
                    window.blit(net_left,(0,0))
                    window.blit(book1,(0,0))
                    window.blit(rep1,(0,0))

            if cue!=8:
                    cue=self.allow


            #CAlling quiz fuction

            if cue==7 and playerY==352:
                cue=8
                quiz11()
                #print "\n return render=",cue

            pygame.display.update()


#main() begins
#loading an image into a variable
img_char13=pygame.image.load("images/images/f1.png").convert_alpha()
img_char13=pygame.transform.scale(img_char13,(100,110))

img_char14=pygame.image.load("images/images/f2.png").convert_alpha()
img_char14=pygame.transform.scale(img_char14,(100,110))
#loading room
img_room=pygame.image.load("images/images/room_draw.png").convert_alpha()
img_room=pygame.transform.scale(img_room,(800,600))

#loading net....blit the image at (0,0) 1st and then edit positoning
net_right=pygame.image.load("images/images/net_right.png").convert_alpha()
net_left=pygame.image.load("images/images/net_left.png").convert_alpha()

#net_org=pygame.image.load("net_org.jpg").convert_alpha()
net_org=pygame.transform.scale(net_left,(450,350))

#Shop images
shop_1=pygame.image.load("images/images/shop new.png").convert_alpha()
shop_detail1=pygame.image.load("images/images/shop_detail1.png").convert_alpha()
shop_detail2=pygame.image.load("images/images/shop_detail2.png").convert_alpha()
shop_detail3=pygame.image.load("images/images/shop_detail3.png").convert_alpha()
shop_detail4=pygame.image.load("images/images/shop_detail4.png").convert_alpha()
shop_detail5=pygame.image.load("images/images/shop_detail5.png").convert_alpha()
shop_detail6=pygame.image.load("images/images/shop_detail6.png").convert_alpha()
shop_detail7=pygame.image.load("images/images/shop_detail7.png").convert_alpha()
shop_detail8=pygame.image.load("images/images/shop_detail8.png").convert_alpha()
shop_cash=pygame.image.load("images/images/shop cash.png").convert_alpha()
#Inventory images
inventory1=pygame.image.load("images/images/inventory.png").convert_alpha()

#Repellent images
rep1=pygame.image.load("images/images/repellent1.png").convert_alpha()

#book image
book1=pygame.image.load("images/images/book1.png").convert_alpha()

#Quiz images
quiz_next=pygame.image.load("images/images/quiz next.png").convert_alpha()

quiz1c=pygame.image.load("images/images/quiz 1 cor new.png").convert_alpha()
quiz2c=pygame.image.load("images/images/quiz 2 new cor.png").convert_alpha()
quiz3c=pygame.image.load("images/images/quiz 3 new cor.png").convert_alpha()
quiz4c=pygame.image.load("images/images/quiz 4 new cor.png").convert_alpha()
quiz5c=pygame.image.load("images/images/quiz 5 new cor.png").convert_alpha()

quiz1=pygame.image.load("images/images/quiz 1.png").convert_alpha()
quiz2=pygame.image.load("images/images/quiz 2.png").convert_alpha()
quiz3=pygame.image.load("images/images/quiz 3.png").convert_alpha()
quiz4=pygame.image.load("images/images/quiz 4.png").convert_alpha()
quiz5=pygame.image.load("images/images/quiz 5.png").convert_alpha()



#Creating a class object of class Sprite
Sprite1=Sprite(0,0,0,0)

Sprite1.images.append(img_char13)
Sprite1.images.append(img_char14)

#variables to detect movement from keyboard
moveX,moveY=0,0

gameLoop=True

#Holds index of the list "images" for character
c=0


#Time event in displaying the two cahracter images:- ("12.png","15.png")
RESETEVENT = pygame.USEREVENT + 1

#GAMELOOP FOR COLLISON AND IMGAE RENDERING
#gameLoop intially True so as to run the loop and will become false when pygame.QUIT is the event
while gameLoop:
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #pygame.event.get() will take whatever sorta movement or thing we do in interface
    #this for loop runs and decides what kinda event has happened on our window
    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

        #Keydown() to check whether we have pressed a key in keyboard
        if (event.type==pygame.KEYDOWN):

            pygame.time.set_timer(RESETEVENT, 10000)
            #Checks whetther the input key is left arrow from keyboard or not
            if (event.key==pygame.K_LEFT):
                #shows the direction and number of points we need to move in Y axis
                moveX = -4
                Sprite1.images=[]
                #loading an image into a variable
                img_char1=pygame.image.load("images/images/l1.png").convert_alpha()
                img_char1=pygame.transform.scale(img_char1,(100,110))

                img_char2=pygame.image.load("images/images/l3.png").convert_alpha()
                img_char2=pygame.transform.scale(img_char2,(100,110))

                img_char3=pygame.image.load("images/images/l5.png").convert_alpha()
                img_char3=pygame.transform.scale(img_char3,(100,110))

                img_char4=pygame.image.load("images/images/l7.png").convert_alpha()
                img_char4=pygame.transform.scale(img_char4,(100,110))

                Sprite1.images.append(img_char1)
                Sprite1.images.append(img_char2)
                Sprite1.images.append(img_char3)
                Sprite1.images.append(img_char4)


            if (event.key==pygame.K_RIGHT):
                moveX = 4
                Sprite1.images=[]
                #loading an image into a variable
                img_char5=pygame.image.load("images/images/r1.png").convert_alpha()
                img_char5=pygame.transform.scale(img_char5,(100,110))

                img_char6=pygame.image.load("images/images/r3.png").convert_alpha()
                img_char6=pygame.transform.scale(img_char6,(100,110))

                img_char7=pygame.image.load("images/images/r5.png").convert_alpha()
                img_char7=pygame.transform.scale(img_char7,(100,110))

                img_char8=pygame.image.load("images/images/r7.png").convert_alpha()
                img_char8=pygame.transform.scale(img_char8,(100,110))

                Sprite1.images.append(img_char5)
                Sprite1.images.append(img_char6)
                Sprite1.images.append(img_char7)
                Sprite1.images.append(img_char8)

            if (event.key==pygame.K_UP):
                moveY = -4
                Sprite1.images=[]
                #loading an image into a variable
                img_char9=pygame.image.load("images/images/b1.png").convert_alpha()
                img_char9=pygame.transform.scale(img_char9,(100,110))

                img_char10=pygame.image.load("images/images/b2.png").convert_alpha()
                img_char10=pygame.transform.scale(img_char10,(100,110))

                img_char11=pygame.image.load("images/images/b1.png").convert_alpha()
                img_char11=pygame.transform.scale(img_char11,(100,110))

                img_char12=pygame.image.load("images/images/b2.png").convert_alpha()
                img_char12=pygame.transform.scale(img_char12,(100,110))

                Sprite1.images.append(img_char9)
                Sprite1.images.append(img_char10)
                Sprite1.images.append(img_char11)
                Sprite1.images.append(img_char12)


            if (event.key==pygame.K_DOWN):
                moveY = 4
                Sprite1.images=[]
                #loading an image into a variable
                img_char13=pygame.image.load("images/images/f1.png").convert_alpha()
                img_char13=pygame.transform.scale(img_char13,(100,110))

                img_char14=pygame.image.load("images/images/f2.png").convert_alpha()
                img_char14=pygame.transform.scale(img_char14,(100,110))

                img_char15=pygame.image.load("images/images/f1.png").convert_alpha()
                img_char15=pygame.transform.scale(img_char15,(100,110))

                img_char16=pygame.image.load("images/images/f2.png").convert_alpha()
                img_char16=pygame.transform.scale(img_char16,(100,110))

                Sprite1.images.append(img_char13)
                Sprite1.images.append(img_char14)
                Sprite1.images.append(img_char15)
                Sprite1.images.append(img_char16)

        #Keyup() to check whether we have lifted fingers off the key we pressed in keyboard
        if (event.type==pygame.KEYUP):

            pygame.time.set_timer(RESETEVENT, 10000)
            #we havent pressed anything so no need to move...thus moveX,Y=0
            if (event.key==pygame.K_LEFT):

                moveX=0

            if (event.key==pygame.K_RIGHT):

                moveX=0

            if (event.key==pygame.K_UP):

                moveY=0

            if (event.key==pygame.K_DOWN):

                moveY=0

        #For number of frames per sec
        if (event.type==RESETEVENT):

            pygame.time.set_timer(RESETEVENT, 0)

    #continuation of gameloop
    #just prividing a color to our screen...if there are no images loaded then useful
    window.fill(black)

    #check intial value of playerX,playerY.....this is how we move our image on the screen..
    playerX+=moveX

    playerY+=moveY

    #Collision ALGORITHM for the traingular parts adjoined to the rectangle on either sides
    if playerX<=minR_x:
        a1 = area(minT_x,maxR_y,minR_x,maxR_y,playerX,playerY)
        a2 = area(minR_x,maxR_y,minR_x,minR_y,playerX,playerY)
        a3 = area(minR_x,minR_y,minT_x,maxR_y,playerX,playerY)
        #to check whether the point is outside the traingle or not
        if a1+a2+a3 != area_t1:
            #so the point is outside traingle on left side
            if moveY<0:#if we had pressed the UP key then moveY = -4
                playerY=playerY - moveY
            playerX=playerX - moveX


    elif playerX>=maxR_x:
        a1 = area(maxR_x,maxR_y,maxT_x,maxR_y,playerX,playerY)
        a2 = area(maxT_x,maxR_y,maxR_x,minR_y,playerX,playerY)
        a3 = area(maxR_x,minR_y,maxR_x,maxR_y,playerX,playerY)
        if a1+a2+a3 != area_t2:
            if moveY<0:
                playerY=playerY - moveY
            playerX=playerX - moveX


    #Collision ALGORITHM for the rectangular part only
    if(playerY>maxR_y):
        playerY=playerY - moveY
    elif(playerY<minR_y):
        if playerY==320:
            playerX=playerX - moveX
            if cue==8:
                #Saving the the count of items we bought and cash used in this room to files
                import background

        if(playerX<=220 or playerX>=240):
                playerX=playerX - moveX
                playerY=playerY - moveY

        if(playerY<320):
                if moveY<0:
                    playerY=playerY - moveY


    #To display Co-ordinates of our character in command window
    #print "X-",playerX,"Y-",playerY
    #print "MX-",cur[0],"MY-",cur[1]


    #checking range
    #if(minR_x<playerX<maxR_x and minR_y<playerY<maxR_y):
    #only 2 images are stored in our list "images[]"..therefore "c" should take only  values 0,1
    if(event.type==pygame.KEYDOWN):

        if c==4:
          c=0
        #calling render function of class object
        Sprite1.render(c)
        #incrementing index of list
        c=c+1
    else:

        Sprite1.render(0)

    #to update the screen...a core function
    pygame.display.flip()

    #50 millisecs delay
    clock.tick(50)

pygame.quit()
