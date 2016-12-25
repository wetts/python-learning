#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 读文件
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理
try:
    f = open('/path/to/file', 'r', encoding='gbk', errors='ignore')
    print(f.read())
finally:
    if f:
        f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。

另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
'''

# 读取二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('/Users/michael/test.jpg', 'rb') as f:
    f.read()

############################
# 写文件
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('/Users/michael/test.txt', 'w', encoding='gbk') as f:
    f.write('Hello, world!')
