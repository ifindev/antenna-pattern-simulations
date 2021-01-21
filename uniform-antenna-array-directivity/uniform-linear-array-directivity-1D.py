from pylab import *

j = 0 + 1j # imaginary number
N = 10 # Number of array elements
M = 361
theta = np.arange(0,180,0.001) # linear space of theta in radian. dtheta = 0.5 degree
beta = 0 # Phase angle beta
la = 0.005 # f = 60 Ghz = 60 * 10^9 -> lambda = 5mm = 0.005 m
k = 2*pi/la # wave number
d = 0.5*la # separation distance of the element
psi = k*d*cos(radians(theta)) # total phase angle psi. Convert it from radian to degree
dtheta=pi/M
dphi=pi/M

# Array Factor Calculation
AF = 0 + 0j
for m in range(1,N+1):
    AF = AF + np.exp(j*(m-1)*psi)
    
AFmag = abs(AF)
AFdB = 10*np.log(AFmag)

# 2D Array Factor Plot
plot(theta,AFdB,c = 'black')
xticks(np.arange(0,182,60),size = 15)
yticks(np.arange(-25,25,5),size = 15)
xlim([0,180])
ylim([-20,25])
xlabel('$\Theta$ (degree)',size = 15)
ylabel('Directivity (dB)',size = 15)
title("d = 0.5$\lambda$",size = 25)
show()
