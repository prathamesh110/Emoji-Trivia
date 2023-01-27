import sys
from tkinter import messagebox
import pygame
import os
from mydb import dbconnect
from util import Title
from util import InputBox
from util import button
from pygame import mixer
import main1
import time
import mysql.connector
import pyautogui

WIDTH, HEIGHT = 1200, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
mainbg = pygame.image.load(os.path.join('images','bg1.png'))
mainbg=pygame.transform.scale(mainbg,(1200, 800))
emojiFBg = pygame.image.load(os.path.join('imgl', 'emojiF2bg4.png'))
emojiFBg=pygame.transform.scale(emojiFBg,(800, 550))
Brown = (191, 117, 42)
White = (255,255,255)

mixer.init()

levelimg = pygame.image.load(os.path.join('imgl', 'levelimg1.png'))
levelimg =pygame.transform.scale(levelimg,(400, 400))


lifeimg = pygame.image.load(os.path.join('imgl', 'life1.png'))
lifeimg =pygame.transform.scale(lifeimg,(300, 300))

submimg = pygame.image.load(os.path.join('imgl','submitbtn.png'))
submbtn=pygame.transform.scale(submimg,(450, 350))
#--------------------------------------input var------------------------------------------------------









#--------------------------------------------------------------------------------------------------




levtitlarr = []
lifeC = [1,1,1]    
scorearr = [0]
class Maingame():
    def __init__(self,name):
        levtitl = 0
        score = 0
        self.score = score
        self.levtitl = levtitl
        eid = 1
        self.eid = eid
        db = mysql.connector.connect(host = "localhost",port = "3306",user = "root",password = "",db = "emojigame")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        self.db = db
        self.cursor = cursor
        dbcon = dbconnect(self.db,self.cursor).emojifetch(name,self.eid)

        self.dbcon = dbcon
            
        
          
    def execg(self):
        WIN.blit(mainbg,(0,0))
        WIN.blit(lifeimg, (900,3))
        WIN.blit(levelimg, (-80,-50))
        WIN.blit(emojiFBg,(200,-20))
        

    def subm_procc(self,name):
        self.ename =name
        cattitl = "Category:"+name
        Submbtn = button.Button(614.5, 350,submbtn, 1)
        
        Title.game_title(cattitl,White,Brown,960,100,WIN,28)
        Title.game_title("Score:"+str(scorearr[-1]),White,Brown,550,50,WIN,28)
        Title.game_title(str(len(levtitlarr)),(255,20,147),None,190,57,WIN,26)
        lenlife = len(lifeC)
        y = 0
        for rlife in lifeC:
            lifeimg = pygame.image.load(os.path.join('imgl', 'heartlife1.png'))
            lifeimg =pygame.transform.scale(lifeimg,(70, 35))
            WIN.blit(lifeimg,(940+y,45))
            y=y+50

        
        self.game_work(Submbtn)
        InputBox.inputbox(WIN)
       

    
    def game_work(self,Submbtn):
        
        
        ans = self.dbcon[0]
        C_ans = str(ans)
        Ci_ans = C_ans.replace(" ","")
        CL_ans = Ci_ans.lower()
        print(CL_ans)
        emojiD = self.dbcon[1].split("_")
        em_count = len(emojiD)
        if em_count == 1:
            eimg1 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[0]+'.png'))
            mimg1=pygame.transform.scale(eimg1,(50, 50))
            WIN.blit(mimg1,(570,195))

        elif em_count == 2:
            eimg1 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[0]+'.png'))
            mimg1=pygame.transform.scale(eimg1,(50, 50))
            WIN.blit(mimg1,(460,195))

            eimg2 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[1]+'.png'))
            mimg2=pygame.transform.scale(eimg2,(50, 50))
            WIN.blit(mimg2,(690,195))

        elif em_count == 3:
            eimg1 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[0]+'.png'))
            mimg1=pygame.transform.scale(eimg1,(50, 50))
            WIN.blit(mimg1,(460,195))

            eimg2 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[1]+'.png'))
            mimg2=pygame.transform.scale(eimg2,(50, 50))
            WIN.blit(mimg2,(575,195))

            eimg3 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[2]+'.png'))
            mimg3=pygame.transform.scale(eimg3,(50, 50))
            WIN.blit(mimg3,(690,195))

        elif em_count == 4:
            eimg1 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[0]+'.png'))
            mimg1=pygame.transform.scale(eimg1,(50, 50))
            WIN.blit(mimg1,(460,195))

            eimg2 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[1]+'.png'))
            mimg2=pygame.transform.scale(eimg2,(50, 50))
            WIN.blit(mimg2,(540,195))

            eimg3 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[2]+'.png'))
            mimg3=pygame.transform.scale(eimg3,(50, 50))
            WIN.blit(mimg3,(620,195))

            eimg4 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[3]+'.png'))
            mimg4=pygame.transform.scale(eimg4,(50, 50))
            WIN.blit(mimg4,(690,195))

        elif em_count == 5:
            eimg1 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[0]+'.png'))
            mimg1=pygame.transform.scale(eimg1,(50, 50))
            WIN.blit(mimg1,(460,195))

            eimg2 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[1]+'.png'))
            mimg2=pygame.transform.scale(eimg2,(50, 50))
            WIN.blit(mimg2,(520,195))

            eimg3 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[2]+'.png'))
            mimg3=pygame.transform.scale(eimg3,(50, 50))
            WIN.blit(mimg3,(580,195))

            eimg4 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[3]+'.png'))
            mimg4=pygame.transform.scale(eimg4,(50, 50))
            WIN.blit(mimg4,(640,195))

            eimg5 = pygame.image.load(os.path.join('D:\pygame\pygametutuorial\images\em_img',emojiD[4]+'.png'))
            mimg5=pygame.transform.scale(eimg5,(50, 50))
            WIN.blit(mimg5,(690,195))

        i_ans = InputBox.inputbox(WIN)
        si_ans = str(i_ans)
        name = self.ename
        if Submbtn.draw(WIN):
            
            time.sleep(2)
            
            
            if si_ans == CL_ans:
                mixer.music.load(os.path.join('sound','win.wav'))
                mixer.music.play()
                levtitlarr.append(self.levtitl)
                self.levtitl= self.levtitl + 1
                score_p= scorearr[-1] + 100
                scorearr.append(score_p)
                print(scorearr)
                InputBox.user_text = ""
                Maingame(name).draw(name)
                
                
            else:
                levtitlarr.clear()
                lifeC.pop(-1)
                mixer.music.load(os.path.join('sound','lose.wav'))
                mixer.music.play()
                score_p= scorearr[-1] - 50
                scorearr.append(score_p)
                pyautogui.alert("you Lost a Life")
                i_ans = ""
                if len(lifeC) == 0:
                    scorearr.clear()
                    scorearr.append(0)
                    pyautogui.alert("Game Over")
                    lifeC.append(1)
                    lifeC.append(1)
                    lifeC.append(1)
                    main1.main()



                else:
                    levtitl = 0

            InputBox.user_text = ""
    
                    
        else:
            Submbtn.draw(WIN)


    
        
        
    
    
        
    def allcall(self,name):
        self.execg()
        self.subm_procc(name)  
        
         
    
    def draw(self,name):
        mgame = True
        
        while mgame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mgame = False
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if InputBox.input_rect.collidepoint(event.pos):
                        InputBox.active = True
                    else:
                        InputBox.active = False
  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if InputBox.active == True:
                            InputBox.user_text = InputBox.user_text[:-1]
                    else:
                        if InputBox.active == True: 
                            InputBox.user_text += event.unicode



            self.allcall(name)
            pygame.display.update()
            WIN.fill([96, 195, 196])





    
    
    