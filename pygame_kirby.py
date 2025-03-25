import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
speed = 5
running = True

PINK = (234, 153, 152)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
BLUE = (100, 100, 255)

def draw_kirby(screen, x, y):
    # drawing body
    pg.draw.circle(screen, PINK, (x, y), 240)
    # drawing arms
    pg.draw.ellipse(screen, PINK, (x + 180, y, 100, 150))
    pg.draw.ellipse(screen, PINK, (x - 280, y, 100, 150))

    # drawing eyes
    pg.draw.ellipse(screen, BLACK, (x + 40, y - 90, 70, 120))
    pg.draw.ellipse(screen, BLACK, (x - 90, y - 90, 70, 120))
    pg.draw.ellipse(screen, WHITE, (x - 75, y - 85, 35, 60))
    pg.draw.ellipse(screen, WHITE, (x + 55, y - 85, 35, 60))

    # drawing cheeks
    pg.draw.ellipse(screen, RED, (x + 100, y + 40, 50, 30))
    pg.draw.ellipse(screen, RED, (x - 140, y + 40, 50, 30))

    # drawing smile
    pg.draw.arc(screen, RED, (x - 15, y + 40, 60, 50), 3.40, -0.15, 6)

    # drawing feet
    left_foot_surface = pg.Surface((110, 160), pg.SRCALPHA, 32);
    right_foot_surface = pg.Surface((110, 160), pg.SRCALPHA, 32);

    pg.draw.ellipse(left_foot_surface, RED, (0, 0, 110, 160))
    pg.draw.ellipse(right_foot_surface, RED, (0, 0, 110, 160))

    screen.blit(left_foot_surface, (x + 60, y + 100))
    screen.blit(right_foot_surface, (x - 130, y + 100))

while running:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    draw_kirby(screen, screen.get_width() / 2, screen.get_height() / 2)
    pg.display.flip()
    clock.tick(60)

pg.quit()
