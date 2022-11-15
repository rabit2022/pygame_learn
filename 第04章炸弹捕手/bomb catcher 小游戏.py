# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:42:49 2015
@author: liuchang
"""

import random
import sys

import pygame
from pygame.locals import *


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


pygame.init()
screen = pygame.display.set_mode((600, 520))
pygame.display.set_caption("bomb game")
pygame.mouse.set_visible(False)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

lives = 3
score = 0
# 判断是否需要重启游戏
game_over = True
font1 = pygame.font.Font(None, 30)

fcclock = pygame.time.Clock()  # 创建一个时间对象
fps = 60

mouse_x = mouse_y = 0
pos_x = 300
pos_y = 460

bomb_x = random.randint(0, 500)
bomb_y = -50

vel_y = 0.7

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            move_x, move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    if game_over:
        print_text(font1, 100, 200, "<click to play>")
    else:
        bomb_y += vel_y
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
        elif bomb_y > pos_y:
            if pos_x < bomb_x < pos_x + 120:
                score += 10
                bomb_x = random.randint(0, 500)
                bomb_y = -50

        pygame.draw.circle(screen, black, (bomb_x - 4, bomb_y - 4), 30, 0)
        pygame.draw.circle(screen, yellow, (bomb_x, bomb_y), 30, 0)

        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500

        pygame.draw.rect(screen, black, (pos_x - 4, pos_y - 4, 120, 40), 0)
        pygame.draw.rect(screen, red, (pos_x, pos_y, 120, 40), 0)

    # draw score and lives
    print_text(font1, 0, 0, "lives: " + str(lives))
    print_text(font1, 500, 0, "score :" + str(score))

    pygame.display.update()
    fcclock.tick(fps)
