'''
The application uses pygame and ThorPy to build the interface
Then executes classification(model_name,samples,labels,RANGEX,RANGEY) from classify.py module

@author: pawel@kasprowski.pl
'''
from pygame import QUIT
from pygame import display
from pygame import draw
from pygame import Rect
import pygame, sys, thorpy
import numpy as np
    
import classify

clock = pygame.time.Clock()

RANGEX = 50
RANGEY = 50
SIZEX = 12
SIZEY = 12

WIDTH = 750
HEIGHT = 600
RED = (255,0,0) #RGB
GREEN = (0,255,0) #RGB

color=RED
red_points = []
green_points = []
result = np.zeros([RANGEX,RANGEY])

def switch_color():
    global color
    if color==RED:
        color=GREEN
    else:
        color=RED   
    
def refresh(screen):
    global color
    for x in range(RANGEX):
        for y in range(RANGEY):
            v = result[x][y]
            c = (200*v,200*(1-v),0)
            draw.rect(screen, c, Rect(x*SIZEX,y*SIZEY,SIZEX,SIZEY), 0)
    for p in red_points:
        draw.rect(screen, RED, Rect(p[0],p[1],SIZEX,SIZEY), 0)
    for p in green_points:
        draw.rect(screen, GREEN, Rect(p[0],p[1],SIZEX,SIZEY), 0)
    draw.rect(screen, color, Rect(RANGEX*SIZEX+25,RANGEY*SIZEY-125,100,100), 0)    




#########################################################################33

def run_classification(model_name):
    global result
    samples = []
    labels = []
    for p in red_points:
        pp = [p[0]/SIZEX,p[1]/SIZEY]
        samples.append(pp)
        labels.append(1)
    for p in green_points:
        pp = [p[0]/SIZEX,p[1]/SIZEY]
        samples.append(pp)
        labels.append(0)
    result = classify.classification(model_name,samples,labels,RANGEX,RANGEY)

def reset():
    global red_points,green_points
    red_points = []
    green_points = []
        
    

def main():
    global reset
    pygame.init()
    screen = display.set_mode((WIDTH,HEIGHT),0,32)
    
    # declaration buttons
    runPerc = thorpy.make_button("Perceptron", func=lambda:run_classification("PERCEPTRON"))
    runHidden = thorpy.make_button("Linear Layer", func=lambda:run_classification("HIDDEN"))
    runHiddenSigmoid = thorpy.make_button("Sigmoid Layer", func=lambda:run_classification("HIDDEN_SIGMOID"))
    runHiddenRelu = thorpy.make_button("RELU Layer", func=lambda:run_classification("HIDDEN_RELU"))
    reset = thorpy.make_button("RESET", func=reset)
    box = thorpy.Box.make(elements=[runPerc,runHidden,runHiddenSigmoid,runHiddenRelu,reset])
    
    #============================
    menu = thorpy.Menu(box)
    box.set_topleft((600,5))
    box.blit()
    box.update()
    
    display.set_caption("Neural classifier byPK")
    while True:
        clock.tick(40)
        for event in pygame.event.get():
            menu.react(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0]<600:
                    if color==RED:
                        red_points.append(pos)
                    if color==GREEN:
                        green_points.append(pos)
                if pos[0]>600 and pos[1]>450:
                    switch_color()
            refresh(screen) 
        display.update()

if __name__ == "__main__":
    main()    