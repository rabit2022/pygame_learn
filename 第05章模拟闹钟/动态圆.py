# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 动态圆.py
# @Time    : 2022/10/26 19:03
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import math
import random
import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("circle demo")
screen.fill((0, 0, 100))

pos_x = 300
pos_y = 250
radius = 200
angle = 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # screen.fill((0, 0, 100))

    angle += 1
    if angle >= 360:
        angle = 0

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = r, g, b

    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    pos = (int(pos_x + x), int(pos_y + y))

    pygame.draw.circle(screen, color, pos, 10, 0)

    pygame.display.update()
