from pygame import *

from spriteClass import GameSprite, Player

''' colors '''
background = (200, 255, 255)

window = display.set_mode((600, 500)) # widht, height
window.fill(background)

clock = time.Clock()

platform_left = Player('img/racket.png', 10, 220, 4, 50, 150)
platform_right = Player('img/racket.png', 540, 220, 4, 50, 150)

''' variables '''
game = True
finish = True

'''' game loop '''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == True:
        window.fill(background) # keep refreshing the window

        platform_left.reset(window_object=window)
        platform_left.update_left()
        platform_right.reset(window_object=window)
        platform_right.update_right()
    

    display.update()
    clock.tick(60) # 60 frame per second