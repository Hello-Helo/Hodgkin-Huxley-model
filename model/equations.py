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

# main

# Max conductance
g_K = 0
g_Na = 0
g_l = 0
