import pygame

def game_title(name,rgba,bg,x,y,WIN,fsize):
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', fsize)
    title1 = font.render(name, True, rgba,bg)
    WIN.blit(title1, (x,y))