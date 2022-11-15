# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:41:03 2015
@author: liuchang
"""


import sys, pygame
from pygame.locals import *


# reload(sys)
# 定义一些变量：
score = 0
scored = False
failed = False
wronganswer = 0
current = 0
total = 0
data = []
correct = 0

# 先显示主界面
pygame.init()
screen = pygame.display.set_mode((780, 500))
pygame.display.set_caption("the trivia game")
screen.fill((200, 200, 200))
# 定义字体
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 40)
# 定义颜色
white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0
black = 0, 0, 0
colors = [white, white, white, white]
currentquestion = 1
# 读取数据，打印在gui当中
data_file = open("trivia.txt", "rt")
datas = data_file.readlines()
print(data)
data_file.close()

for lines in datas:
    total += 1
    data.append(lines.strip())


# 打印方法
def print_text(x, y, font, text, color=(255, 255, 255), shadow=True):
    # 先打印阴影部分
    # if shadow:
    # imgText = font.render(text,True,(0,0,0))
    # screen.blit(imgText,(x+2,y+2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))
    # print("printing...")


def show_question():
    # 画基本信息
    global score
    print_text(190, 5, font1, "trivia game", purple)
    print_text(190, 35, font2, "press keys(1-4)to answer ", purple)
    print_text(600, 5, font2, "score", purple)
    print_text(600, 25, font2, str(score), purple)
    # print(score)
    # 画当前答题情况
    global current
    global data
    global colors
    global correct
    global currentquestion
    question = current
    question = currentquestion
    correct = int(data[current + 5])
    print_text(5, 80, font1, "question :" + str(question))
    print_text(20, 120, font2, data[current], yellow)
    print_text(5, 200, font1, "answers")

    # 如果已经作答需要将结果用颜色表示出来

    if scored:
        colors = [white, white, white, white]
        colors[correct - 1] = green
        print_text(230, 380, font2, "correct", green)
        print_text(170, 420, font2, "press enter for next question", green)
    elif failed:
        colors = [white, white, white, white]
        colors[correct - 1] = green
        colors[wronganswer - 1] = red
        print_text(230, 380, font2, "incorrect", red)
        print_text(170, 420, font2, "press enter for next question", red)

    print_text(20, 240, font2, "1-" + data[current + 1], colors[0])
    print_text(20, 270, font2, "2-" + data[current + 2], colors[1])
    print_text(20, 300, font2, "3-" + data[current + 3], colors[2])
    print_text(20, 330, font2, "4-" + data[current + 4], colors[3])


# 判断是否可以进入下一题


def handle_input(num):
    global score
    global scored
    global failed
    global wronganswer
    global correct

    if num == correct:
        scored = True
        score += 1
        print("correct answer")
    else:
        failed = True
        wronganswer = num


def next_question():
    global scored
    global failed
    global colors
    global current

    if scored or failed:
        print("get next question....")
        # 要做一些清理任务
        scored = False
        failed = False
        colors = [white, white, white, white]
        # 换题
        current += 6
        global currentquestion
        currentquestion += 1
        if current >= total:
            current = 0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        # 添加按键响应，以及对应的题目的填写
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                print("1 \n")
                handle_input(1)
            elif event.key == pygame.K_2:
                print("2 \n")
                handle_input(2)
            elif event.key == pygame.K_3:
                print("3 \n")
                handle_input(3)
            elif event.key == pygame.K_4:
                print("4 \n")
                handle_input(4)
            elif event.key == pygame.K_RETURN:
                print("enter \n")
                next_question()
            screen.fill((200, 200, 200))
    show_question()
    # screen.fill((200,200,200))
    pygame.display.update()
