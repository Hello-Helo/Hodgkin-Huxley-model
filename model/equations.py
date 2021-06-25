import numpy as np


# Defining parameters Alpha and Beta

def alpha_n(voltage):
    a = (0.01*(10+voltage))/(np.exp((10+voltage)/10)-1)
    return a

def alpha_m(voltage):
    a = (0.1*(25+voltage))/(np.exp((25+voltage)/10)-1)
    return a

def alpha_h(voltage):
    a = 0.07*np.exp(voltage/20)
    return a

def beta_n(voltage):
    b = 0.125*np.exp(voltage/80)
    return b

def beta_m(voltage):
    b = 4*np.exp(voltage/18)
    return b

def beta_h(voltage):
    b = 1/(np.exp((30+voltage)/10)+1)
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

# Max conductance
g_K = 0
g_Na = 0
g_l = 0

# Channel voltages
v_K = 0
v_Na = 0
v_l = 0

# Capacitance of the manbrane
c = 0
