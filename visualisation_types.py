from pygame import draw
from config import WIDTH, SCREEN_SIZE, NUMBER_OF_ELEMENTS
from time import sleep
from math import sin, cos, log


def step_as_bars(screen, step):
    for ind, el in enumerate(step[0]):
        color = step[1][ind] if ind in step[1] else (255, 255, 255)
        draw.rect(screen, color,
                  (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]))
        draw.rect(screen, (0, 0, 0),
                  (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]), 1)


def step_as_spiral(screen, step):
    center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
    for ind, el in enumerate(step[0], 1):
        color = step[1][ind] if ind in step[1] else (255, 255, 255)
        base = 1 / (0.6 + ind / len(step[0]) * 0.38)
        draw.circle(screen, color,
                    (center[0] + (el + 1) * cos(log(ind, base)), center[1] + (el + 1) * sin(log(ind, base))), 2)


def ending_as_bars(screen, array, display):
    for ind, el in enumerate(array):
        draw.rect(screen, (0, 127, 0),
                  (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]))
        draw.rect(screen, (0, 0, 0),
                  (ind * WIDTH, SCREEN_SIZE[1] - el, WIDTH, SCREEN_SIZE[1]), 1)
        display.flip()
        sleep(0.01)


def ending_as_spiral(screen, array, display):
    center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
    for ind, el in enumerate(array, 1):
        base = 1 / (0.6 + ind / len(array) * 0.38)
        draw.circle(screen, (0, 127, 0),
                    (center[0] + (el + 1) * cos(log(ind, base)), center[1] + (el + 1) * sin(log(ind, base))), 2)
        display.flip()
        sleep(0.02)
