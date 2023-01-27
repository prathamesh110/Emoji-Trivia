import pygame

user_text = ''
active = False
base_font = pygame.font.Font(None, 32)
input_rect = pygame.Rect(390, 300, 440, 38)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
  
def inputbox(WIN):  
    if active:
        color = color_active
    else:
        color = color_passive
          
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(WIN, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    WIN.blit(text_surface, (input_rect.x+5, input_rect.y+6))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    #input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()    
    return user_text