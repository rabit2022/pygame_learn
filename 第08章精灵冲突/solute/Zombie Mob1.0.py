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
# @Description: $END$原版

import random

from MyLibrary import *


def calc_velocity(direction, vel=1.0):
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


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Collision Demo")
    font = pygame.font.Font(None, 40)
    # 使帧变动按照一定的时间间隔发生
    timer = pygame.time.Clock()
    # 创建组
    player_group = pygame.sprite.Group()
    zombie_group = pygame.sprite.Group()
    health_group = pygame.sprite.Group()
    # 创建玩家，初始方向为下
    player = MySprite()
    player.load("resource/farmer walk.png", 96, 96, 8)
    player.position = 80, 80
    player.direction = 4
    player_group.add(player)
    # 创建10个僵尸，位置随机，方向随机
    # zombie_image = pygame.image.load("zombie walk.png").convert_alpha()
    for n in range(0, 10):
        zombie = MySprite()
        zombie.load("resource/zombie walk.png", 96, 96, 8)
        zombie.position = random.randint(0, 700), random.randint(0, 500)
        zombie.direction = random.randint(0, 3) * 2
        zombie_group.add(zombie)
    # 创建血包
    health = MySprite()
    health.load("resource/heart.png", 32, 32, 1)
    health.position = 400, 300
    health_group.add(health)

    game_over = False
    player_moving = False
    player_health = 100

    while True:
        # 将帧速率设置为30
        timer.tick(30)
        # 为精灵动画定时
        ticks = pygame.time.get_ticks()

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
        elif keys[K_s] or keys[K_DOWN]:
            player.direction = 4
            player_moving = True
        elif keys[K_a] or keys[K_LEFT]:
            player.direction = 6
            player_moving = True
        else:
            player_moving = False

        if not game_over:
            # 根据玩家方向设置动画帧
            player.first_frame = player.direction * player.columns
            player.last_frame = player.first_frame + player.columns - 1
            if player.frame < player.first_frame:
                player.frame = player.first_frame

            if not player_moving:
                # 玩家不按键就不移动
                player.frame = player.first_frame = player.last_frame
            else:
                # 设置移动的速度
                player.velocity = calc_velocity(player.direction, 1.5)
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

        # 检测玩家是否与僵尸发生碰撞
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, zombie_group)
        if attacker is not None:
            # 若发生碰撞，则进行更加精确的检测
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
        if pygame.sprite.collide_rect_ratio(0.5)(player, health):
            player_health += 30
            if player_health > 100:
                player_health = 100
            health.position = random.randint(0, 700), random.randint(0, 500)
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

        if game_over:
            print_text(font, 300, 100, "G A M E O V E R")

        pygame.display.update()
