# (C) Muhammad Arifin - Engineering Physics 2015, Universitas Gadjah Mada

import math
from pylab import *
#Varable Declaration

# Isotropic Source pattern
cr =linspace(1,1,73)
psi =arange(0,361,5)
theta=psi*math.pi/180

# ~~~~~~~ lambda/2 dipole pattern ~~~~~~~
x  = np.arange(0, (2*np.pi), 0.0001)
si = 1.67*((np.cos(np.pi/2*np.cos(x)))/(np.sin(x)))**2

# ~~~~~~~ l<<lambda pattern ~~~~~~~
y  = np.arange(0, (2*np.pi), 0.0001)
siy = 1.5*(np.sin(y))**2


# Result
polar(theta,cr)
polar(x,si)
polar(y,siy)
legend(('Isotropic',r'$\lambda$/2',r'$l \ll \lambda$'),loc='upper right')
show()
