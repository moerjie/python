from rand import Randomwalk
import matplotlib.pyplot as plt

rf = Randomwalk(5000)
rf.fill_walk()
point_num = list(range(rf.num_points))

plt.plot(rf.x_values, rf.y_values, lw=1)
plt.show()
