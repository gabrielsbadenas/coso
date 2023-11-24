import pygame
from pygame.locals import *
screen=pygame.display.set_mode((640,480))
x=0
y=1
running = True
pygame.init()
key_dict={K_k:(0,0,0)}
def quit(event):
    if event.type == KEYDOWN:
        if event.key in key_dict:
            print('k')
    if event.type==pygame.QUIT:
        running = False
def events(key_in_dict,key_quit):
    if key_in_dict:
        print('k')
    if key_quit:
        return False
    return True
key_down=False
while running:
    for event in pygame.event.get():
        key_down = event.type == KEYDOWN
        if key_down:
            key_in_dict = event.key in key_dict
            key_quit = event.key == K_BACKSPACE
            running=events(key_in_dict,key_quit)
    screen.fill((255,0,0))
    pygame.display.update()
pygame.quit()
