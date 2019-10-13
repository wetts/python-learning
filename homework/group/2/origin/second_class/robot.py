import typing
from typing import Union

my_type = Union[int, str, float]


class robot():
    la = 100

    def __init__(self, name, height, weight):
        self._name = name
        self._height = height
        self._weight = weight
        self._power = 100

    # ->输出类型
    # :输入类型
    @property
    def name(self) -> my_type:
        return self._name

    @name.setter
    def name(self, value: my_type):
        assert isinstance(value, str)
        self._name = value

    def introduction(self):
        print('My name is', self._name)

    @property
    def power(self):
        return self._power

    def charge(self):
        self._power += 10

    def work(self):
        pass

    @classmethod
    def get_height(cls):
        return cls.name

    @staticmethod
    def ord():
        print('ord')
        pass


class talk_robot(robot):
    def __init__(self, name, height, weight):
        # self._name = name
        # self._height = height
        # self._weight = weight
        # self._power = 100
        super().__init__(name, height, weight)
        super().introduction()
        print('I am a talk robot')

    def work(self):
        print('I am talking')

    def talk(self):
        print('hhh')


class wash_robot(robot):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)
        print('I am a wash robot')
        # super().introduction()

    def work(self):
        print('I am washing...')

    def wash(self):
        print('washing...')


class talk_wash_robot(talk_robot, wash_robot):
    def __init__(self, name, height, weight):
        talk_robot.__init__(self,name, height, weight)



if __name__ == '__main__':
    # robot1 = robot('x1', 100, 200)
    #
    # print(robot1.power)
    #
    # robot1.name = 'lsx'
    # print(robot1.name)
    # # robot1.name=1212
    # # print(robot1.name)
    # print(robot.la)
    # print(robot1.get_height())
    # robot1.introduction()
    # robot.ord()
    #
    # robot2 = talk_robot('ss', 150, 200)
    # # robot2.introduction()
    # print(robot2.power)

    robot3 = talk_wash_robot('wash_talk', 200, 120)
    robot3.talk()
    robot3.wash()


