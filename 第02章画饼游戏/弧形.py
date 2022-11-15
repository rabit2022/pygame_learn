# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 弧形.py
# @Time    : 2022/10/26 10:46
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import math
import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 清除屏幕，绘制，刷新
    screen.fill((0, 0, 200))

    color = 255, 0, 255
    position = 200, 150, 200, 200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8

    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.display.update()
