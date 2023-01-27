import pygame
import os
import random
import math
from pygame import mixer
mixer.init()
pygame.init()
import sys
from util import button
from util import Title
from util import Menu
from util import maingame



WIDTH, HEIGHT = 1200, 750
White = (255,255,255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emoji Trivia")

FPS = 60
DW_HALF = WIDTH/2
DH_HALF = HEIGHT/2
DISPLAY_AREA = WIDTH*HEIGHT


#--------------------------------------------Menu-Frame--------------------------------------------------#

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

brandimg = pygame.image.load(os.path.join('imgl','brandbtn.jpg'))
movieimg = pygame.image.load(os.path.join('imgl','movie.jpg'))
wordimg = pygame.image.load(os.path.join('imgl','wordbtn.jpg'))
songimg = pygame.image.load(os.path.join('imgl','sings.jpg'))


bgimg1=pygame.transform.scale(bgimg1,(100, 100))
bgimg2=pygame.transform.scale(bgimg2,(100, 100))
bgimg3=pygame.transform.scale(bgimg3,(100, 100))
bgimg4=pygame.transform.scale(bgimg4,(100, 100))
bgimg5=pygame.transform.scale(bgimg5,(100, 100))
bgimg6=pygame.transform.scale(bgimg6,(100, 100))
bgimg7=pygame.transform.scale(bgimg7,(100, 100))
bgimg8=pygame.transform.scale(bgimg8,(100, 100))


dimstart = startimg.get_rect()
dimexit = exitimg.get_rect()
dimimg1 = bgimg1.get_rect()
dimimg5 = bgimg5.get_rect()
imgo=[bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8,bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8,
       bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8,bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8
       ,bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8,bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8
       ,bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8,bgimg1,bgimg2,bgimg3,bgimg4,bgimg5,bgimg6,bgimg7,bgimg8]
       
    
#-------------------------------------------Start Exit------------------------------------------------------------



startbtn = button.Button(620, 200,startimg, 0.25)
exitbtn = button.Button(620, 350,exitimg, 0.25) 
BALLS = list([Menu.Mainmenu(imgo[j],dimimg1,WIDTH,HEIGHT,WIN) for j in range(0,64)])

#-----------------------------------------------category----------------------------------------------------------------

brandimg=pygame.transform.scale(brandimg,(400, 250))
movieimg=pygame.transform.scale(movieimg,(400, 250))
wordimg=pygame.transform.scale(wordimg,(400, 250))
songimg=pygame.transform.scale(songimg,(400, 250))



Brandbtn = button.Button(350, 150,brandimg, 1)
Moviebtn = button.Button(850, 440,movieimg, 1)
Wordbtn = button.Button(350, 440,wordimg, 1)
Songbtn = button.Button(850, 150,songimg, 1)











def  categories():
    Brown = (191, 117, 42)
    titl = "Category"
    categ= True
    while categ:
        for cat in pygame.event.get():
            if cat.type == pygame.QUIT:
                run = False
                sys.exit()
        
        if Brandbtn.draw(WIN):
            mixer.music.load(os.path.join('sound','click.wav'))
            mixer.music.play()
            name = "Brand"
            maingame.Maingame(name).draw(name)
            
        if Moviebtn.draw(WIN):
            mixer.music.load(os.path.join('sound','click.wav'))
            mixer.music.play()
            name = "Movie"
            maingame.Maingame(name).draw(name)
            
        if Wordbtn.draw(WIN):
            mixer.music.load(os.path.join('sound','click.wav'))
            mixer.music.play()
            name = "Word"
            maingame.Maingame(name).draw(name)
            
        if Songbtn.draw(WIN):
            mixer.music.load(os.path.join('sound','click.wav'))
            mixer.music.play()
            name = "Song" 
            maingame.Maingame(name).draw(name)
            
        
        
        Title.game_title(titl,Brown,White,460,40,WIN,64)
        pygame.display.update()
        draw_window()
    pygame.quit() 




def Execmenu():
    
    Brown = (191, 117, 42)
    titl = "Emoji Trivia"
    #Emoji design
    for b in BALLS:
        b.draw()
    
     
    #start exit button
    if startbtn.draw(WIN):
        mixer.music.load(os.path.join('sound','greetsound.wav'))
        mixer.music.play()         
        categories()

    if exitbtn.draw(WIN):
        run = False
        sys.exit()

    Title.game_title(titl,Brown,White,430,60,WIN,64)
    
  
def draw_window():
    
    WIN.fill([96, 195, 196])

#-----------------------------------------------main-loop-----------------------------------------------------------------   
def main():
    clock = pygame.time.Clock()
    run=True
    
    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
                
        
        
        
        Execmenu()
        pygame.display.update()
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()





        
        
    

