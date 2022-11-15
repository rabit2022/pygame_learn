# 导入游戏使用到的模块
import pygame
import sys

from pygame.locals import *



class Trivia(object):
    '''
    所有游戏的逻辑都在该类中实现
    '''
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        # read trivia data from file
        f = open(filename, "r")
        trivia_data = f.readlines()
        f.close()

        # count and clean up trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

        # print(self.data)

    def show_question(self):
        """
        在屏幕上显示问题和答案
        """
        # 正确答案，绿色
        # 错误答案，错误答案红色，正确答案绿色
        print_text(font1, 210, 5, "TRIVIA GAME")
        print_text(font2, 190, 500 - 20, "Press Keys (1-4) To Answer", purple)

        print_text(font2, 530, 5, "SCORE", purple)
        print_text(font2, 550, 25, str(self.score), purple)

        # get correct answer out of data
        self.correct = int(self.data[self.current + 5])
        # print(self.correct)

        # display question
        question = self.current
        print_text(font1, 5, 80, "QUESTION" + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        # respond to correct answer
        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct - 1] = green
            print_text(font1, 230, 380, "CORRECT!", green)
            print_text(font2, 170, 420, "Press Enter For Next Question", green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wronganswer - 1] = red
            self.colors[self.correct - 1] = green
            print_text(font1, 220, 380, "INCORRECT!", red)
            print_text(font2, 170, 420, "Press Enter For Next Question", red)

        # display answer
        print_text(font1, 5, 170, "ANSWERS")
        print_text(font2, 20, 210, "1 - " + self.data[self.current + 1], self.colors[0])
        print_text(font2, 20, 240, "2 - " + self.data[self.current + 2], self.colors[1])
        print_text(font2, 20, 270, "3 - " + self.data[self.current + 3], self.colors[2])
        print_text(font2, 20, 300, "4 - " + self.data[self.current + 4], self.colors[3])

    def handle_input(self, number):
        '''
        响应用户输入
        :param number:answers number
        :return:
        '''
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        '''
        Enter,重置颜色，标志，跳转下一个问题
        :return:
        '''
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0

            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0


# 主代码
def print_text(font, x, y, text, color=(255, 255, 255), shadow=True):
    """
    它需要一个字体、一个 x 和 y 坐标、一个字符串和一种颜色，然后将字符串打印到屏幕上

    :param font: 要使用的字体。
    :param x: 文本左上角的 x 坐标。
    :param y: 文本左上角的 y 坐标。
    :param text: 要呈现的文本。
    :param color: 文本的颜色。
    :param shadow: 如果为 True，则文本将带有黑色阴影。, defaults to True (optional)
    """
    if shadow:
        imgText = font.render(text, True, (0, 0, 0))
        screen.blit(imgText, (x - 2, y - 2))

    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


# 主程序初始化代码
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Trivia Game")

font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)

white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0

# load the Trivia data file
trivia = Trivia("./resource/t_data.txt")


# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()

    # clear the screen
    screen.fill((0, 0, 200))

    # display trivia data
    trivia.show_question()

    # update the display
    pygame.display.update()
