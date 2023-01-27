import pygame
import os

WIDTH, HEIGHT = 1200, 750
White = (255,255,255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emoji Trivia")

FPS = 60
DW_HALF = WIDTH/2
DH_HALF = HEIGHT/2
DISPLAY_AREA = WIDTH*HEIGHT

#--------------------------------------------Main-Frame--------------------------------------------------#

bgimg = pygame.image.load(os.path.join('images', 'bg1.png'))
bgimg1 = pygame.image.load(os.path.join('imgl', 'in-love.png'))
bgimg2 = pygame.image.load(os.path.join('imgl', 'cool.png'))
bgimg3 = pygame.image.load(os.path.join('imgl', 'star.png'))
bgimg4 = pygame.image.load(os.path.join('imgl', 'love.png'))
bgimg5 = pygame.image.load(os.path.join('imgl', 'wow.png'))
bgimg6 = pygame.image.load(os.path.join('imgl', 'party.png'))
bgimg7 = pygame.image.load(os.path.join('imgl', 'cool1.png'))
bgimg8 = pygame.image.load(os.path.join('imgl', 'emoji.png'))

startimg = pygame.image.load(os.path.join('imgl','startbutton.png'))
exitimg = pygame.image.load(os.path.join('imgl','exit.png'))


bgimg1=pygame.transform.scale(bgimg1,(100, 100))
bgimg2=pygame.transform.scale(bgimg2,(100, 100))
bgimg3=pygame.transform.scale(bgimg3,(100, 100))
bgimg4=pygame.transform.scale(bgimg4,(100, 100))
bgimg5=pygame.transform.scale(bgimg5,(100, 100))
bgimg6=pygame.transform.scale(bgimg6,(100, 100))
bgimg7=pygame.transform.scale(bgimg7,(100, 100))
bgimg8=pygame.transform.scale(bgimg8,(100, 100))
startimg=pygame.transform.scale(startimg,(100,100))
exitimg=pygame.transform.scale(exitimg,(100,80))


dimimg1 = bgimg1.get_rect()
dimimg5 = bgimg5.get_rect()

direction = 1



def draw_window():
    WIN.fill(White)
    


    


def move_x(xey):
    WIN.blit(bgimg, (0,0))
    WIN.blit(bgimg1, (250, xey))
    WIN.blit(bgimg2, (500, xey))
    WIN.blit(bgimg3, (750, xey))
    WIN.blit(bgimg4, (1000,xey))
    
    
    

def move_y(yex):
    WIN.blit(bgimg5, (yex,150))
    WIN.blit(bgimg6, (yex,300))
    WIN.blit(bgimg7, (yex,450))
    WIN.blit(bgimg8, (yex,600))
    
    


def start():
    WIN.blit(startimg, (550,250))
    


def exit():
    WIN.blit(exitimg, (550,350))
    pygame.display.update()

    
    
    

    


def main():
    emx, emy = 50, 50
    direction1 = 1
    direction2 = 1 
    clock = pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        emy += direction1
        emx += direction2
        if emy >= WIDTH - dimimg1.width or emy <=0:
            direction1 *= -1
            print("hi")
        if emx >= HEIGHT - dimimg5.height or emx <=0:
            direction2 *=-1
            print("bye")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        move_x(emx)
        move_y(emy)
        start()
        exit()
        draw_window()
        
        
    pygame.quit()

if __name__ == "__main__":
    main()