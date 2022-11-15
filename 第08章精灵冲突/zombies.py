# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : zombies.py
# @Time    : 2022/10/28 11:07
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import random

from direction import *
from MyLibrary_1 import *
from generation import Generation


class Zombies(object):
    def __init__(self):

        self.zombie_group = pygame.sprite.Group()
        self.zombie_number = 0

        self.generation = Generation()
        self.probabilities = self.generation.probability  # 生成概率
        self.number_limit = self.generation.number_limit

        # 创建10个僵尸，位置随机，方向随机
        for n in range(0, 10):
            self.zombies_create()

    def zombies_create(self, speed=1.5):
        self.zombie = MySprite()
        self.zombie.load("resource/zombie walk.png", 8, 8)
        self.zombie.position = random.randint(0, 700), random.randint(0, 500)
        self.zombie.direction = random.randint(0, 7)
        self.zombie.speed = random.uniform(1, speed)
        self.zombie_group.add(self.zombie)
        self.zombie_number += 1

    def collide(self):
        """
        僵尸之间相撞
        """
        # 当前僵尸一直在更新
        # 检测玩家是否与僵尸发生碰撞
        attacker = None
        attacker = pygame.sprite.groupcollide(self.zombie_group, self.zombie_group,
                                              False, False)  # spritecollideany
        if attacker is not None:
            for attacker1, attacker2_list in attacker.items():
                for attacker2 in attacker2_list:
                    # 若发生碰撞，则进行更加精确的检测，矩形缩小50%%
                    if pygame.sprite.collide_rect_ratio(0.5)(attacker1, attacker2):
                        if attacker1.X < attacker2.X:
                            attacker1.X -= 10
                        elif attacker1.X > attacker2.X:
                            attacker1.X += 10

    def update(self, ticks, fps, game_over, player):
        # 手动处理所有僵尸
        for z in self.zombie_group:
            z: Zombies.zombie

            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns - 1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            z.velocity = calc_velocity(z.direction, z.speed)
            # print(z.speed)

            z.X += z.velocity.x
            z.Y += z.velocity.y

            # 越界判断
            if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
                reverse_direction(z)

            # 推出边界
            if z.X < -5 or z.X > 705 or z.Y < -5 or z.Y > 505:
                z.kill()
                self.zombie_number -= 1
                if not game_over:
                    # player.score += 10
                    player.score += round(z.speed)
                    # print(round(z.speed))

        self.live_time = (ticks // 1000)
        # ticks是毫秒级，每10秒生成一个新的僵尸   使用定时器变量，使得每10秒增加一个僵尸
        # if ticks % 100 == 0:
        if self.zombie_number <= self.number_limit and random.randint(0, self.probabilities) == 1:
            self.zombies_create(3)

            # 80秒后，至少10个僵尸
            if self.live_time >= 80 and self.zombie_number <= self.number_limit - 5:
                for _ in range(self.number_limit - self.zombie_number - 5):
                    self.zombies_create(8)

            for item in self.generation.gg_dict:
                if not self.random_generate(*item):
                    # print(item[0],'generation')
                    break

            if not game_over:
                # 每生成一个僵尸，分数+1
                player.score += 1

        # 更新僵尸组
        self.zombie_group.update(ticks, fps)
        # 僵尸之间相撞
        self.collide()

    def random_generate(self, live_time, speed, probabilities, number_limit):
        """
        产生僵尸的概率,最大僵尸数量,随机生成僵尸

        :param live_time: 游戏运行的时间。
        :param speed: 僵尸的速度
        :param probabilities: 产生僵尸的概率
        :param number_limit: 可以同时生成的最大僵尸数量
        :return: 对或错
        """
        # 改变概率
        if probabilities <= self.probabilities:
            self.probabilities = probabilities
        if number_limit >= self.number_limit:
            self.number_limit = number_limit

        if self.live_time >= live_time:
            # 随机生成
            if random.randint(0, self.probabilities) == 1:
                self.zombies_create(speed)
            return True
        return False

    def draw(self):
        screen = pygame.display.get_surface()
        self.zombie_group.draw(screen)
