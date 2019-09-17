# -*- coding: utf-8 -*-


class Iterable_test(object):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Iterator_test(self.data)

class Iterator_test(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __next__(self):
        if self.index <= 0 :
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class NotIterable(object):
    def __init__(self, baselist):
        self._baselist = baselist

    def __getitem__(self, index):
        return self._baselist[index]


iterator_winter = Iterable_test('abcde')
for item in iterator_winter:
    print(item)
print(''.center(50, '-'))
t = NotIterable([1, 2, 3])
for i in t:
    print(i)
