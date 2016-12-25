'''
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
'''
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

# StringIO
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
f.close()

###
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

###
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
f.seek(0)
print(f.readline())
f.close()

###
# write会覆盖构造函数赋值
f = StringIO("1\n2\n3")
f.write("4\n 5\n 6")
f.seek(0)
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())

#################################
# BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(f.read())
f.seek(0)
print(f.read())
