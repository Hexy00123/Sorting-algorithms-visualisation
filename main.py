from pprint import pprint
from BubbleSort import BubbleSort
from QuickSort import QuickSort
from random import randint
import pygame as pg
from config import *
from time import sleep

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)

    array = QuickSort([randint(3, SCREEN_SIZE[1]) for _ in range(NUMBER_OF_ELEMENTS)])
    steps = array.sort()
    running = True
    is_ended = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if steps:
            step = steps.pop(0)
            screen.fill((0, 0, 0))
            for ind, el in enumerate(step[0]):
                color = step[1][ind] if ind in step[1] else (255, 255, 255)
                pg.draw.rect(screen, color,
                             (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]))
                pg.draw.rect(screen, (0, 0, 0),
                             (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]), 1)
            sleep(0.02)
        elif not is_ended:
            for ind, el in enumerate(array):
                pg.draw.rect(screen, (0, 127, 0),
                             (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]))
                pg.draw.rect(screen, (0, 0, 0),
                             (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]), 1)
                pg.display.flip()
                sleep(0.01)
            is_ended = True

        pg.display.flip()
