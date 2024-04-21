import pgzrun
import os
import time

os.environ["SDL_VIDEO_CENTERED"] = '1'

TITLE = 'race game'
WIDTH = 1000
HEIGHT = 700

welcome = Actor("welcome",(480,350))
map1 = Actor("map1",(0,0))
start = Actor("start",(500,350))
waitPage = Actor("map1",(480,350))
menu = Actor("start",(480,350))
map1 = False

def draw() :
    screen.clear()
    welcome.draw()
    start.draw()
    if map1 == True :
        waitPage.draw()
        time.sleep(10)
        menu,draw()

def update() :
    pass


def on_mouse_down(pos,button):
    global map1 , start , openMenuWindow
    if start.collidepoint(pos) and button == mouse.LEFT:
        map1 = True
pgzrun.go()



