# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : pie游戏字典版.py
# @Time    : 2022/10/26 10:58
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
pygame.display.set_caption("pie game")
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200  # 半径
position = x - radius, y - radius, radius * 2, radius * 2

piece = [True, False, False, False, False]

num_positions = [None, lambda x, y: (x - radius / 2 - 20, y - radius / 2),
                 lambda x, y: (x + radius / 2 - 20, y - radius / 2),
                 lambda x, y: (x - radius / 2 - 20, y + radius / 2 - 20),
                 lambda x, y: (x + radius / 2 - 20, y + radius / 2 - 20)
                 ]


def draw_num(nums):
    # draw four numbers
    textImg = myfont.render(str(nums), True, color)
    new_position = num_positions[nums](x, y)
    screen.blit(textImg, new_position)


piece_positions = [None, lambda x, y: (90, y - radius, x - radius),
                   lambda x, y: (0, y - radius, x + radius),
                   lambda x, y: (180, y + radius, x - radius),
                   lambda x, y: (270, y + radius, x + radius)
                   ]


def draw_piece(num):
    start, line1_param, line2_param = piece_positions[num](x, y)

    start_angle = math.radians(start)  # 90度转弧度
    end_angle = math.radians(start + 90)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    pygame.draw.line(screen, color, (x, y), (x, line1_param), width)
    pygame.draw.line(screen, color, (line2_param, y), (x, y))


button_list = [None, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            else:
                for idx in range(1, len(button_list)):
                    if event.key == button_list[idx]:
                        if not piece[idx]:
                            piece[idx] = True
                        elif piece[idx]:
                            piece[idx] = False

    # clear the screen
    screen.fill((0, 200, 200))

    for idx in range(1, len(piece)):
        # draw four numbers
        draw_num(idx)
        # draw piece
        if piece[idx]:
            draw_piece(idx)

    # is finished??
    # if piece[1] and piece[2] and piece[3] and piece[4]:
    if all(piece):
        color = 0, 255, 0
    else:
        color = 255, 0, 0

    pygame.display.update()
