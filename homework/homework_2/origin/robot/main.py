import time


class robot(object):
    def __init__(self, height, weight, name):
        print('i robot')
        self._height = height
        self._weight = weight
        self.name = name
        self._state = False
        self._power = 100

    def introduction(self):
        print('I am', self.name)

    @property
    def power(self):
        return self._power

    def power_down(self):
        self._power -= 10

    @property
    def get_height(self):
        print('my height is', self._height)
        return self._height

    def get_weight(self):
        print('my weight is', self._weight)
        return self._weight

    def get_power(self):
        print('My power is', self._power)

    # @property
    # def name(self):
    #     return self._weight
    #
    # @name.setter
    # def name(self, weight):
    #     assert isinstance(weight, str)

    def work(self):
        pass

    def relax(self):
        pass

    def charge(self):
        print('i am charge')
        time.sleep(5)
        self._power += 10
        print('I have power 10')


class talk_robot(robot):
    def __init__(self, height, weight, name):
        # self._height = height
        # self._weight = weight
        # self._power = 100

        # super(robot,self).__init__()
        robot.__init__(self, height, weight, name)
        super().introduction()
        print('i am talk robot')

    def work(self):
        if self._power < 10:
            print('I have no power')
        if not self._state:
            self._state = True
            print('What are you talking about?')
            # while True:
            #     self.answer()
        else:
            print('I am busy now')

    def relax(self):
        self._state = False
        print('I am relax')

    def answer(self):
        print('lalala')
        self.power_down()


class wash_robot(robot):
    def __init__(self, height, weight, name):
        robot.__init__(self, height, weight, name)
        print('i am wash robot')

    def work(self):
        if self._state:
            self._state = True
            print('I am washing')

    def relax(self):
        self._state = False
        print('I am relaxing')

    def wash(self):
        print('wash...')
        self.power_down()


class wash_talk_robot(wash_robot, talk_robot):
    def __init__(self, height, weight, name):
        super(wash_robot, self).__init__(height, weight, name)


if __name__ == '__main__':
    # robot1 = robot(100, 200, 'x1')
    # print(robot1.get_height)
    # robot1.get_weight()
    # robot1.get_power()
    # robot1.name = 12
    #
    # robot2 = talk_robot(150, 210, 'x2')
    # robot2.get_weight()
    # print(robot2.get_height)
    #
    # robot2.get_power()
    # robot2.work()

    robot3 = wash_talk_robot(100, 100, 'll')
    print(robot3.get_height)
    robot3.answer()
    robot3.wash()
