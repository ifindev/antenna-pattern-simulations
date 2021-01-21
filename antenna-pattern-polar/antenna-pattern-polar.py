# (C) Muhammad Arifin - Engineering Physics 2015, Universitas Gadjah Mada

import math
from pylab import *
#Variable Declaration

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

# ~~~~~~Array Pattern~~~~~~~

N=5   #Number of elements of dipole
s=0.25 #Space between dipole elements(wavelengths)
phi0=90*math.pi/180 #Angle between array factor and array(radians)

#Calculation

alpha=-2*math.pi*s*math.cos(phi0)  #Current phase(radians)
phi=arange(-180,185,5)
Si=linspace(0,0,73)
for k in range(0,73):
    Si[k]=alpha+2*math.pi*s*math.cos(phi[k]*math.pi/180)

AFR=linspace(0,0,73)
AFI=linspace(0,0,73)

for i in range(0,73):
  for j in range(0,N):
     AFR[i]=AFR[i]+math.cos(j*Si[i])  #Real part of Array factor
     AFI[i]=AFI[i]+math.sin(j*Si[i])#Imaginary part of Array factor

teta=phi*math.pi/180
AF=linspace(0,0,73)
for k in range(0,73):
   AF[k]=AF[k]+(AFR[k]**2+AFI[k]**2)**0.5

# Result
polar(theta,cr)
polar(x,si)
polar(y,siy)
polar(teta,AF)
legend(('Isotropic',r'$\lambda$/2',r'$l \ll \lambda$','Array N = 5'),loc='upper right')
show()
