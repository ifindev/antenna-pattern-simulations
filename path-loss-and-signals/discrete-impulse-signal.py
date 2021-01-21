import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(-5,6,1)])
tick = np.arange(-5,6,1)

# Amplitude of the signal
amp = [] 
for i in range(len(x)):
    if x[i] == 0:
        amp.append(1)
    else:
        amp.append(0)
ampl = np.array(amp) # Amplitude of the signal

plt.scatter(x,ampl)
plt.grid(True)
plt.title("Discrete Impulse Signal: $\delta$[n]")
plt.xlabel("n")
plt.ylabel("$\delta$[n]")
plt.xticks(tick)
plt.show()
