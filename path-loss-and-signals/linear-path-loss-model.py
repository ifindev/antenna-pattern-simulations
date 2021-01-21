""" Linear Path Loss Model """
""" Received Power Pr ~ k/d and Pr ~ 1/d**2 """
""" Improved Analysis from Andrea Goldsmith's Wireless Communications pp.28"""
""" Muhammad Arifin (Effendi) """
""" 22 October 2019 """

from pylab import*
import numpy as np
import matplotlib.pyplot as plt
    
def Prd(d):
    """ Model received power to be"""
    """ inversely proportional with distance d between the TX and RX"""
    """ d is a linearspace of distance from 10e-5 to the maximum value of d"""
    """ minimum d is 10e-5 to zero division operation """
    k = 1 # Arbitrary constant k
    P_rx = k/d # received power

    return P_rx

def Prd_sqr(d):
    """ Model received power to be"""
    """ inversely proportional with square distance d between the TX and RX"""
    """ d is a linearspace of distance from 10e-5 to the maximum value of d"""
    """ minimum d is 10e-5 to zero division operation """
    k = 1 # Arbitrary constant k
    P_rx_sqr = k/(d**2) # received power

    return P_rx_sqr

""" ITU - R Path loss model  from Yunyi Yao Slide"""
""" L = 10Nlog10(d) + X_sigma """
""" L: Excess Path Loss; N: Path loss exponent """
""" d: Distance between TX and RX; X_sigma: Shadowing fading """

def ITU_R(d):
    """ N = 3.1; sigma = 12 (Ignored first. Still not understand about it) """
    L_ITU = 10*3.1*np.log10(d)
    return L_ITU

def tgpp_L(d):
    """ 3GPP Path Loss Model """
    L_3gpp = 10*1.73*np.log10(d) 
    return L_3gpp

""" Main Program Begin """

# Distance, transmitted power and received power
d = np.linspace(0,100,200)
P_TX = 1 #P_tx is a single value of transmitted power in Watt
#P_RX1 = Prd(d)
#P_RX2 = Prd_sqr(d)

PL_ITU = ITU_R(d)
PL_3gpp = tgpp_L(d)

# Path Loss calculation
#PL1 = P_TX/P_RX1
#PL2 = P_TX/P_RX2

#PL1_dB = 10*np.log10(PL1)
#PL2_dB = 10*np.log10(PL2)

# Plot the Path Loss over distance
#plot(d,PL1,label = "$P_{r} = k/d$")
#plot(d,PL2,label = "$P_{r} = k/d^{2}$",c='orange')
plot(np.log(d),PL_ITU,label = "ITU-R",c='red')
plot(np.log(d),PL_3gpp,label = "3GPP",c='green')

# x - and y - axes limit
xlabel('$d$ (m)')
ylabel('$Path Loss$ ($P_{TX}/P_{RX}$)')
title("Linear Path Loss Model")
xticks(np.arange(0,2.01,0.5))
yticks(np.arange(0,70,10))
xlim([0,2])
#ylim([0,1.01])
legend()
show()
