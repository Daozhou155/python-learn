# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/9
#__len()__.__getitem()__

class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]


c1 = CountList(1, 3, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)

print(c1[1])
print(c2[1])
print(c1[1]+c2[1])
print(c1.count)
