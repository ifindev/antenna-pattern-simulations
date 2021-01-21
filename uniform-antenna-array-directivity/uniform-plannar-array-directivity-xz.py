"""Simulasi UPA xz"""
"""Muhammad Arifin"""
"""Teknik Fisika UGM"""

from pylab import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


j= 0 + 1j
M=361 #angle resolution
la = 3e8/60e9
k=2*pi/la #wavenumber 2*pi/lamda
theta=linspace(0,pi,M) #generates M points between 0 and pi.
phi=linspace(0,2*pi,M)
THETA,PHI=meshgrid(theta,phi)
#     Cartesian grid in 2-D/3-D space
#     [THETA,PHI] = meshgrid(theta,phi) replicates the grid vectors theta and phi to 
#     produce the coordinates of a rectangular grid (THETA,PHI). The grid vector
#     theta is replicated numel(phi) times to form the columns of THETA. The grid 
#     vector phi is replicated numel(theta) times to form the rows of PHI.

dtheta=pi/M
dphi=pi/M

#Planar Array Variables
Mx=10
Nz=10
dy=1.5*la
dz=1.5*la #distance between array element follow wavelength
deltax=0
deltaz=0 #progress phase shifts

#Array Factor Calculation
psix=(k*dy*sin(THETA)*cos(PHI))+deltax
psiz=(k*dz*cos(THETA))+ deltaz
AFx=0
AFz=0

for m in range(1,Mx + 1):
    AFx=AFx + exp(j*(m-1)*psix)

for n in range(1,Nz + 1):
    AFz=AFz + exp(j*(n-1)*psiz)

AF=AFx*AFz
AFmag=abs(AF)


#Directivity Calculation
Utheta=AFmag**2
Prad = sum(sum(Utheta*sin(THETA)*dtheta*dphi))
D = 4*pi*Utheta/Prad  #pp.310 Antenna Theory Balanis 3rd Edition
DdB=10*log10(D)

DdB[DdB < -20 ] = -20 # Untuk keperluan grafik saja

#3D Directivity plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim3d(-20,30,20)
ax.set_xlabel("$\Theta$(deg)")
ax.set_ylabel("$\phi$(deg)")
ax.set_zlabel("D (dB)")
#ax.set_title('Directivity ULA (d = 0.5$\lambda$)',size=10)
surf = ax.plot_surface(degrees(THETA), degrees(PHI),DdB,cmap='viridis',linewidth=0, antialiased=False,)

# 2D Contour Plot
fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 

a = amax(DdB)

levels = [i for i in range(-20,30,5)]
cp = plt.contourf(degrees(THETA), degrees(PHI),DdB,levels)
plt.colorbar(cp,label="Directivity (dB)")

ax.set_title('Directivity UPA-xz (d = 1.5$\lambda$)',size=20)
ax.set_xlabel('$\Theta$ (degree)')
ax.set_ylabel('$\phi$ (degree)')
legend(["$D_0$ = %.3f dB" %a])
plt.show()
