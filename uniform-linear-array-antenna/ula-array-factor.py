# Description: 
#				Python Code for simulating array factor of Uniform Linar Array (ULA) Antenna 
#				for 5G communications.
#				In this program, I simulated ULA with four different separation distances between 
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
d1 = 0.25*la # d = 1/4 lambda
d2 = 0.5*la # d = 1/2 lambda
d3 = la # d = lambda
d4 = 1.5*la # d = 1.5 lambda

psi1 = k*d1*cos(theta*pi/180)
psi2 = k*d2*cos(theta*pi/180)
psi3 = k*d3*cos(theta*pi/180)
psi4 = k*d4*cos(theta*pi/180)

AF1 = 1/N * (sin(N2*psi1))/(sin(psi1/2))
AF2 = 1/N * (sin(N2*psi2))/(sin(psi2/2))
AF3 = 1/N * (sin(N2*psi3))/(sin(psi3/2))
AF4 = 1/N * (sin(N2*psi4))/(sin(psi4/2))


# Normalize and Convert to dB the Magnitude of Array Factor
dB1 = 20*np.log10(abs(AF1/max(AF1)))
dB2 = 20*np.log10(abs(AF2/max(AF2)))
dB3 = 20*np.log10(abs(AF3/max(AF3)))
dB4 = 20*np.log10(abs(AF4/max(AF4)))

# Plot rectangular graph of the array factor's magnitude
subplot(4,2,1)
plot(theta,dB1,label='$d = \lambda/4$')
ylabel('AF (dB)')
ylim([-25,0.5])
xlim([0,180])
xticks(np.arange(0,181,60))
legend()

subplot(4,2,2)
plot(theta,dB2,label='$d = \lambda/2$')
ylabel('AF (dB)')
ylim([-25,0.5])
xlim([0,180])
xticks(np.arange(0,181,60))
legend()

subplot(4,2,3)
plot(theta,dB3,label='$d = \lambda$')
ylabel('AF (dB)')
ylim([-25,0.5])
xlim([0,180])
xticks(np.arange(0,181,60))
legend()

subplot(4,2,4)
plot(theta,dB4,label='$d = 1.5\lambda$')
ylabel('AF (dB)')
ylim([-25,0.5])
xlim([0,180])
xticks(np.arange(0,181,60))
legend()



show()
