def fib(max):
    '''
    1 1 2 3 5 8
    :param max:
    :return:
    '''
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n += 1
        print(b)
    return 'done'


# fib(6)

def generator_fib(max):
    '''
        1 1 2 3 5 8
        :param max:
        :return:
        '''
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a + b
        n += 1
        # print(b)

    print('done')

# print(generator_fib(6))
# next(generator_fib(6))
g=generator_fib(6)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

li=[i for i in range(10)]
def odd(n):
    if n %2==0:
        return True
    else:
        return False

print(list(filter(odd,li)))

def sqrt(n):
    return n**0.5

print(list(map(sqrt,li)))

def func(*args,**kwargs):
    print(type(args))
    print(kwargs)
    pass

doc={''}
func(li,doc)

print(list(map(lambda x:x**0.5,li)))
print(list(filter(lambda x:True if x%2==0 else False,li)))
