# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/20
# 匿名函数
def ds(x):
    return 2 * x + 1


print(ds(5))

# lambda省下定义函数过程，精简代码，不需要考虑命名
g = lambda x: 3 * x + 1
print(g(5))

# filter 过滤函数
filter(None, [1, 0, False, True])  # 过滤掉非真内容
print(list(filter(None, [1, 0, False, True])))

print(list(filter(lambda n: not (n % 3), range(1, 100))))  # 打印100以内所有3的倍数
print([i for i in range(1, 100) if not (i % 3)])  # 列表推导式实现

h = lambda x: x % 2
temp = range(10)
k = filter(h, temp)
print(list(k))

# map 函数
j = list(map(lambda x: x * 2, range(10)))  # 把range（10）参数带入到lambda函数中
print(j)
#zip将两组数以元组的形式绑在一块
print(list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
#map后边可以用多个序列作为参数
print(list(map(lambda x, y: [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
list1 = list(map(lambda x, y: [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(list1[0:1])


