class A:
  x = 0
  def _init_ (self,v = 0):
    self.Y=v
    A.X += v 

a = A ()
b = A (1)
c = A (2)
print(c.x)