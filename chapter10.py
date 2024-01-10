# 文件 错误&异常处理 json
# from pathlib import Path
# path = Path('text.txt')
# contents = path.read_text()
# contents = contents.rstrip()
# print(contents)
# from pathlib import Path
# 访问文件的各行
# path = Path('text.txt')
# contents = path.read_text().rstrip()
# lines = contents.splitlines()
# for line in lines:
#     print(line[1])

#big scale file
# path = Path('text.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# pi = ''
# for line in lines:
#     pi += line.lstrip()
#
# name = input("enter your birthday")
# if name in pi:
#     print("yes")
# else:
#     print("no")
# string = "hello i like your mom"
# string = string.replace('your', 'your_dad\'s')
# print(string)

#写入文件
# path = Path('programming.txt')
# path.write_text('i love u')
#
# contents = 'i love u ,too\n'
# contents += 'i love your mom either\n'
# path.write_text(contents)

#exception 异常
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('you r wrong')
# name = input('enter your file name ') #path并不会对文件进行具体操作 而是调用path的函数时才会发现文件不存在
# path = Path(name)
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError as e:
#     print(f"{e}")
# else:
#     print('file found!')
# file_list = [
#
# ]
# while True:
#     file_name = input("enter file name and enter q to exit")
#     if file_name == 'q':
#         break
#     else:
#         file_list.append(file_name)
#
# for name in file_list:
#     path = Path(name)
#     try:
#         contents = path.read_text().splitlines()
#     except FileNotFoundError as e:
#         print(e)
#     else:
#         for pet in contents:
#             print(f"{pet} is a {name[0:3]}")

#使用json来存储数据 JavaScript object notation
# from pathlib import Path
# import json

# nums = [1,2,3,4,7]
# path = Path('numbers.json')
# contents = json.dumps(nums)
# path.write_text(contents)

# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)

