a = 'name'
print(type(a))
小甲鱼 = '游泳'
print(小甲鱼)
print(1 > 3 and 2 < 4)
print(1 and 3)
print(3 or 4)
print(3.0 // 2.0)
print(3.0 / 2.0)
print(5 ** -2)
# 三元操作符
x, y, z = 6, 5, 4
smll = x if (x < y and x < z) else (y if y < z else z)
print(smll)
# 列表扩展
number = [1, 2, 3, 4]
number.append('a')
print(number)
number.extend('b')
print(number)
number.extend(['c', 'd'])
print(number)
number.append(['e', 'f'])
print(number)
number.insert(4, 5)
print(number)
