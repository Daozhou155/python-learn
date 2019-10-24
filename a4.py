#！/usr/bin/env python
#-*-coding:utf-8-*-
# author: zjr time:2019/8/18
#列表解析
list1 = [i*i for i in range(10)]
print(list1)
list2 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list2)
list3 = []
for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 != 0:
                 list3.extend([(x, y)])
print(list3)




