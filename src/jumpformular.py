import numpy as np
import matplotlib.pyplot as plt


def y(t, v0=1, y0=0, scale=10000, g = -9.807):
    h=(y0 + v0*t + g*t**2/2)*scale
    return h

t = np.linspace(0, 100, 10) # 0~100 millisecond
h = y(t/1000, 0.49)

plt.plot(t, h)
plt.show()