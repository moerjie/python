'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-09-03 19:56:06
FilePath: \python\sympy.py
'''
from sympy import *
from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [x**2 for x in x]
plt.scatter(x, y)

plt.show()
