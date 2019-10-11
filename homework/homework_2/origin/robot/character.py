
li=[i for i in range(10)]
print(li)
print(li[1])
print(li[-1])
print(li[3:5])
print(li[1:6:2])
string='sd'
long_str='''adsa
asd
'''
print(string[1])
print(len(string))
print(len(long_str))

for i in range(10):
    print(i)

from collections import Iterable
print(isinstance(li,Iterable))
print(isinstance(string,Iterable))

print(long_str)
for i in long_str:
    print(i)

assert isinstance(long_str,str)
def hh(ia:int):
    assert isinstance(ia,int)

