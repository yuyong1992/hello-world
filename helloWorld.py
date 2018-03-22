# coding:utf-8
# '''
# num = 1
# str = '1'
# num2 = int(str)
# print("the end:%d" %(num + num2))
# answer = "好啊！"
# print(answer*3 + '...')
# '''
#
# '''
# # 隐藏部分内容
# phoneNumber = '18811133446'
# # hidingNumber = '*' * 7 + phoneNumber[7:]
# # print(hidingNumber)
# placeNumber = phoneNumber[7:]
# print('*' * 7 + placeNumber)
# '''
#
# #print('{} a word she can get what she {} for.'.format('With','came'))
# def text_create(name,msg):
#     desktop_path = 'E:\\Users\\'
#     full_path = desktop_path + name + '.txt'
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('Done')
# #text_create('hello','Hello,world!')
# def text_filter(word,censored_word = 'lame',change_word = 'awesome'):
#     return word.replace(censored_word,change_word)
# # text_filter('python is lame')
#
# def invest(amount = 1000,rate = 0.05,time = 1):
#     amount = amount * (1 + rate) ** time
#     print('{} year your amount is {}' .format(time,amount))
# f = invest(1000,0.05,2)

# import random
#
# print('<<<GAME START!>>>')
# yourAnswer = input('Big OR Small:')
# print('<<<ROLE THE DICE!>>>')
# point1 = random.randrange(1,7)
# point2 = random.randrange(1,7)
# point3 = random.randrange(1,7)
# points = [point1,point2,point3]
# if yourAnswer == 'Big':
#     if sum(points) >= 3 and sum(points) <= 10:
#         print('The points are:[{},{},{} ],you lose!'.format(point1,point2,point3))
#     else:
#         print('The points are:[{},{},{} ],you win!'.format(point1, point2, point3))
# elif yourAnswer == 'Small':
#     if sum(points) >= 3 and sum(points) <= 10:
#         print('The points are:[{},{},{} ],you win!'.format(point1,point2,point3))
#     else:
#         print('The points are:[{},{},{} ],you lose!'.format(point1, point2, point3))
# else:
#     print('Your input was invalid!')

# import random
# def roll_dice(number=3,points=None):
#     print(<<<< Roll The Dice! >>>>)
#     if points = None:
#         points = []
#     while number > 0:
#         point = random.randrange(1,7)
#         points.append(point)
#         number = number - 1
#     return points
# def roll_result(total):
#     isBig = 11 <= total <= 18
#     isSmall = 3 <= total <= 10
#     if isBig:
#         return 'Big'
#     if isSmall:
#         return 'Small'
# def start_game():
#     print(<<<<< Gane Start! >>>>>)
#     choices = ['Big','Small']
#     your_choice = input('Big or Small:')
#     if your_choice in choices:
#         points = roll_dice()
#         total = sum(points)
#         youWin = your_choice == roll_result(total)
#         if youWin:
#             print('The points are :',points,'You Win!')
#         else:
#

# import time
# a = []
# t0 = time.clock()
# for i in range(1,20000):
#     a.append(i)
# print(time.clock() - t0,"seconds process time")
#
# t1 = time.clock()
# b = [i for i in range(1,20000)]
# print(time.clock() - t1,"seconds process time")

# lyric = 'The night begin to shine, the night begin to shine.'
# words = lyric.split()
# print(words)

# import string
# path = 'E:\\Users\\test.txt'
# with open(path,'r') as file:
#     words = [raw_word.strip(string.punctuation).lower() for raw_word in file.read().split()]
#     words_set = set(words)
#     words_count = {word:words.count(word) for word in words_set}
#     for word in sorted(words_count,key=lambda x:words_count[x],reverse=True):
#         print('{} - {} times'.format(word,words_count[word]))

# class CocaCola:
#     colaries = 140
#     sodium = 45
#     total_carb = 39
#     caffeine = 34
#     ingredients = [
#         'High Fructose Corn Syrup',
#         'Carbonated Water',
#         'Phosphoric Acid',
#         'Natural Flavors',
#         'Caramel Color',
#         'Caffeine'
#     ]
#     def __init__(self,logo_name):
#         self.logo_name = logo_name
#     def drink(self):
#         print('You have got {} cal energy!'.format(self.colaries))
# class CaffeineFree(CocaCola):
#     colaries = 0
#     ingredients = [
#         'High Fructose Corn Syrup',
#         'Carbonated Water',
#         'Phosphoric Acid',
#         'Natural Flavors',
#         'Caramel Color'
#     ]
# coke = CaffeineFree('CocaCola-Free')
# coke.drink()

# class TestA:
#     attr = 1
# inst_a = TestA()
# inst_a.attr = 40
# print(inst_a.attr)

# class Test:
#     attr = 1
# inst_a = Test()
# inst_b = Test()
# inst_a.attr = 40
# print(inst_b.attr)

# class test:
#     attr = 1
#     def __init__(self):
#         self.attr = 40
# ins_a = test()
# print(ins_a.attr)

# obj1 = 1
# obj2 ='string'
# obj3 = []
# obj4 = {}
#
# print(type(obj1),type(obj2),type(obj3),type(obj4))