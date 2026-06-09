# this is casic basic calculator ,addl,sub,add,multiplication

def addl(a):
    c = 0
    for i in a:
        c = c +i
    return c
def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def multi(a,b):
    c = a*b
    return c
def adde(a,b,c):
    c = a+b+c
    return c

a = [1,2,3,4]
h = addl(a)
p = add(9,5)
c = sub(7,5)
f = multi(6,5)
d = adde(3,4,5)
print(h)
print(p)
print(f)
print(c)
print(d)
