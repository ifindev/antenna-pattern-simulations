# Description: 
#				Python Code for simulating array factor of Uniform Linar Array (ULA) Antenna 
#				for 5G communications with 60 GHz working frequency. .
#				In this program, I simulated ULA with 1.5 lambda eparation distances between 
#				antenna array elements.
# Author: Muhammad Arifin
# Institution: Engineering Physics, Universitas Gadjah Mada

from pylab import *

theta = np.arange(0,180,0.01)
beta = 0
la = 0.005 # f = 60 Ghz = 60 * 10^9 -> lambda = 5mm = 0.005 m
N = 10
N2 = N/2
k = 2*pi/la

d = 0.5*la # d = 1.5 lambda

psi = k*d*cos(theta*pi/180)

AF = 1/N * (sin(N2*psi))/(sin(psi/2))

# Normalize AF to the maximum value
AFn = abs(AF/max(abs(AF)))

# Plot rectangular graph of the array factor's magnitude
plot(theta,AFn)
xlabel('$\Theta$ (degree)')
ylabel('Array Factor')
title('$d = \lambda/2$')
xticks(np.arange(0,182,60))
yticks(np.arange(0,1.1,0.2))
xlim([0,180])
ylim([0,1.01])
show()


