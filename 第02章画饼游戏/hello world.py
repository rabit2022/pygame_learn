# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : hello world.py
# @Time    : 2022/10/26 10:17
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import sys

import pygame
from pygame.locals import *

white = 255, 255, 255
blue = 0, 0, 255

pygame.init()
screen = pygame.display.set_mode((600, 500))
# None默认的字体
myfont = pygame.font.Font(None, 60)
# 抗锯齿，提升质量
textImage = myfont.render("hello pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 清除屏幕，绘制，刷新
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()
