'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-30 21:30:36
FilePath: \python\data_show\rw_visual.py
'''
import matplotlib.pyplot as plt
from rand import Randomwalk


while True:
    rw = Randomwalk()
    rw.fill_walk()

    point_num = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_num,
                cmap=plt.cm.Blues, edgecolors='none', s=10)
    plt.scatter(0, 0, c='red', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.show()

    keep_running = input("Make another walk?(1/2): ")
    if keep_running == '1':
        break
