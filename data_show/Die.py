'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-31 18:22:13
FilePath: \data_show\Die.py
'''
from random import randint


class Die():
    def __init__(self, num_sides=8):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

    def creat_x(self):
        x_label = []
        i = j = 1
        for i in range(1, self.num_sides+1):
            for j in range(1, self.num_sides+1):
                x_label.append(i+j)
                j += 1
            i += 1
        return x_label
