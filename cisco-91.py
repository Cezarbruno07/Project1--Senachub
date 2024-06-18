class A:
    def _init_(self,v = 1):
        self_v = v
    def set (self,v):
        self.v = v
        return v
a = A()
print(a.set(a.v+1))