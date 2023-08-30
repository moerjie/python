"""
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-30 17:05:41
FilePath: \python\math.py
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


t = np.arange(0, 5, 0.1)
squ = [1, 4, 9, 16, 25]
val = [1, 2, 3, 4, 5]
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
x_val = list(range(1, 1001))
y_val = [x**2 for x in x_val]
plt.scatter(x_val, y_val,  c=y_val, cmap=plt.cm.Blues,edgecolors='none', s=40)
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(tickdir='in')
'''
plt.plot(squ, 'ro', lw=5)
plt.axes([0, 6, 0, 25])
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squ of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=12)

# plt.plot(t, t ** 2, 'b--', t, t, 'r^')

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.plot(names, values, 'b--')
plt.subplot(133)
plt.scatter(names, values)
plt.suptitle('group')
'''
plt.show()
