from pprint import pprint

import pygame.display

from BubbleSort import BubbleSort
from QuickSort import QuickSort
from random import shuffle
import pygame as pg
from config import *
from time import sleep
from visualisation_types import *

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    array = list(range(1, NUMBER_OF_ELEMENTS + 1))
    shuffle(array)
    array = QuickSort(array)
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
            step_as_spiral(screen, step)
            sleep(0.02/20)

        elif not is_ended:
            ending_as_spiral(screen, array, pg.display)
            is_ended = True

        pygame.display.flip()
