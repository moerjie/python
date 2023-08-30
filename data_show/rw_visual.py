'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-30 20:50:28
FilePath: \python\data_show\rw_visual.py
'''
import matplotlib.pyplot as plt
from rand import Randomwalk

while True:
    rw=Randomwalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()

    keep_running=input("Make another walk?(y/n): ")
    if keep_running =='n':
        break