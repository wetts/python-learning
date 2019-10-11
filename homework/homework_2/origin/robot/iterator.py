import typing
li = [i for i in range(10)]
dic = {'a': 1, 'b': 1}
tup = (i for i in range(10))

# print(isinstance(list,list))
print(li)
# print(tup)

for i in tup:
    print(i)

li_it = iter(li)
print(li_it)
for i in li_it:
    print(i)

li_gen = (i for i in range(10))
print(li_gen)

for i in li_gen:
    print(i)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(10)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
