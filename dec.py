from time import  time




def timer(function):
    def f(*args,**kwargs):
        before = time()
        rv = function(*args,**kwargs)
        after = time()
        print('Ellapsed: ', after - before)
        return rv
        
    return f

@timer
def add(x,y=10):
    return x+y

@timer
def sub(x, y=10):
    return x-y


print('add(10)', add(5,6))
print('sub(10)', sub(5,6))

