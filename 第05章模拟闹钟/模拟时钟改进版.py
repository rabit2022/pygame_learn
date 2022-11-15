# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 模拟时钟改进版.py
# @Time    : 2022/10/26 19:26
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import math
import random

import pygame
import sys
from datetime import datetime

from pygame.locals import *


def print_text(x, y, info: int, color=(255, 255, 255)):
    if info % 3:
        font1 = pygame.font.Font(None, 50)
    else:
        font1 = pygame.font.Font(None, 70)
        color = orange

    imgText = font1.render(str(info), True, color)
    screen.blit(imgText, (x, y))


def draw_handle(second_num, carry_over, size, color=(255, 255, 255)):
    """
    一个角度的指针
    :param second_num: 秒数、分钟数或小时数
    :param carry_over: 一分钟的秒数，或一小时的分钟数。
    :param size: 指针的长短,粗细
    :type size: tuple[int, int]
    :param color: 手柄的颜色。
    """

    def wrap_angle(angle):
        """
        它以度为单位取一个角度，并返回 0 到 360 度之间的等效角度
        :param angle: 角度，以度为单位
        :return: 0 到 360 度之间的等效角度
        """
        return angle % 360

    # draw  seconds hands
    seconds_angle = wrap_angle(second_num * (360 / carry_over) - 90)
    seconds_angle = math.radians(seconds_angle)

    second_x = math.cos(seconds_angle) * (radius - size[0])
    second_y = math.sin(seconds_angle) * (radius - size[0])

    target = (pos_x + second_x, pos_y + second_y)
    pygame.draw.line(screen, color, (pos_x, pos_y), target, size[1])


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("analog clock")

orange = 220, 180, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100
green = 0, 255, 0
light_gray = 230, 230, 230

pos_x = 300
pos_y = 250
radius = 250
angle = 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

    screen.fill(light_gray)

    # 表盘
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)
    pygame.draw.circle(screen, green, (pos_x, pos_y), radius, radius-6)

    # draw clock number 1,2,...,12
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 28) - 18
        y = math.sin(angle) * (radius - 28) - 18
        print_text(pos_x + x, pos_y + y, n)

    # time
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    draw_handle(seconds, 60, (40, 5), white)
    draw_handle(minutes, 60, (60, 10), orange)
    draw_handle(hours, 12, (80, 25), pink)

    pygame.display.update()
