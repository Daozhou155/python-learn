# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/21
dict5 = {}
print(dict5.fromkeys((1, 2, 3)))
print(dict5.fromkeys((1, 2, 3), 'number'))
print(dict5.fromkeys((1, 3), 'book'))  # 不能修改原有字典，只是创建了一个新字典

# key，value item get 用法
dict5 = dict5.fromkeys(range(10), '赞')
for eachkey in dict5.keys():
    print(eachkey, end="")

for eachvalue in dict5.values():
    print(eachvalue, end="")

for eachitem in dict5.items():
    print(eachitem, end="")

print('\n')
print(dict5[9])

dict5.get(10, '无')
print(dict5.get(10, '无'))
print(dict5.get(9, '无'))

print(9 in dict5)
print(10 in dict5)

#清空字典
dict5.clear()
print(dict5)

#字典拷贝
x = {"a": 1, "b": 2, "c": 3}
y = x.copy()   #拷贝字典x
z = x          #只是给字典x换了个名字
z['d'] = 4
print(x, y, z)

