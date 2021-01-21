# Muhammad Arifin 
# 3GPP 3 - sector antenna Pattern 
# 15102019 - Teknik Fisika UGM

from pylab import *

tita = np.arange(-180,180,0.1) # linear space of theta in radian 
tita_3dB = 70 #degree
A_m = 20 #dB

A_tita = -12*(tita/tita_3dB)**2
for i in range(len(A_tita)):
    if A_tita[i] < -A_m:
        A_tita[i] = -20

# Plot the array factor
plot(tita,A_tita)
title('3GPP - Three Sector Antenna Pattern')
xlabel('$\Theta$ (degree)')
ylabel('Gain(dB)')
xticks(np.arange(-120,122,60))
yticks(np.arange(-25,0.1,5))
xlim([-120,120])
ylim([-25,1.1])
#legend()
show()
