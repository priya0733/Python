import matplotlib.pyplot as plt
import numpy as np

xpoint = ([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
ypoint = ([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(xpoint,ypoint)
plt.title("sport watch data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()