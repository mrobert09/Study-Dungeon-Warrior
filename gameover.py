import pygame
from pygame.locals import *
pygame.init()
width = 600
height = 600
surface = pygame.display.set_mode((width, height))
font = pygame.font.Font("Fonts/Oswald-VariableFont_wght.ttf", 24)

def press_key_msg():
    """
    Tells user to press any key to play the game.
    :return: Nothing
    """
    msg = font.render('Press any key to try again.', True, (0, 0, 0))
    msg_rect = msg.get_rect()
    msg_rect.topleft = (width - 415, height - 50)
    surface.blit(msg, msg_rect)

def key_press_check():
    """
    Checks for key press.
    :return: Nothing
    """
    if len(pygame.event.get(QUIT)) > 0:
        pygame.quit()
    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return None
    if key_up_events[0].key == K_ESCAPE:
        pygame.quit()
    return key_up_events[0].key



def game_over():
    """
    Displays the title of the game.
    :return:
    """
    title = font.render('You died. Be better next time.', True, (0, 0, 0), (255, 255, 255))
    while True:
        surface.fill((255, 255, 255))
        rect = title.get_rect()
        rect.center = (width / 2, height / 2)
        surface.blit(title, rect)

        press_key_msg()

        if key_press_check():
            pygame.event.get()
            break
        pygame.display.update()
    
    return True
