class A:
    def __init__(self):
        self.n = 2

    def plus(self, m):
        print('当前对象是 {} 来自 A类的plus方法'.format(self))
        self.n += m

#声明B类，继承A类
class B(A):
    def __init__(self):
        self.n = 3

    def plus(self, m):
        print('当前对象是 {} 来自 B类的plus方法'.format(self))
        super().plus(m)
        # self.plus(m) # 死循环。下面详解。
        # A.plus(self,m) # 与super().plus(m) 效果一致，但有隐患，下面详解。
        self.n += 3

b = B()
b.plus(2)
print(b.n)