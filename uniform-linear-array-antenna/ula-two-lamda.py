# Muhammad Arifin 
# Simulation Array Factor of ULA
# 10102019 - Teknik Fisika UGM

# Declaration of Variables
# There six parameters need to be declare for the array factor simulation. 
# These six are, the number elements of the array (N), wavelength (lambda), element separation (d)
# Theta from 0 to pi, phase angle beta, and phase angle psi

from pylab import *


N = 10 # Number of array elements
N2 = N/2 # Number of array elements divided by two
theta = np.arange(0,180,0.001) # linear space of theta in radian 
beta = 0 # Phase angle beta
la = 0.005 # f = 60 Ghz = 60 * 10^9 -> lambda = 5mm = 0.005 m
k = 2*pi/la # wave number
d = 2.000001*la # separation distance of the element
psi = k*d*cos(theta*pi/180) # total phase angle psi. Convert it from radian to degree

# Calculating Array Factor
AF = 0
AF1 =(sin(N2*psi))/(sin(psi/2))


# Normalize AF to the maximum value
AF1n = abs(AF1)/max(abs(AF1))

# Plot the array factor
plot(theta,AF1n)
#plot(theta,AF2n,label='phase vector = n')
xlabel('$\Theta$ (degree)')
ylabel('Array Factor (dB)')
title("d = 2$\lambda$")
xticks(np.arange(0,182,60))
yticks(np.arange(0,1.1,0.2))
xlim([0,180])
ylim([0,1.01])
#legend()
show()
