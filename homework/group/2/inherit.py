# -*- coding: utf-8 -*-


class animal():

    __code = 0

    def __init__(self, name):
        self._name = name

    def eat(self):
        pass

    def run(self):
        pass

    @classmethod
    def add_code(cls):
        cls.__code += 1

    @classmethod
    def print_code(cls):
        print(cls.__code)

    @staticmethod
    def static_method():
        print('this is static method')


class bird():
    def fly(self):
        pass


class dog(animal):
    def eat(self):
        print('dog eat')


class cat(animal):
    def eat(self):
        print('cat eat')


class owl(animal, bird):
    def eat(self):
        print('owl eat')

    def fly(self):
        print('owl fly')


if __name__ == '__main__':
    animal.print_code()
    animal.add_code()
    animal.print_code()
    animal.static_method()
    cat = cat('c1')
    owl = owl('o1')
    cat.eat()
    owl.fly()
