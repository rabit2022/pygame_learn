# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 矩形.py
# @Time    : 2022/10/26 10:30
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
pygame.display.set_caption("Drawing Rectangles")

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 清除屏幕，绘制，刷新
    screen.fill((0, 0, 200))

    # 移动
    pos_x += vel_x
    pos_y += vel_y

    # 越界判断
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 500 or pos_y <= 0:
        vel_y = -vel_y

    yellow = 255, 255, 0
    width = 0
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect(screen, yellow, pos, width)

    pygame.display.update()
