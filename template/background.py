import pygame as py

def run():
    py.init()
    
    screen = py.display.set_mode([400,400])

    launched = True

    while launched:
        for event in py.event.get():
            if event.type == py.QUIT:
                launched = False
        screen.fill((12,25,38))
        py.draw.line(screen, (128,25,240),[10,10],[280,310],3)
        py.display.flip()
    
    py.quit()

run()