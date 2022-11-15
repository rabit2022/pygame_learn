# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : Orbiting Spaceship.py
# @Time    : 2022/10/26 20:29
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :https://blog.csdn.net/weixin_55267022/article/details/122277260
# @Description: $END$

import math
import pygame
import sys

from pygame.locals import *


class Point(object):
    '''Point class'''

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x

    x = property(getx, setx)

    # Y property
    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y

    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
               ",Y:" + "{:.0f}".format(self.__y) + "}"


# print_text function
def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


# wrap_angle function
def wrap_angle(angle):
    return angle % 360


# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("送给寒武纪白")
font = pygame.font.Font(None, 18)

# load bitmaps
# convert()位图转换成为本地颜色深度，作为一种优化，若在一开始加载的时候没有转换，则每次绘制的时候都要进行转换，代价比较大。
# convert_alpha()用透明方式绘制前景对象
space = pygame.image.load("resource/space.png").convert_alpha()
planet = pygame.image.load("resource/mars_plane.png").convert_alpha()
ship = pygame.image.load("resource/satellite.png").convert_alpha()

width, height = ship.get_size()
# pygame.transform.scale()函数对其进行放缩，缩小了一半。
# 当然，也可以用另一种更好技术的放缩函数：smoothscale()
ship = pygame.transform.smoothscale(ship, (width // 2, height // 2))

radius = 250
angle = 0.0

pos = Point(0, 0)
old_pos = Point(0, 0)

fcclock = pygame.time.Clock()
fps = 600

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # draw background
    screen.blit(space, (0, 0))

    # draw planet
    width, height = planet.get_size()
    screen.blit(planet, (400 - width / 2, 300 - height / 2))

    # move the ship
    angle = wrap_angle(angle - 0.1)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius

    # rotate the ship
    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    # atan2反正切。返回角度
    rangle = math.atan2(delta_y, delta_x)
    # print(rangle)
    rangled = wrap_angle(-math.degrees(rangle))

    # rotate返回新的图像
    scratch_ship = pygame.transform.rotate(ship, rangled)

    # draw the ship
    width, height = scratch_ship.get_size()
    x = 400 + pos.x - width // 2
    y = 300 + pos.y - height // 2
    screen.blit(scratch_ship, (x, y))

    print_text(font, 0, 0, "Orbit:" + "{:.0f}".format(angle))
    print_text(font, 0, 20, "Rotation:" + "{:.2f}".format(rangle))
    print_text(font, 0, 40, "Position:" + str(pos))
    print_text(font, 0, 60, "Old Pos:" + str(old_pos))

    pygame.display.update()

    # remember position
    old_pos.x = pos.x
    old_pos.y = pos.y

    fcclock.tick(fps)
