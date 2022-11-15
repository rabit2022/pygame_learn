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
import functools
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

    def __imul__(self, other):
        """
        该函数接受一个 Point 对象并将 Point 对象的 x 和 y 值设置为另一个 Point 对象的 x 和 y 值。

        :param other: 与当前对象相乘的另一个对象。
        """
        if isinstance(other, Point):
            self.x = other.x
            self.y = other.y

    def __sub__(self, other):
        """
        它取当前位置和旧位置之间的差异，
        然后使用 atan2 函数计算两点之间的角度，
        然后将角度从弧度转换为度，
        然后使角度为负，
        然后将角度包裹在 0 到 360 之间

        :param other: 我们从这个对象中减去的另一个对象。
        """
        if isinstance(other, Point):
            global angle
            # move the ship
            angle = wrap_angle(angle - speed)
            self.x = math.sin(math.radians(angle)) * radius
            self.y = math.cos(math.radians(angle)) * radius

            global distance
            distance += self.setDistance(other)

            # rotate the ship
            delta_x = self.x - other.x
            delta_y = self.y - other.y
            # atan2反正切。返回弧度
            rangle = math.atan2(delta_y, delta_x)

            # 将角度从弧度转换为度，然后将其设为负值，然后将其包装为 0 到 360 之间的值。
            rangled = wrap_angle(-math.degrees(rangle))
            return rangle, rangled

    # @functools.cache
    def setDistance(self, other):
        # 计算距离
        x0, y0 = (400 - width / 2, 300 - height / 2)  # planet圆心
        theta = abs(math.atan((other.y - y0) / (other.x - x0)) -
                    math.atan((self.y - y0) / (self.x - x0)))  # 圆心角
        arc_length = math.pi * radius * (theta / 180)  # 弧长公式
        # arc_length = math.sqrt((other.y / other.x) ** 2 + (self.y / self.x) ** 2)
        return arc_length


# print_text function
def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


# wrap_angle function
def wrap_angle(angle):
    return angle % 360


def check_event():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # 让程序可以通过按下向上键或者向下键实现飞船速度加快或者减慢
    # 加上这条语句方便可以一直按着键盘不松
    pygame.key.set_repeat(10)

    # 用于控制速度变化
    global speed
    if keys[K_UP]:
        speed += 0.01
    elif keys[K_DOWN]:
        speed -= 0.01

    if keys[K_r]:
        speed = 0.1
    elif keys[K_v]:
        speed += 1
    elif keys[K_c]:
        speed -= 1

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
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
speed = 0.1
distance = 0

pos = Point(0, 0)
old_pos = Point(0, 0)

fcclock = pygame.time.Clock()
fps = 60

# repeating loop
while True:
    check_event()

    # draw background
    screen.blit(space, (0, 0))

    # draw planet
    width, height = planet.get_size()
    screen.blit(planet, (400 - width / 2, 300 - height / 2))

    rangle, rangled = pos - old_pos
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
    print_text(font, 0, 80, "Distance:" + "{:.2f}".format(distance))
    print_text(font, 0, 100, "Speed:" + "{:.2f}".format(speed))

    pygame.display.update()

    # remember position
    old_pos.x = pos.x
    old_pos.y = pos.y
    # old_pos = pos

    fcclock.tick(fps)
