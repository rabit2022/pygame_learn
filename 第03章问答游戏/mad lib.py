# https://blog.csdn.net/LSYtop/article/details/51757152

# print('MAD LIB GAME !')
#
# guy = input('what\'s your name? ')
# arm = input('what arm do you have ?')
# place_to_go = input('where to go ?')
# thing_to_do = input('what do you want to do ?')
# monster = input('Monster is ?')
# start_time = input('when start to go ?')
# end_time = input('when end ?')
#
# result = 'you are winner'
#
# story = """
#     My name is GUY, I want to go to PLACE. Because I want to beat a Monster, I have a ARM so I decide to THING ,
#     I will go at START , and back at END.
#     Finally, The GUY fight whith MONSTER, result is RESULT.
#     """
#
# dic = {'GUY': guy, 'ARM': arm, 'PLACE': place_to_go, 'THING': thing_to_do, 'START': start_time, 'END': end_time,
#        'RESULT': result, 'MONSTER': monster}
#
# for i in dic:
#     story = story.replace(i, dic[i])
#
# print(story)

#coding=utf-8
# https://www.jianshu.com/p/fa2f6a3bd8d0
# madlibs是欧美曾流行的一种群体游戏. 比较象我们的故事接龙大家共同编造一个故事...
# 故事可能随着个人不同的想象变化,最后也不知道会发展成什么样子
# 疯狂填词

print("MAD LIB GAME")
print("请根据提示输入以下问题的答案\n")


guy = input("一个男名人的名字: ")
girl = input("一个女名人的名字: ")
food = input("你最喜欢的食物: ")
ship = input("一架宇宙飞船的名字: ")
job = input("一个职业名称: ")
planet = input("一个星球名称: ")
drink = input("你最喜欢的饮料: ")
number = input("一个从1到10的数字: ")

story = "\n一对著名的已婚夫妇, GUY和GIRL, 前往PLANET这颗星球去度假. 他们乘坐SHIP飞船花费了NUMBER星期才来到了那里. " \
        "他们一边吃着FOOD, 一边喝着DRINK, 一边享受着豪华的烛光晚餐. " \
        "他们为了JOB的工作>，所以不得不缩短假期. "

story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("FOOD", food)
story = story.replace("SHIP", ship)
story = story.replace("NUMBER", number)
story = story.replace("DRINK", drink)
story = story.replace("PLANET", planet)
story = story.replace("JOB", job)

print(story)
