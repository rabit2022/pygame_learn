# -*- coding: utf-8 -*-
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

piece = [None, False, False, False, False]


def draw_num(info, oper1, oper2):
    # draw four numbers
    textImg = myfont.render(str(info), True, color)
    axis_x = eval("x" + oper1 + "radius/2-20")
    axis_y = eval("y" + oper2 + "radius/2")
    screen.blit(textImg, (axis_x, axis_y))


def draw_piece(start, oper1, oper2):
    start_angle = math.radians(start)  # 90度转弧度
    end_angle = math.radians(start + 90)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    axis_x = eval("y" + oper1 + "radius")
    axis_y = eval("x" + oper2 + "radius")
    pygame.draw.line(screen, color, (x, y), (x, axis_x), width)
    pygame.draw.line(screen, color, (axis_y, y), (x, y))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece[1] = True;
            elif event.key == pygame.K_2:
                piece[2] = True;
            elif event.key == pygame.K_3:
                piece[3] = True;
            elif event.key == pygame.K_4:
                piece[4] = True;

    # clear the screen
    screen.fill((0, 200, 200))

    # draw four numbers
    draw_num(1, "-", "-")
    draw_num(2, " + ", "-")
    draw_num(3, "-", " + ")
    draw_num(4, " + ", " + ")

    # draw which piece??
    if piece[1]:
        draw_piece(90, "-", "-")
    if piece[2]:
        draw_piece(0, "-", " + ")
    if piece[3]:
        draw_piece(180, " + ", "-")
    if piece[4]:
        draw_piece(270, " + ", " + ")

    # is finished??
    if piece[1] and piece[2] and piece[3] and piece[4]:
        color = 0, 255, 0

    pygame.display.update()
