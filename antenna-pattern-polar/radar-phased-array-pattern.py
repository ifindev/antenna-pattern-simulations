# (C) Muhammad Arifin - Engineering Physics 2015, Universitas Gadjah Mada

from pylab import *

# mainkan sudut fasa sinyal eksitasinya untuk 
theta = np.arange(0,pi,0.01)
la = 0.005 # f = 60 Ghz = 60 * 10^9 -> lambda = 5mm = 0.005 m
N = 10
N2 = N/2
k = 2*pi/la
d = 0.5*la # d = 1.5 lambda

# mainkan beta
beta = [-5*pi/6,-pi/2,-pi/6,0,pi/6,pi/2,5*pi/6,pi]
# Sudut fasa
psi =[]
AF = []
AFn = []
for i in range(len(beta)):
    psi.append(k*d*cos(theta) + beta[i])
    AF.append(1/N * (sin(N2*psi[i]))/(sin(psi[i]/2)))
    AFn.append(abs(AF[i]/max(abs(AF[i])))) # Normalize AF to the maximum value

# Plot grafik
axes(polar = True)
title(r'$\beta = 180{\circ}$')
plot(theta, AFn[0])
plot(theta, AFn[1])
plot(theta, AFn[2])
plot(theta, AFn[3])
plot(theta, AFn[4])
plot(theta, AFn[5])
plot(theta, AFn[6])
plot(theta, AFn[7])
show()
