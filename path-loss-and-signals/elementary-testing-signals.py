""" Generate Unit Step, Unit Ramp, Unit Impulse, and Rectangular Pulse"""
""" for Continuous Signals"""
""" Reference from https://www.youtube.com/watch?v=NyoA5O-4ikk"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4,4.1,0.0001) # Coba variasikan time - step. Lihat akibatnya
u_t = (np.sign(x) + 1)/2 # Continuous unit step signal
r_t = (x * (np.sign(x) + 1)/2 - x*(np.sign(x - 1) + 1)/2) # Continuous unit ramp signal
d_t = (np.sign(x)+1)/2 - (np.sign(x - 0.0001) + 1)/2 # Continuous unit impulse signal
rp_t = ((np.sign(x) + 1)/2 - (np.sign(x - 2) + 1)/2)

#fig, axs = plt.subplots(2,2, figsize=(10,6), sharex='col', sharey='row')
fig, axs = plt.subplots(2,2, figsize=(10,6))
fig.subplots_adjust(hspace=0.4, wspace=0.3)


axs[0, 0].plot(x,u_t, c = 'black')
axs[0, 0].set(xlabel='$t$', ylabel='$u(t)$',title = 'CT Unit Step Signal')

axs[0, 1].plot(x,r_t, c = 'black')
axs[0, 1].set(xlabel='$t$', ylabel='$r(t)$',title = 'CT Unit Ramp Signal')

axs[1, 0].plot(x,d_t, c = 'black')
axs[1, 0].set(xlabel='$t$', ylabel='$\delta(t)$',title = 'CT Unit Impulse Signal')

axs[1, 1].plot(x,rp_t, c = 'black')
axs[1,1 ].set(xlabel='$t$', ylabel='$rp(t)$',title = 'CT Rectangular Pulse Signal')


plt.show()
