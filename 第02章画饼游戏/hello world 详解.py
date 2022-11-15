# 这是一个图形库，有了它就可以实现绘图
import sys

import pygame

# 这句代码的意义在于让代码变得简单 ，少敲几下键盘
from pygame.locals import *

########################以上举个例子，引入各种库，看你需要什么#############################
# 初始化代码， 准备工作做好
pygame.init()

# 绘制屏幕， 你的图形界面至少要出现在一个框子中，就是它了 screen， 后面是大小参数
screen = pygame.display.set_mode((800, 600))

# 字体, 这些有关图形的都是pygame 库所包含的
font = pygame.font.Font(None, 40)

# 颜色  ， 为了方便
red = (255, 0, 0)
white = (0, 0, 0)

# 文字 ， 这是你要显示的文字内容。 注意它只是内容。  要想显示 你需要把他变成图片（其实是位图，说图片好理解）
text = "Hello, World ! "

# 位图，  就是把你所说的内容，转化为位图，这样他才能够绘制在屏幕上，就行照片的底片一样。这里把你的‘图片文字’准备好
imgText = font.render(text, True, red)

######################以上举个例子，初始化就是这个样子######################################
##################
# 这个while就是一个循环主体，它是True就会一直循环， 想让游戏里面的东西动起来，其实就是不断的循环你创建出 #来的屏幕。
# 这一秒它在这里， 循环一次他又移动一段距离，下一秒有跑到哪里，快速的刷新下，就成了游戏里面动态的物体移动
##################
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    # 第一步就是先fill（把你屏幕背景充满颜色， 就用白色了）
    screen.fill(white)

    # 把你的‘图片文字’展示到屏幕上,后面是（x,y）坐标位置
    screen.blit(imgText, (400, 300))

    # 这里继续刷新,到这里你就可以显示一个图形界面的Hello，world了 ，  你想啊，让（x,y）坐标进行一个变化，每次刷新位置都改变，这不就是动态的界面了。   如果再通过If语句进行判断和 按键结合，就能控制方向。这不就是一个受控制的小游戏了。  当然还有很多逻辑，后续博客更新。。
    pygame.display.update()
