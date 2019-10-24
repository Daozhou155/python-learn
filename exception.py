# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/23
# file_name = input('请输入要打开的文件名：')
# f = open(file_name)
# print('文件内容是：')
# for each_line in f:
#   print(each_line)
# 异常处理
try:
    int(123)  # try语句一旦监测到异常，后边的语句不再处理
    f = open('我是一个文件.txt', 'w')
    print(f.write('我存在了'))
    sum = 1 + '1'
    f.close()
except OSError as reason:  # 也可以写在一起：except (OSError,TypeError):
    print('文件出错\n原因是：' + str(reason))
except TypeError as reason:
    print('类型出错\n原因是：' + str(reason))
except:
    print('出错啦')
finally:  # 无论如何都会被执行
    f.close()

# 引发一个异常
raise ZeroDivisionError('除数不能为零')
