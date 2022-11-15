# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 圆形.py
# @Time    : 2022/10/26 10:25
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Circle")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 清除屏幕，绘制，刷新
    screen.fill((0, 0, 200))

    yellow = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10

    pygame.draw.circle(screen, yellow, position, radius, width)
    pygame.display.update()
