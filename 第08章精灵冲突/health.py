# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : health.py
# @Time    : 2022/10/28 11:22
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import random

from MyLibrary_1 import *


class Health(object):
    def __init__(self):
        self.health_create()

    def health_create(self):
        self.health_group = pygame.sprite.Group()
        # 创建n个血包
        for n in range(0, 6):
            health = MySprite()
            health.load("resource/heart.png", 1, 1)
            health.position = random.randint(0, 700), random.randint(0, 500)
            self.health_group.add(health)

    def update(self, ticks, player, zombie):
        # 更新血包组
        self.health_group.update(ticks, 50)

        self.player_attack(player)
        self.zombie_attack(zombie)

    def player_attack(self, player):
        # 玩家捡起血包
        attacker = None
        attacker = pygame.sprite.spritecollideany(player.player, self.health_group)
        if attacker is not None:
            if pygame.sprite.collide_rect_ratio(0.5)(player.player, attacker):
                player.player_health += 30
                player.score += 10
                player.speed += 0.1

                if player.player_health > 100:
                    player.player_health = 100
                attacker.position = random.randint(0, 700), random.randint(0, 500)

    def zombie_attack(self, zombie):
        # 僵尸捡起血包
        attacker = None
        attacker = pygame.sprite.groupcollide(zombie.zombie_group, self.health_group,
                                              False, False)
        if attacker is not None:
            for attacker1, attacker2_list in attacker.items():
                for attacker2 in attacker2_list:
                    if pygame.sprite.collide_rect_ratio(0.5)(attacker1, attacker2):
                        attacker1.speed += 0.4
                        attacker2.position = random.randint(0, 700), random.randint(0, 500)

    def draw(self):
        screen = pygame.display.get_surface()
        self.health_group.draw(screen)
