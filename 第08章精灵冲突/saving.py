# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : saving.py
# @Time    : 2022/10/28 16:56
# @Author  : 魏老师
# @Version : python3.10.8
# @IDE     : PyCharm
# @Origin  :
# @Description: $END$
import json


class SaveScores(object):
    def __init__(self, filename):
        self.filename = filename

    def _saving(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def _getting(self) -> dict:
        with open(self.filename, 'r') as f:
            # content = json.loads(f.read())
            content = json.load(f)
        self.content = content
        # print(content)
        return content

    def saving_datas(self, score=0, time=0, speed=0):
        content = self.content.copy()
        if score > self.score:
            self.score = score
            content["score"] = score
        if time > self.time:
            self.time = time
            content["time"] = time
        if speed > self.speed:
            self.speed = speed
            content["speed"] = speed

        if content != self.content:
            # 有变化，保存
            self._saving(content)

    def getting_datas(self):
        self.score, self.time, self.speed = self._getting().values()
        return self.score, self.time, self.speed


if __name__ == '__main__':
    s = SaveScores("resource/data.json")
    a, b, c = s.getting_datas()
    print(a, b, c)
    s.saving_datas(10)
