import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1,linestyle = "dashed",color = "pink",linewidth = 10)
plt.plot(y2,linestyle = "dotted",color = "blue")


plt.show()

