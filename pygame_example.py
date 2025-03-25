import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

x, y = 50, 250
speed = 5

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    x += speed
    if x > 450 or x < 50:
        speed = -speed
    pg.draw.circle(screen, (0, 0, 255), (x, y), 30)
    pg.display.flip()
    clock.tick(60)

pg.quit()
