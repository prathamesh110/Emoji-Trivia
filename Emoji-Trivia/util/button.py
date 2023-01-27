import pygame


class Button():
    def __init__(self,x,y,image,scale):
        Simgwidth = image.get_width()
        Simgheight = image.get_height()
        self.image = pygame.transform.scale(image, (int(Simgwidth * scale), int(Simgheight * scale)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.clicked = False


    def draw(self,WIN):
        action = False
        Pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(Pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        WIN.blit(self.image,(self.rect.x, self.rect.y))
        return action