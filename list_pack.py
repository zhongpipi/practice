def pack1(a, b, *c, **d):
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)
    print(type(d), d)


score = [1.0, 2.0, 3.0, 4.0, 5.1, 6.7]
pack1(*score)

def pack(*c):
    print(type(c), c)


student = {'score': 1.0, 'id': 2, 'name': 'xiaoxiao'}
pack(*student)

def func(a,b,c):
    print(a,b,c)

func(*[1,2,3])
func(*(1,2,3))
func(*"abc")
func(*{'a':1,'b':2,'c':3})
func(**{'a':1,'b':2,'c':3})