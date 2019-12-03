from collections import namedtuple
import random
import math


def menu():
    print('-' * 30)
    print('欢迎来到猜数游戏')
    print('1.开始游戏')
    print('2.结束游戏')
    print('-' * 30)


class GuessNum:
    random_choice = [i * 100 for i in range(1, 20)]

    def __init__(self):
        self.guess_range = None
        self.guess_num = None
        self.left = None
        self.right = None
        self.random_num()

    def init_range(self):
        self.left = 1
        self.right = self.guess_range

    @property
    def _random_range(self):
        return random.choice(self.random_choice)

    def random_num(self):
        self.guess_range = self._random_range
        self.guess_num = random.randint(1, self.guess_range)
        self.init_range()

    def user_choice(self, choice):
        if choice == '1':
            print('数值的范围是：{}-{}'.format(self.left, self.right))
            user_num = input('请输入你猜测的数值：')
            flag = self.guess(user_num)
            return flag

        elif choice == '2':
            exit()

    def guess(self, num):
        flag = 0
        num = math.floor(float(num))
        if self.guess_num == num:
            print('恭喜你猜中了：{}'.format(self.guess_num))
            flag = 1
        elif self.guess_num > num:
            if num > self.left:
                self.left = num
            print('猜小了')
        elif self.guess_num < num:
            if num < self.right:
                self.right = num
            print('猜大了')
        return flag


def main():
    menu()
    game = GuessNum()
    choice = input('请输入你的选择：')
    while True:
        flag = game.user_choice(choice)
        if flag:
            main()


if __name__ == '__main__':
    main()