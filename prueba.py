import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y = np.sin(x)

plt.figure()
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print("Finished")