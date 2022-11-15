# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:28:18 2015
@author: liuchang
"""

import pygame
import random
import sys
import time

from pygame.locals import *


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("keyboard demo")

font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)

white = 255, 255, 255
yellow = 255, 255, 0

# pressed = False

key_flag = False
correct_answer = 97  # "a"

seconds = 11
score = 0
clock_start = 0
game_over = True

clock_start = time.perf_counter()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False

    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 11
            clock_start = time.perf_counter()

    '''
    Python3.8 不再支持time.clock，但在调用时依然包含该方法
    用 time.perf_counter() 来替换
    '''
    # clock_start = time.clock()
    # current = time.clock() - clock_start
    # clock_start = time.perf_counter()

    current = time.perf_counter() - clock_start
    # print(current, seconds - current)
    speed = score * 6

    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122)
            score += 1

    # clean
    screen.fill((0, 100, 0))
    print_text(font1, 0, 0, "lets see how fast you can type ")
    print_text(font1, 0, 20, "try to keep up for 10 seconds..  ")

    if key_flag:
        print_text(font1, 500, 0, "<key>")

    if not game_over:
        print_text(font1, 0, 80, "time :" + str(int(seconds - current)))

    print_text(font1, 0, 100, "speed :" + str(speed) + "letters/min")
    print_text(font1, 500, 30, "score :" + str(score))

    if game_over:
        print_text(font1, 0, 160, "press enter to start")

    print_text(font2, 0, 240, chr(correct_answer - 32), yellow)

    pygame.display.update()

