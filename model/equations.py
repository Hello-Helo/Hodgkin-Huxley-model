import numpy as np

from matplotlib import pyplot as plt
import matplotlib.animation as animation

from pathlib import Path

from ode_solutions import runge_kutta, euler

import argparse

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

def run_and_save():
    if name_space.euler == True:
        result = [euler(gen_dalldt(i), np.array([voltage, n0, m0, h0]), int(5000 * max(1, t[1]/300)), t) for i in i_list]
    else:
        result = [runge_kutta(gen_dalldt(i), np.array([voltage, n0, m0, h0]), int(5000 * max(1, t[1]/300)), t) for i in i_list]
    save_location = Path("cache/")
    if not save_location.exists():
        save_location.mkdir()
    np.save(save_location / f"result-{['runge_kutta','euler'][int(name_space.euler)]}-tf{name_space.final_time}", result)
    return result

def load():
    return np.load(Path("cache/") / f"result-{['runge_kutta','euler'][int(name_space.euler)]}-tf{name_space.final_time}.npy")

def animate(i):
    graph_line.set_ydata(result[i][:,column])
    text.set_text(f"Corrente = {round(i_list[i], 2)} mA")
    return graph_line,text,

# Main ####

parser = argparse.ArgumentParser(description='Hodgkin-Huxley Model')

parser.add_argument("-tf", "--final-time", type=int, action="store", default=300, help="Tempo final da análise")


method_group = parser.add_mutually_exclusive_group(required=True)
method_group.add_argument("-E", "--euler", action="store_true", help="Utilizar o método de Euler")
method_group.add_argument("-R", "--runge-kutta", action="store_true", help="Utilizar o método de Runge-Kutta")

graph_group = parser.add_mutually_exclusive_group()
graph_group.add_argument("-V", "--graph-voltage", action="store_true", help="Criar grafico da voltagem")
graph_group.add_argument("-N", "--graph-n", action="store_true", help="Criar grafico do n")
graph_group.add_argument("-M", "--graph-m", action="store_true", help="Criar grafico do m")
graph_group.add_argument("-H", "--graph-h", action="store_true", help="Criar grafico do h")

name_space = parser.parse_args()

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

# Time interval
tf = name_space.final_time
t = (0,tf)

i0 = -1
ifinal = 10
i_steps = 100
i_list = np.linspace(i0, ifinal, num=i_steps, endpoint=False)

try:
    result = load()
except IOError:
    run_and_save()
    result = load()

column = 1 + int(name_space.graph_n) + 2*int(name_space.graph_m) + 3*int(name_space.graph_h)

# Plotting

fig, ax = plt.subplots()
axis_sizes = [(-85, 60), (-0.15, 1.15), (-0.15, 1.15), (-0.15, 1.15)]
plt.ylim(axis_sizes[column-1])

graph_line, = ax.plot(result[0][:,0], result[0][:,column])

text = plt.text(25, 47, "")

ani = animation.FuncAnimation(fig, animate, interval=60, blit=True, frames=range(i_steps))

plt.ylabel(["Voltagem (mV)", "n (0-1)", "m (0-1)", "h (0-1)"][column-1])
plt.xlabel("Tempo (ms)")
plt.show()
