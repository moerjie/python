'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-31 22:26:09
FilePath: \data_show\cube.py
'''
import matplotlib.pyplot as plt

x_val = [1, 2, 3, 4, 5]
y_val = [x ** 3 for x in x_val]

x_val_pro = list(range(1, 1001))

y_val_pro = [x_p ** 3 for x_p in x_val_pro]
plt.figure(figsize=(9, 6))
plt.subplot(121)
plt.plot(x_val, y_val, 'b--')
plt.tick_params(tickdir='in')
plt.title('1~5')

plt.subplot(122)
plt.scatter(x_val_pro, y_val_pro, c=y_val_pro, cmap=plt.cm.Blues)
plt.show()