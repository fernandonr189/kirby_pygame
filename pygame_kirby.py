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

def animate_kirby_feet(screen, x, y, t):
    left_foot_surface = pg.Surface((140, 180), pg.SRCALPHA, 32);
    right_foot_surface = pg.Surface((140, 180), pg.SRCALPHA, 32);
    pg.draw.ellipse(left_foot_surface, RED, (0, 0, 140, 180))
    pg.draw.ellipse(right_foot_surface, RED, (0, 0, 140, 180))
    left_foot_surface = pg.transform.rotate(left_foot_surface, 30 + t)
    right_foot_surface = pg.transform.rotate(right_foot_surface, -30 - t)
    screen.blit(left_foot_surface, (x + 40, y + 70))
    screen.blit(right_foot_surface, (x - 190, y + 70))

def animate_kirby_arms(screen, x, y, t):
    left_arm_surface = pg.Surface((100, 150), pg.SRCALPHA, 32);
    right_arm_surface = pg.Surface((100, 150), pg.SRCALPHA, 32);
    pg.draw.ellipse(left_arm_surface, PINK, (0, 0, 100, 150))
    pg.draw.ellipse(right_arm_surface, PINK, (0, 0, 100, 150))
    left_arm_surface = pg.transform.rotate(left_arm_surface, t)
    right_arm_surface = pg.transform.rotate(right_arm_surface, t)
    screen.blit(left_arm_surface, (x + 180, y))
    screen.blit(right_arm_surface, (x - 280, y))

def draw_kirby(screen, x, y):
    # drawing body
    pg.draw.circle(screen, PINK, (x, y), 240)

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

tx = 0.7
t = 7
while running:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    draw_kirby(screen, screen.get_width() / 2, screen.get_height() / 2)
    animate_kirby_feet(screen, screen.get_width() / 2, screen.get_height() / 2, t)
    animate_kirby_arms(screen, screen.get_width() / 2, screen.get_height() / 2, (t - 15) / 5)
    t += tx
    if t > 15 or t < 5:
        tx = -tx
    pg.display.flip()
    clock.tick(60)

pg.quit()
