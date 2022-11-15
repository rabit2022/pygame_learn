# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : self.player.py
# @Time    : 2022/10/28 10:36
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$

from MyLibrary_1 import *
from direction import calc_velocity


class Players(object):
    def __init__(self):
        self.player_moving = False
        # 玩家属性
        self.player_health = 100
        self.live_time = 0  # 存活时间
        self.score = 0
        self.speed = 1.5

        self.player_create()

    def player_create(self):
        self.player_group = pygame.sprite.Group()
        # 创建玩家，初始方向为下
        self.player = MySprite()
        self.player.load("resource/farmer walk.png", 8, 8)
        self.player.position = 80, 80
        self.player.direction = 4
        self.player_group.add(self.player)

    def update(self, ticks, fps):
        self.live_time = (ticks // 1000)

        # 根据玩家方向设置动画帧,direction的优点
        self.player.first_frame = self.player.direction * self.player.columns
        self.player.last_frame = self.player.first_frame + self.player.columns - 1
        # 确保动画帧始终位于第一帧和最后一帧之间。
        if self.player.frame < self.player.first_frame:
            self.player.frame = self.player.first_frame

        if not self.player_moving:
            # 玩家不按键就不移动
            self.player.frame = self.player.first_frame = self.player.last_frame
        else:
            # 设置移动的速度
            self.player.velocity = calc_velocity(self.player.direction, self.speed)
            self.player.velocity.x *= 1.5
            self.player.velocity.y *= 1.5

        # 手动移动玩家
        if self.player_moving:
            self.player.X += self.player.velocity.x
            self.player.Y += self.player.velocity.y
            if self.player.X < 0:
                self.player.X = 0
            elif self.player.X > 700:
                self.player.X = 700
            if self.player.Y < 0:
                self.player.Y = 0
            elif self.player.Y > 500:
                self.player.Y = 500

        # 更新玩家组
        self.player_group.update(ticks, fps)

    def collide(self, zombie):
        # 检测玩家是否与僵尸发生碰撞
        attacker = None
        attacker = pygame.sprite.spritecollideany(self.player, zombie.zombie_group)
        if attacker is not None:
            # 若发生碰撞，则进行更加精确的检测，矩形缩小50%%
            if pygame.sprite.collide_rect_ratio(0.5)(self.player, attacker):
                self.player_health -= 6
                if attacker.X < self.player.X:
                    attacker.X -= 10
                elif attacker.X > self.player.X:
                    attacker.X += 10
            else:
                attacker = None

    def draw(self):
        screen = pygame.display.get_surface()
        self.player_group.draw(screen)
