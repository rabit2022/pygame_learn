# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : generation.py
# @Time    : 2022/11/09 13:24
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$

class Generation(object):
    def __init__(self):
        self.live_time_alter = [_ for _ in range(100, 6000, 60)]
        self.speed_alter = [_ for _ in range(5, 500, 5)]
        self.probability_alter = [_ for _ in range(50, 3, -5)]
        self.number_limit_list = [_ for _ in range(10, 100, 5)]

        self.probability = self.probability_alter[0]
        self.number_limit = self.number_limit_list[0]
        # print(self.probability_alter)

        self.gg_dict = list(zip(self.live_time_alter, self.speed_alter, self.probability_alter,self.number_limit_list))
        # print(self.gg_dict)


if __name__ == '__main__':
    a = Generation()
