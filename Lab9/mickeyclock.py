import pygame
import sys
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 700, 525
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load(r"C:\Users\archa\Desktop\pptwo\Lab9\mickey.jpeg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

center = (WIDTH // 2, HEIGHT // 2)

def draw_hand(angle, length, color, width):
    rad = math.radians(angle - 90)
    x = center[0] + length * math.cos(rad)
    y = center[1] + length * math.sin(rad)
    pygame.draw.line(screen, color, center, (x, y), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))

    now = datetime.now()

    hour = now.hour % 12
    minute = now.minute
    second = now.second

    sec_angle = second * 6
    min_angle = minute * 6 + second * 0.1
    hour_angle = hour * 30 + minute * 0.5

    draw_hand(hour_angle, 100, (0, 0, 0), 6)    
    draw_hand(min_angle, 150, (0, 0, 0), 4)     
    draw_hand(sec_angle, 180, (255, 0, 0), 2)   

    pygame.draw.circle(screen, (0, 0, 0), center, 5)

    pygame.display.flip()
    clock.tick(1)