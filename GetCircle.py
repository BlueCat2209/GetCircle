#IMPORT
import sys, pygame, time
import pgzrun as pg
from random import randint

from pygame.constants import TIMER_RESOLUTION

#INIT
    #gameWindow
WIDTH= 800  
HEIGHT= 800

    #gamePrimaryInformation
score = 0
gameOver = False
safeZoneCheck = False

    #gameCharacter
man = Actor('man')
place = Actor('safe_zone')
explosion = Actor('explosion')

    #characterPosition
man.pos = 405,405
place.pos = 127,132
while True:
    def draw():
        #bringPictureIntoScreen
        screen.blit('background',(0,0))
        man.draw()
        place.draw()
        screen.draw.text("Score: " + str(score),color = 'black',topleft = (10,10))
        if gameOver :
            screen.blit('background',(0,0))
            screen.draw.text('Final Score: '+str(score), color = 'black', topleft = (10,10))
            screen.draw.text('Press "ESC" to exit', color = 'black', topleft = (330,400))

    def placeToStayAlive():
            #randomPosition
        x = randint(1,3) 
        y = randint(1,3)
            #takePositionIntoPlace.x
        if x == 1: place.x = 127
        elif x == 2: place.x = 402
        elif x == 3: place.x = 671
            #takePositionIntoPlace.y
        if y == 1: place.y = 132
        elif y == 2: place.y = 405
        elif y == 3: place.y = 671
        place.draw()

    def update():
            #ExitKey
        if keyboard.ESCAPE: sys.exit()
            #MovingKey
        if keyboard.left:
            man.x = man.x - 10
        if keyboard.right:
            man.x = man.x + 10
        if keyboard.up:
            man.y = man.y - 10
        if keyboard.down:
            man.y = man.y + 10
            #CheckTheGame
        global score
        safeZoneCheck = man.colliderect(place)
        if (safeZoneCheck): 
            music.play('ting')
            score += 1
            time.sleep(0.1)
            music.stop()
            placeToStayAlive()
    def timeUp():
        global gameOver
        gameOver = True
    clock.schedule(timeUp, 10.0)  
    pg.go() # Run program
