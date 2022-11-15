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
# @Description: $END$每10秒生成一个新的僵尸，分数系统，八个方向
import random
import sys

from MyLibrary_1 import *


def calc_velocity(direction, vel=1.0):
    """
    它需要一个方向和一个速度，并返回一个速度

    :param direction: 玩家面对的方向。
    :param vel: 人物的速度。
    :return: 具有 x 和 y 值的 Point 对象。
    :rtype: Point
    """
    velocity = Point(0, 0)
    # 上
    if direction == 0:
        velocity.y = -vel
    # 右
    elif direction == 2:
        velocity.x = vel
    # 下
    elif direction == 4:
        velocity.y = vel
    # 左
    elif direction == 6:
        velocity.x = -vel

    # 右上
    elif direction == 1:
        velocity.x = vel
        velocity.y = -vel
    # 右下
    elif direction == 3:
        velocity.x = vel
        velocity.y = vel
    # 左下
    elif direction == 5:
        velocity.x = -vel
        velocity.y = vel
    # 左上
    elif direction == 7:
        velocity.x = -vel
        velocity.y = -vel
    return velocity


# 转向
def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

    elif sprite.direction == 1:
        sprite.direction = 5
    elif sprite.direction == 3:
        sprite.direction = 7
    elif sprite.direction == 5:
        sprite.direction = 1
    elif sprite.direction == 7:
        sprite.direction = 3


def check_event():
    """
    如果玩家正在按键，则将玩家的方向设置为按键的方向，并将 player_moving 设置为 True
    """
    global player_moving
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    # 玩家向上移动
    elif keys[K_w] or keys[K_UP]:
        player.direction = 0
        player_moving = True
    elif keys[K_d] or keys[K_RIGHT]:
        player.direction = 2
        player_moving = True
    elif keys[K_s] or keys[K_DOWN] or keys[K_x]:
        player.direction = 4
        player_moving = True
    elif keys[K_a] or keys[K_LEFT]:
        player.direction = 6
        player_moving = True

    elif keys[K_q]:
        player.direction = 7
        player_moving = True
    elif keys[K_e]:
        player.direction = 1
        player_moving = True
    elif keys[K_z]:
        player.direction = 5
        player_moving = True
    elif keys[K_c]:
        player.direction = 3
        player_moving = True
    else:
        player_moving = False


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Collision Demo")
    font = pygame.font.Font(None, 30)
    # 使帧变动按照一定的时间间隔发生
    timer = pygame.time.Clock()

    # 创建组
    player_group = pygame.sprite.Group()
    zombie_group = pygame.sprite.Group()
    health_group = pygame.sprite.Group()

    # 创建玩家，初始方向为下
    player = MySprite()
    player.load("resource/farmer walk.png", 8, 8)
    player.position = 80, 80
    player.direction = 4
    player_group.add(player)

    # 创建10个僵尸，位置随机，方向随机
    for n in range(0, 10):
        zombie = MySprite()
        zombie.load("resource/zombie walk.png", 8, 8)
        zombie.position = random.randint(0, 700), random.randint(0, 500)
        # zombie.direction = random.randint(0, 3) * 2
        zombie.direction = random.randint(0, 7)
        zombie_group.add(zombie)

    # 创建3个血包
    for n in range(0, 3):
        health = MySprite()
        health.load("resource/heart.png", 1, 1)
        health.position = random.randint(0, 700), random.randint(0, 500)
        health_group.add(health)

    game_over = False
    player_moving = False
    player_health = 100

    live_time = 0  # 存活时间
    score = 0
    speed = 1.5

    while True:
        # 将帧速率设置为30
        timer.tick(30)

        # 为精灵动画定时
        ticks = pygame.time.get_ticks()
        if not game_over:
            live_time = (ticks // 1000)
            # print(live_time)

        check_event()

        if not game_over:
            # 根据玩家方向设置动画帧,direction的优点
            player.first_frame = player.direction * player.columns
            player.last_frame = player.first_frame + player.columns - 1
            # 确保动画帧始终位于第一帧和最后一帧之间。
            if player.frame < player.first_frame:
                player.frame = player.first_frame

            if not player_moving:
                # 玩家不按键就不移动
                player.frame = player.first_frame = player.last_frame
            else:
                # 设置移动的速度
                player.velocity = calc_velocity(player.direction, speed)
                player.velocity.x *= 1.5
                player.velocity.y *= 1.5

        # 更新玩家组
        player_group.update(ticks, 50)

        # 手动移动玩家
        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0:
                player.X = 0
            elif player.X > 700:
                player.X = 700
            if player.Y < 0:
                player.Y = 0
            elif player.Y > 500:
                player.Y = 500

        # 更新僵尸组
        zombie_group.update(ticks, 50)
        # 手动处理所有僵尸
        for z in zombie_group:
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns - 1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            z.velocity = calc_velocity(z.direction)

            z.X += z.velocity.x
            z.Y += z.velocity.y
            if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
                reverse_direction(z)

        # ticks是毫秒级，每10秒生成一个新的僵尸   使用定时器变量，使得每10秒增加一个僵尸
        # if ticks % 10000 == 0:
        if round(ticks % 100, 0) == 0:
            zombie = MySprite()
            zombie.load("resource/zombie walk.png", 8, 8)
            zombie.position = random.randint(0, 700), random.randint(0, 500)
            # zombie.direction = random.randint(0, 3) * 2
            zombie.direction = random.randint(0, 7)
            zombie_group.add(zombie)

        # 检测玩家是否与僵尸发生碰撞
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, zombie_group)
        if attacker is not None:
            # 若发生碰撞，则进行更加精确的检测，矩形缩小50%%
            if pygame.sprite.collide_rect_ratio(0.5)(player, attacker):
                player_health -= 10
                if attacker.X < player.X:
                    attacker.X -= 10
                elif attacker.X > player.X:
                    attacker.X += 10
            else:
                attacker = None

        # 更新血包组
        health_group.update(ticks, 50)
        # 玩家捡起血包
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, health_group)
        if attacker is not None:
            if pygame.sprite.collide_rect_ratio(0.5)(player, attacker):
                player_health += 30
                score += 10
                speed += 0.1

                if player_health > 100:
                    player_health = 100
                attacker.position = random.randint(0, 700), random.randint(0, 500)

        # 玩家死亡
        if player_health <= 0:
            game_over = True

        screen.fill((50, 50, 100))

        health_group.draw(screen)
        zombie_group.draw(screen)
        player_group.draw(screen)

        # 画血条
        pygame.draw.rect(screen, (50, 150, 50, 180), Rect(300, 570, player_health * 2, 25))
        pygame.draw.rect(screen, (100, 200, 100, 180), Rect(300, 570, 200, 25), 2)
        # 分数
        print_text(font, 0, 0, "Score:{:2d}".format(score))
        print_text(font, 0, 35, "Living Time:{:2d}".format(live_time))
        print_text(font, 0, 60, "Speed:{:.2f}".format(speed))

        if game_over:
            print_text(font, 300, 100, "G A M E O V E R")

        pygame.display.update()
