# Muhammad Arifin 
# Simulation Array Factor of ULA plotted in Polar Plot
# 10102019 - Teknik Fisika UGM

from pylab import *
# grafik polar untuk d = 0.5 lambda
theta = np.arange(0,pi,0.01) # Kalau mau setengah saja, gunakan (0,pi,0.01)
beta = 0
la = 0.005 # f = 60 Ghz = 60 * 10^9 -> lambda = 5mm = 0.005 m
N = 10
N2 = N/2
k = 2*pi/la

d = 2*la # d = 0.5 lambda

psi = k*d*cos(theta) + beta

AF = (sin(N2*psi))/(sin(psi/2))

# Normalize AF to the maximum value
AFn = abs(AF/max(abs(AF)))

# Plot grafik
axes(polar = True)
title("2$\lambda$")
plot(theta, AFn)
show()
