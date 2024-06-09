class A:
    def _str_(self):
        return 'a'
class B:
    def _str_(self):
        return'b'
class C(A,B):
        pass
o=c()
print(o)
