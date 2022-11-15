# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : Escape the Dragon.py
# @Time    : 2022/10/27 14:23
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :https://blog.csdn.net/weixin_55267022/article/details/122283772
# @Description: $END$

import random
import sys

import pygame
from pygame.locals import *


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        # 调用父类的初始化方法
        pygame.sprite.Sprite.__init__(self)

        self.master_image = None  # 整张图片

        self.frame = 0  # 当前帧
        self.old_frame = -1  # 上一帧
        self.first_frame = 0  # 开始帧
        self.last_frame = 0  # 最后一帧

        self.frame_width = 1  # 宽度
        self.frame_height = 1  # 高度
        self.columns = 1  # 列数

        self.last_time = 0  # 时间记录

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

    def load(self, filename, rows, columns):
        """
        该函数加载图像，设置帧的宽度和高度，设置列数，并设置最后一帧。

        :param filename: 精灵表的文件名。
        :param rows: 列数。
        :param columns: 精灵表中的列数。
        """
        self.master_image = pygame.image.load(filename).convert_alpha()
        width, height = self.master_image.get_size()

        self.frame_width = width // rows
        self.frame_height = height // columns

        self.rect = Rect(0, 0, self.frame_width, self.frame_height)
        self.columns = columns

        self.last_frame = rows * columns - 1

    def update(self, rate=30):
        """
        如果当前时间大于上次时间加上速率，则增加帧。
        如果该帧大于最后一帧，则将该帧设置为第一帧。
        将上次时间设置为当前时间。
        如果帧不等于旧帧，则将帧 x 和 y 坐标以及图像设置为主图像的次表面。
        将旧框架设置为框架

        :param current_time: 当前时间（以毫秒为单位）。
        :param rate: 帧之间的毫秒数。, defaults to 30 (optional)
        """
        # 为精灵动画定时
        current_time = pygame.time.get_ticks()
        # 帧变动
        if current_time > self.last_time + rate:
            self.frame += 1

            # 使动画重复的循环
            if self.frame > self.last_frame:
                self.frame = self.first_frame

            # 更新时间记录
            self.last_time = current_time

            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
                # 将要展示的图片送给image属性，以便展示出来
                self.image = self.master_image.subsurface(rect)

                # 记录上一帧
                self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + "," + str(self.last_frame) + \
               "," + str(self.frame_width) + "," + str(self.frame_height) + "," + \
               str(self.columns) + "," + str(self.rect)


def print_text(font, x, y, text, color=(255, 255, 255)):
    """
    它需要一个字体、一个 x 和 y 坐标、一个文本字符串和一种颜色，然后将文本打印到屏幕上

    :param font: 字体对象
    :param x: 文本左上角的 x 坐标。
    :param y: 文本左上角的 y 坐标。
    :param text: 要显示的文本。
    :param color: 文本的颜色。
    """
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def reset_arrow():
    """
    将箭头的位置y设置为随机,x为800的 坐标
    """
    y = random.randint(150, 400)
    arrow.position = 800, y


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escape The Dragon Game")
font = pygame.font.Font(None, 48)
# 使帧变动按照一定的时间间隔发生
framerate = pygame.time.Clock()

# 引入背景图片
bg = pygame.image.load("resource/background.png").convert_alpha()
# 创建一个精灵组
group = pygame.sprite.Group()

# 创建龙
dragon = MySprite(screen)
dragon.load("resource/飞龙1.png", 4, 4)
dragon.first_frame = 8
dragon.last_frame = 11
dragon.position = 100, 130
group.add(dragon)

# 创建玩家
player = MySprite(screen)
player.load("resource/法师.png", 4, 4)
player.first_frame = 0
player.last_frame = 3
player.position = 400, 303
group.add(player)

# 创建箭
arrow = MySprite(screen)
arrow.load("resource/arrow1.png", 1, 1)
arrow.position = 800, 320
group.add(arrow)

arrow_vel = 8.0
game_over = False
you_win = False
player_jumping = False
jump_vel = 0.0
player_start_y = player.Y

fcclock = pygame.time.Clock()
fps = 60

score = 0
# 用于判断玩家是否被击中
hit = False

while True:
    # 将帧速率设置为30
    framerate.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 加上这条语句方便可以一直按着键盘不松
    pygame.key.set_repeat(10)

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_SPACE]:
        if not game_over:
            if not player_jumping:
                player_jumping = True
            jump_vel = -8.0

    # 更新arrow
    if not game_over:
        arrow.X -= arrow_vel
        if arrow.X < -40:

            if not hit:
                score += 10

            reset_arrow()

    # 检测玩家和箭是否碰撞，被击中则往后退
    if pygame.sprite.collide_rect(arrow, player):
        hit = True
        reset_arrow()
        player.X -= 40

    # 检测龙和箭是否碰撞，被击中则往后退
    if pygame.sprite.collide_rect(arrow, dragon):
        score += 10
        reset_arrow()
        dragon.X -= 10

    # 检测玩家和龙是否碰撞，即玩家是否会被龙吃了
    if pygame.sprite.collide_rect(player, dragon):
        game_over = True

    # 龙被击中10次则游戏结束
    if dragon.X < 0:
        you_win = True
        game_over = True

    # 检测玩家跳跃
    if player_jumping:
        player.Y += jump_vel
        jump_vel += 0.5
        if player.Y > player_start_y:
            player_jumping = False
            player.Y = player_start_y
            jump_vel = 0.0

    # draw the background
    screen.blit(bg, (0, 0))

    # update the game
    if not game_over:
        group.update(50)
    # draw sprites
    group.draw(screen)

    print_text(font, 350, 560, "Press SPACE to jump!")
    print_text(font, 150, 560, "Score: " + str(score))

    if game_over:
        print_text(font, 360, 100, "G A M E O V E R")
        if you_win:
            print_text(font, 330, 130, "YOU BEAT THE DRAGON!")
        else:
            print_text(font, 330, 130, "THE DRAGON GOT YOU!")

    pygame.display.update()
    fcclock.tick(fps)
