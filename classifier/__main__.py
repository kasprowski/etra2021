
'''
The application uses pygame and ThorPy to build the interface
Then executes classification(model_name,samples,labels,RANGEX,RANGEY) from classify.py module

@author: pawel@kasprowski.pl
'''
from pygame import QUIT
from pygame import Rect
from pygame import display
from pygame import draw
import pygame, sys, thorpy
from classify import classification
import numpy as np

clock = pygame.time.Clock()

# parameters for visualization
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
result = np.zeros([RANGEX,RANGEY]) # table of results

# changes the current color
def switch_color():
    global color
    print("switch color")
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
    

# classifies all points in results matrix using given samples and the classification algorithm
def run_classification(model_name):
    global result
    # copy points to samples and labels
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
    result = classification(model_name,samples,labels,RANGEX,RANGEY)

# removes all sample points        
def reset():
    global red_points,green_points
    red_points = []
    green_points = []

def main():    
    pygame.init()

    # =============================================================================
#     import ctypes
#     # Query DPI Awareness (Windows 10 and 8)
#     awareness = ctypes.c_int()
#     errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
#     print(awareness.value)
#     errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(0)
#     print(errorCode)
#     success = ctypes.windll.user32.SetProcessDPIAware()
# =============================================================================
    screen = display.set_mode(size=(WIDTH,HEIGHT),flags=pygame.SCALED,display=0,depth=32)
    #screen = display.set_mode(size=(WIDTH,HEIGHT),display=0,depth=32)
    
    # declaration of algorithms for ThorPy buttons
    runKnn = thorpy.make_button("kNN", func=lambda:run_classification("KNN"))
    runLda = thorpy.make_button("LDA", func=lambda:run_classification("LDA"))
    runNB = thorpy.make_button("NB", func=lambda:run_classification("NB"))
    runTree = thorpy.make_button("Decision Tree", func=lambda:run_classification("TREE"))
    runForest = thorpy.make_button("Random Forest", func=lambda:run_classification("RF"))
    runSvc = thorpy.make_button("SVM", func=lambda:run_classification("SVM"))
    runGB = thorpy.make_button("Gradient Boosting", func=lambda:run_classification("GB"))
    runPerc = thorpy.make_button("Perceptron", func=lambda:run_classification("PERC"))
    runReset = thorpy.make_button("RESET", func=reset)
    # create a box of buttons
    box = thorpy.Box.make(elements=[runKnn,runLda,runNB,runTree,runForest,runSvc,runGB,runPerc,runReset])
    menu = thorpy.Menu(box)
    box.set_topleft((600,5))
    box.blit()
    box.update()
        
    display.set_caption("Simple classifier byPK")
    
    while True:
        clock.tick(40)
        for event in pygame.event.get():
            menu.react(event) #read an event
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