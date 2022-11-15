# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : Zombie Mob1.0.py
# @Time    : 2022/10/27 17:28
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :https://blog.csdn.net/weixin_55267022/article/details/122382934
# http://jharbour.com/
# @Description: $END$面向对象

import warnings

import pygame.time

from direction import *
from MyLibrary_1 import *

from health import Health
from player import Players
from zombies import Zombies
from saving import SaveScores

warnings.filterwarnings("ignore")


class Game(object):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Collision Demo")
        self.font = pygame.font.Font(None, 30)
        # 使帧变动按照一定的时间间隔发生
        self.timer = pygame.time.Clock()

        self.player = Players()
        self.zombie = Zombies()
        self.health = Health()

        self.game_over = False
        self.fps = 60
        self.pause = False

        self.saving = SaveScores("resource/data.json")
        self.score, self.time, self.speed = self.saving.getting_datas()

    def print_status(self):
        # 画血条
        pygame.draw.rect(self.screen, (50, 150, 50, 180), Rect(300, 570, self.player.player_health * 2, 25))
        pygame.draw.rect(self.screen, (100, 200, 100, 180), Rect(300, 570, 200, 25), 2)

        # 分数
        print_text(self.font, 0, 0, "Score:{:2d}    {:2d}".format(self.score, self.player.score))
        print_text(self.font, 0, 30, "Time:{:2d}   {:2d}"
                   .format(self.time, self.player.live_time))
        print_text(self.font, 0, 60, "Speed:{:.2f}    {:.2f}".format(self.speed, self.player.speed))
        print_text(self.font, 0, 90, "Zombie:{:2d}    {:.2f}"
                   .format(self.zombie.zombie_number, self.zombie.zombie.speed))

        if self.game_over:
            print_text(self.font, 300, 100, "G A M E O V E R")
            self.saving.saving_datas(self.player.score, self.player.live_time, self.player.speed)

    def update_draw(self):
        if not self.game_over:
            self.player.update(self.ticks, self.fps)
        self.player.collide(self.zombie)
        self.zombie.update(self.ticks, self.fps, self.game_over, self.player)
        self.health.update(self.ticks, self.player, self.zombie)

        self.health.draw()
        self.zombie.draw()
        self.player.draw()

    def main(self):
        while True:
            # 将帧速率设置为30
            self.timer.tick(30)

            check_event(self, self.player)

            if not self.pause:
                # 为精灵动画定时
                self.ticks = pygame.time.get_ticks()

                self.screen.fill((50, 50, 100))

                self.update_draw()
                self.print_status()

                # 玩家死亡
                if self.player.player_health <= 0:
                    self.game_over = True

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.main()
