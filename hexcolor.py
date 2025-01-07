import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker = '<',ms = 20,mec = "#ACAF50",mfc = "#ACAF50",linestyle = "dotted")
plt.show()