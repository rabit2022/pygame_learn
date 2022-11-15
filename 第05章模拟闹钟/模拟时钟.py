# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:07:20 2015
@author: liuchang
"""

import math
import pygame
import sys
from datetime import datetime

from pygame.locals import *


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def wrap_angle(angle):
    """
    它以度为单位取一个角度，并返回 0 到 360 度之间的等效角度
    :param angle: 角度，以度为单位
    :return: 0 到 360 度之间的等效角度
    """
    return angle % 360


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("analog clock")
font = pygame.font.Font(None, 60)
orange = 220, 180, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100

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

    screen.fill((0, 0, 100))

    # 表盘
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)

    # draw clock number 1,2,...,12
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 28) - 18
        y = math.sin(angle) * (radius - 28) - 18
        print_text(font, pos_x + x, pos_y + y, str(n))

    # time
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    # draw  seconds hands
    seconds_angle = wrap_angle(seconds * (360 / 60) - 90)
    seconds_angle = math.radians(seconds_angle)
    second_x = math.cos(seconds_angle) * (radius - 40)
    second_y = math.sin(seconds_angle) * (radius - 40)

    target = (pos_x + second_x, pos_y + second_y)
    pygame.draw.line(screen, white, (pos_x, pos_y), target, 10)

    # minute hand
    minute_angle = wrap_angle(minutes * (360 / 60) - 90)
    # add the angle affected by the minute hand
    add_angle = minutes
    minute_angle = math.radians(minute_angle)
    minute_x = math.cos(minute_angle) * (radius - 60)
    minute_y = math.sin(minute_angle) * (radius - 60)

    target = (pos_x + minute_x, pos_y + minute_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 10)

    # hour hand
    hour_angle = wrap_angle(hours * (360 / 12) - 90)
    # 化弧度制用于计算
    add_angle = (add_angle / 60) * (360 / 12)
    hour_angle = math.radians(hour_angle + add_angle)
    hour_x = math.cos(hour_angle) * (radius - 80)
    hour_y = math.sin(hour_angle) * (radius - 80)

    target = (pos_x + hour_x, pos_y + hour_y)
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 25)

    pygame.display.update()
