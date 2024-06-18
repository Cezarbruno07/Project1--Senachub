""" class A:
    def a (self):
        print('a')

class B:
    def a(self):
        print('b')
class C(B,A):
    def c(self):
        self.a()
o=C()
o.c() """

""" try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args)) """

""" numbers=(i*i for i in range(5)) """

""" x="\\\\"
print(len(x)) """

""" from datetime import timedelta

delta=timedelta(weeks=1,days=7,hours=11)
print(delta*2) """

""" try:
    raise Exception
except Exception:
    print("a")
except Exception:
    print("b")
except:
    print("c") """


""" assert var !=0 """

""" print(chr(ord('p')+2)) """

""" class A:
    def _init_(self):
        pass
a = A(1)
print(hasattr(a,'A')) """

""" for x in open('file','rt'):
    print(x) """

class I:
    def__init__(self):
    