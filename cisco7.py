class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
        def _iter_(self):
         return self
        def _next_(self):
           if self.i == len(self.s):
              raise StopIteration
           v = self.s[self.i]
           self.i += 1
           return v
for x in I():
   print(x,end='') 
        