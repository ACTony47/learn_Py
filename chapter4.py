# #遍历整个列表
# magicians = ['alice', 'david']
# for magician in magicians: #遍历
#     print(f"{magician.title()}, that was a nice trick")
#     print(f"i can't wait to see your next show\n") #换行符要包含在双引号里面
# #缩进很重要 不能无端地缩进

# #practice
# pizzas = ['sausage', 'lemon', 'pineapple']
# for pizza in pizzas:
#     print(f"my favorate pizza is {pizza}")
#     print(f"{pizza} is very delicious\n")
# print(f"i like eating pizza")

#创建数值列表
# for value in range(1,5):
# #     print(value)
# # #from 1 to less than 5

# numbers = list(range(1,6)) 使用range函数为列表赋值
# print(numbers)

# numbers = list(range(1,11,2)) #第三个参数作为步长
# print(numbers)

# square = []
# for value in range(1,11):
#     square.append(value ** 2)
# print(square)

#列表推导式
# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# #切片
# players = ['a', 'b', 'c', 'd']
# print(players[0:3]) # start from 0（index) , 3 persons in total
# 如果前者未设置 默认从第一个开始 后者未设置 默认到最后一个元素

# #复制列表
# my_foods = ['apple', 'garbage', 'shit']
# his_foods = my_foods[:] #使用这种方法是可以得到两个不同的了列表 只是值不同·
# #如果是his_foods = my_foods 得到的不是两个列表
# print(his_foods[0:2])

#元组 不可变 tuple
dimensions = (200, 50)
print(dimensions[0])
#dimensions[0] = 100 不支持元素赋值
#但是支持将元组的值重新赋值
dimensions = (400, 100)
print(dimensions)



