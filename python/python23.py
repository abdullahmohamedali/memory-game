import os 
import sys
import random
import pygame
from pygame import *

pygame.init()

scr_size= (width,height) =(610,160)
FPS=60
gravity=0.6

black = (0,0,0)
white = (225,225,225)
background_col =(235,235,235)

high_score=0

screen=pygame.display.set_mode(scr_size)
clock=pygame.time.Clock()
pygame.display.set_caption("dino game")

def load_image( name, sizex=-1,sizey=-1,colorkey=None,):
    
    fullname = os.path.join('assets',name)
    image = pygame.image.load(fullname)
    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)

    if sizex != -1 or sizey != -1:
        image=pygame.transform.scale(image,(sizex,sizey))
        return (image,image.get_rect())
def load_sprite_sheet(sheetname,nx,ny,scalex=-1,colorkey=None,):
        fullname=os.path.join('assets',sheetname)
        sheet=pygame.image.load(fullname)
        sheet=sheet.convert()

        sheet_rect = sheet.get_rect 

        sprites=[]

        sizex = sheet_rect.width/nx
        sizey = sheet_rect.hight/ny
for i in range(0,ny):
    for j in range(0,nx):
                            rect = pygame.rect((j*sizex,i*sizey,sizex,sizey))