# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : MyLibrary.py
# @Time    : 2022/10/27 20:57
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import pygame
from pygame.locals import *


# 类中的X、Y、position用于设置精灵的位置
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        # 调用父类的初始化方法
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def getx(self):
        return self.rect.x

    def setx(self, value):
        self.rect.x = value

    X = property(getx, setx)

    def gety(self):
        return self.rect.y

    def sety(self, value):
        self.rect.y = value

    Y = property(gety, sety)

    def getpos(self):
        return self.rect.topleft

    def setpos(self, pos):
        self.rect.topleft = pos

    position = property(getpos, setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        # 帧变动
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            # 当帧发生变化时，进行修改
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
                # 将要展示的图片送给image属性，以便展示出来
                self.image = self.master_image.subsurface(rect)
                self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + "," + str(self.last_frame) + \
               "," + str(self.frame_width) + "," + str(self.frame_height) + "," + \
               str(self.columns) + "," + str(self.rect)


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x

    x = property(getx, setx)

    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y

    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + ",Y:" + "{:.0f}".format(self.__y) + "}"


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    # screen变量的简化
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x, y))


