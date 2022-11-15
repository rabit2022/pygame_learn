# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 线条.py
# @Time    : 2022/10/26 10:41
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
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 清除屏幕，绘制，刷新
    screen.fill((0, 80, 0))

    color = 100, 255, 200
    width = 8
    pygame.draw.line(screen, color, (100, 100), (500, 400), width)

    pygame.display.update()
