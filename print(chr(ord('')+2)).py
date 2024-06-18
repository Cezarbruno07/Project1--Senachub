""" class A:
    def __init__ (self):
        pass
    def f (self):
        return 1
    def g ():
        return self.f()
a = A()
print(a.g())
 """

############################################
""" class B
    def a (self):
        print('b')
class C(B,A):
    def c (self):
        self.a()

o=C()
o.c() """

################################
""" def a(x):
    def b():
        return x+x
    return b
x=a('x')
y=a('')
print(x() +y()) """

##########################

""" print ("a", "b","c", sep="'") """

###############################

""" def fun(x):
    return 1 if x %2!=0 else 2
print (fun(fun(1))) """

#################################
""" d = {}
d['2'] = [1,2]
d['1'] = [3,4]
for x in d.keys():
    print(d[x][1], end="") """


#####################################

""" class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A, "A")) """

##################################

""" class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x=X()
z=Z()
print (isinstance (x,Z),isinstance(z,X)) """

####################################

""" my_list = [[c for c in range (r)] for r in range (3)]
for element in my_list:
    if len(element) <2:
       print() """

######################################

""" my_string_1 = 'bond'
my_string_2 ='James Bond'

print (my_string_1.isalpha(),my_string_2.isalpha()) """

####################################

""" try:
    raise Exception
except BaseException:
    print("a",end='')
else:
    print("b",end="")
finally:
    print("c") """

######################################

""" print (len([i for i in range(0, -2)])) """

##########################

""" x="""
"""
print(len(x))
 """
######################################

""" class A:
    pass
class B:
    pass
class C(A,B):
    pass
print(issubclass(C,A) and issubclass(C,B)) """

##########################################
""" my_string ='abcdef'

def fun(s):
    del s[2]
    return s
print(fun(my_string)) """

##########################
""" z= 2
y= 1
x= y < z or z > y and y > z or z < y  """
###########################

""" import calendar

c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end="") """

#########################

""" x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z) """
##############################

""" class A:
    def __init__(self,v):
        self.a = v + 1
a = A(0)
print(a._a) """

#############################

""" def fun(n):
    s=''
    for i in range(n):
        s+= '*'
        yield s
for x in fun(3):
    print(x,end='') """

################################

""" v=1+1 // 2+1 /2+2
print(v) """

###############################
""" a = True
b = False
a = a or b
b = a and b
a = a or b
print (a,b) """

##########################

""" x = 16 
while x > 0 :
    print('*',end='')
    x//=2
 """
########################

""" d ={'one': 1, 'three':3, 'two':2}
for k in sorted(d.values()):
    print(k, end='') """

############################

""" print(__name__)

#resposta __main__
 """

################

""" print(len((1,)))

#Resultado é 1 """

""" def fun (d,k,v):
    d[k]=v

my_dictionary = {}
print (fun(my_dictionary, '1','v'))
 """
# resposta é NONE

""" import os
os.makedirs('pictures/thumbnails')
os.rmdir('pictures')

#resposta é erro no codigo """ 

##########################

""" y = input()
x = input()
print (x+y)
# resposta é 21 
 """
############################

""" i = 4
while i > 0 :
    i-=2
    print("*")
    if i ==2:
        break
else:
    print("*")
#Resultado é * """

########################

""" t = (1,)
t=t[0] + t[0]
print(t)
# Resposta é 2 """

############################
""" class A:
    def a (self):
        print('a')
class B:
    def a (self):
        print('b')
class C(A,B):
    def c (self):
        self.a()
o = C()
o.c() """

#Resposta é 'a'

""" def fun (a,b, c=0):
    fun(0)

######################### """

""" from datetime import datetime

datetime = datetime (2019,11,27,11,27,22)
print (datetime.strftime('%Y/%m/%d %H:%M:%S')) """

#Resultados 2019/11/27 11:27:22

############################

""" my_list = [1,2,3,4]
my_list = list(map(lambda x: 2*x, my_list))
print (my_list)

# Resultado é 2 4 6 8 """

###################

class Class:
    def __init__(self):
        pass

########################
""" class A:
    A=1
    def __init__(self, v=2):
        self.v = v+A.A
        A.A += 1
    def set (self,v):
        self.v += v
        A.A += 1
        return
a=A()
a.set(2)
print(a.v)
 """
# Resposta é 5

#################################

""" d={1:0,2:1,3:2,0:1}
x=0
for y in range(len(d)):
    x=d[x]
print(x) """
#Resposta é 0

##############################

""" from datetime import timedelta 
delta = timedelta(weeks =1, days= 7, hours=11 )

print (delta) """
#Resposta 14 days , 11:00:00

##############################

""" t = (1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t) """

# Resposta certa è 3 

####################

""" try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b") """

##Resposta codigo vai gerar um erro


#############################
""" def fun (par2, par1):
    return par2 + par1
print (fun(par2=1, 2))
 """
#Resultado codigo errado

""" class A:
    def __init__(self,name):
        self.name=name

a = A("Class")
print(a) """

#Resposta Uma string a terminar com o codigo hexadecimal
#longo

""" x ="\"
print(len(x))
 """
#Resposta causará um erro 