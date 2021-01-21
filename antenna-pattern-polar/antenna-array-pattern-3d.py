# (C) Muhammad Arifin - Engineering Physics 2015, Universitas Gadjah Mada

from pylab import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


j= 0 + 1j
M=1000 #angle resolution
k=2*pi #wavenumber 2*pi/lamda
theta=linspace(0,pi,M) #generates M points between 0 and pi.
phi=linspace(-pi/2,pi/2,M)
[THETA,PHI]=meshgrid(theta,phi);
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
dy=1
dz=1 #distance between array element follow wavelength
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

#3D Directivity plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(30, -30)
surf = ax.plot_surface(degrees(THETA), degrees(PHI), D,cmap='viridis',linewidth=0, antialiased=False)

show()
