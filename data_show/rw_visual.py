'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-30 20:45:16
FilePath: \python\data_show\rw_visual.py
'''
import matplotlib.pyplot as plt
from rand import Randomwalk

rw=Randomwalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
