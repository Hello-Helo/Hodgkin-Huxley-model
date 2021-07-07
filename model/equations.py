import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
from ode_solutions import runge_kutta, euler

# Defining parameters Alpha and Beta

def alpha_n(voltage):
    a = (0.01*(55+voltage))/(1-np.exp(-(55+voltage)/10))
    return a

def alpha_m(voltage):
    a = (0.1*(40+voltage))/(1-np.exp(-(40+voltage)/10))
    return a

def alpha_h(voltage):
    a = 0.07*np.exp(-(voltage+65)/20)
    return a

def beta_n(voltage):
    b = 0.125*np.exp(-(voltage+65)/80)
    return b

def beta_m(voltage):
    b = 4*np.exp(-(voltage+65)/18)
    return b

def beta_h(voltage):
    b = 1/(np.exp(-(35+voltage)/10)+1)
    return b

def gen_dalldt(i):
    def dalldt(t,x):
        voltage,n,m,h = x
        dvdt = (i-g_K*(n**4)*(voltage-v_K)-g_Na*(m**3)*h*(voltage-v_Na)-g_l*(voltage-v_l))/c
        dndt = alpha_n(voltage)*(1-n) - beta_n(voltage)*n
        dmdt = alpha_m(voltage)*(1-m) - beta_m(voltage)*m
        dhdt = alpha_h(voltage)*(1-h) - beta_h(voltage)*h

        return dvdt, dndt, dmdt, dhdt
    return dalldt

# Main ####

# Max conductance (m / cm^2)
g_K = 36
g_Na = 120
g_l = 0.3

# Channel voltages (mV)
v_K = -77
v_Na = 50
v_l = -54.387

# Capacitance of the manbrane (mF / cm^2)
c = 1.

# Initial value
m0 = 0.05
n0 = 0.32
h0 = 0.6

# NEED:
# find n, m, h
# find voltage

voltage = -65
i = 6
t0 = 0
t = t0
tf = 10

# Time interval
t= (0,450)

result = runge_kutta(gen_dalldt(i), np.array([voltage, n0, m0, h0]), 100000, t)

# The results in np.array form
time = result[:,0]
voltage_result = result[:,1]
n_result = result[:,2]
m_result = result[:,3]
p_result = result[:,4]

# Plotting
plt.plot(time, voltage_result)
plt.show()
