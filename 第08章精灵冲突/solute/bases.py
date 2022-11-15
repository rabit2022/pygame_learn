# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : direction.py
# @Time    : 2022/10/28 10:38
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import functools
import sys

from MyLibrary_1 import *


data_keys = {0: [4, lambda vel: [0, -vel], [K_w, K_UP]],
             1: [5, lambda vel: [vel, -vel], [K_e]],
             2: [6, lambda vel: [vel, 0], [K_d, K_RIGHT]],
             3: [7, lambda vel: [vel, vel], [K_c]],

             4: [0, lambda vel: [0, vel], [K_s, K_DOWN, K_x]],
             5: [1, lambda vel: [-vel, vel], [K_z]],
             6: [2, lambda vel: [-vel, 0], [K_a, K_LEFT]],
             7: [3, lambda vel: [-vel, -vel], [K_q]],
             }


@functools.lru_cache
def get_direction(key):
    """
    它接受一个键作为输入，并返回一个键的元组和键的方向
    预存储技术
    :param key: 我们想要获得方向的关键
    :return: 两个元素的元组。第一个元素是 data_keys 字典中的键列表。第二个元素是键的方向。
    """

    def process(key):
        """
        它将一个键作为输入，并返回与输入键在同一行、列或框中的键的列表，以及键的方向（行、列或框）

        :param key: 被按下的键
        :return: data_keys 字典中的键列表和键的方向。
        """
        res = []
        direction = 0
        keys = list(data_keys.keys())
        values = (data_keys.values())
        for idx, val in enumerate(values):
            if key in val[2]:
                res.append(key)
                direction = keys[idx]
        return res, direction

    return process(key)


def calc_velocity(direction, vel=1.0):
    """
    预测位置
    :param direction: 玩家面对的方向。
    :param vel: 人物的速度。
    :return: 具有 x 和 y 值的 Point 对象。
    :rtype: Point
    """
    velocity = Point(0, 0)
    velocity.x, velocity.y = data_keys[direction][1](vel)
    return velocity



def reverse_direction(sprite):
    '''
    转向
    :param sprite: image+rect=sprite
    :return:
    '''
    sprite.direction = data_keys[sprite.direction][0]


def check_event(player: "Players"):
    """
    如果玩家正在按键，则将玩家的方向设置为按键的方向，并将 player_moving 设置为 True
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            val, direction = get_direction(event.key)
            if event.key in val:
                player.player.direction = direction
                player.player_moving = True
            elif event.key == K_ESCAPE:
                sys.exit()
        elif event.type == KEYUP:
            player.player_moving = False
