# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/23
# pickle模块是以二进制的形式序列化后保存到文件中（保存文件的后缀为”.pkl”）
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
import pickle

my_list = [123, 3.14, '道周', 'love']
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()
pickle_file = open('my_list.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
