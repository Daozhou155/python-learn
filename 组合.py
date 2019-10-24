# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/26
class T:
    def __init__(self, x):
        self.num = x


class F:
    def __init__(self, x):
        self.num = x


# 组合：把类和实例化放到一个新类里
class P:
    def __init__(self, x, y):
        self.t = T(x)
        self.f = F(y)

    def print_num(self):
        print('水池里共有乌龟%d只，小鱼%d条' % (self.t.num, self.f.num))


pool = P(1, 10)
pool.print_num()


# 类定义->类对象->实例对象
class C:
    count = 0


a = C()
b = C()
print(a.count)
print(b.count)
a.count += 10  # 覆盖了类中count
print(a.count)
print(b.count)
C.count += 100
print(a.count)
print(b.count)


# 绑定


# 相关BIF
class A:
    pass


class B(A):
    pass


print(issubclass(B, A))  # B是A的子类返回true，一个类被认为是自身的子类
print(issubclass(B, B))
print(issubclass(B, object))  # object是所有类默认的父类
print(issubclass(B, C))

b1 = B()
print(isinstance(b1, B))  # 第一个参数是对象，检查第一个是不是第二个类的实例对象
print(isinstance(b1, A))
print(isinstance(b1, C))
print(isinstance(b1, (A, B, C)))  # 类可以是元组,有一个类符合即可


# hasattr(object,name)检查对象是否有指定的属性
class G:
    def __init__(self, x=0):
        self.x = x


g1 = G()
print(hasattr(g1, "x"))

# getattr(object,name[, default])得到对象的属性值
print(getattr(g1, 'x'))
print(getattr(g1, 'y', '您访问的属性不存在'))  # 如果属性不存在，则返回后面的

# setattr（object，name，value）设定属性值，如果属性不存在则新建并赋值
setattr(g1, 'y', '道周')
print(getattr(g1, 'y', '您访问的属性不存在'))

# delattr（object，name）删除属性，
delattr(g1, 'y')


# delattr(g1, 'y')#已经删除，属性不存在则报错

# property
class K:
    def __init__(self, size=10):
        self.size = size

    def getsize(self):
        return self.size

    def setsize(self, value):
        self.size = value

    def delsize(self):
        del self.size

    x = property(getsize, setsize, delsize)  # 获取、设置、删除属性


k1 = K()
print(k1.x)
k1.x = 20
print(k1.x)
print(k1.size)
print(k1.getsize())
del k1.x
