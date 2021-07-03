import numpy as np
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

# Defining activations parameters

def gen_actv(alpha, beta, voltage):
    def actv(x,t):
        a = alpha(voltage)*(1-x) - beta(voltage)*x
        return a
    return actv

# Defining V(t) from current

def gen_volt(n, m, h, i):
    def volt(x,t):
        a = (i-g_K*(n**4)*(x-v_K)-g_Na*(m**3)*h*(x-v_Na)-g_l*(x-v_l))/c
        return a
    return volt

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
i = 10
t0 = 0
t = t0
tf = 10
step_number = 1000

step_size = (tf-t0)/step_number
volt_graph = [(t0, voltage)]

to_graph = []

for step in range(0,step_number):
    interval = (t, t + step_size)
    n_prime = gen_actv(alpha_n, beta_n, voltage)
    m_prime = gen_actv(alpha_m, beta_m, voltage)
    h_prime = gen_actv(alpha_h, beta_h, voltage)

    n = runge_kutta(n_prime, n0, 1, interval)[-1]
    m = runge_kutta(m_prime, m0, 1, interval)[-1]
    h = runge_kutta(h_prime, h0, 1, interval)[-1]

    to_graph.append(n)
    n0, m0, h0 = n[1], m[1], h[1]

    volt_prime = gen_volt(n[1], m[1], h[1], i)
    volt = runge_kutta(volt_prime, voltage, 1, interval)[-1]
    # print(volt)
    volt_graph.append(volt)

    voltage = volt[1]
    t = t + step_size

plt.plot(*zip(*volt_graph))
# plt.plot(*zip(*to_graph))
plt.show()
