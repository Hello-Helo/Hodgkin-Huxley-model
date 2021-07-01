from matplotlib import pyplot as plt

# ODE solving algorithim

def runge_kutta(f_prime, x, n, interval):
    t0 = interval[0]
    tf = interval[1]
    t = t0
    h = (tf-t0)/n
    points = [(t,x)]
    for i in range(0,n):
        k1 = f_prime(t,x)
        k2 = f_prime(t+0.5*h, x+0.5*k1)
        k3 = f_prime(t+0.5*h, x+0.5*k2)
        k4 = f_prime(t+h, x+h*k3)
        x = x + h/6*(k1+2*k2+2*k3+k4)
        t = (i + 1)*h
        points.append((t,x))
    return points

def euler(f_prime, x, n, interval):
    t0 = interval[0]
    tf = interval[1]
    t = t0
    h = (tf-t0)/n
    points = [(t,x)]
    for i in range(0,n):
        x = x + h*f_prime(t,x)
        t = (i + 1)*h
        points.append((t,x))
    return points

# Main

def derivative(t,x):
    a = 0.3 * x * (1. - x/100.)
    return a

interval = (0,30)
# print(runge_kutta(derivative, 10, 100, interval))
plt.plot(*zip(*runge_kutta(derivative, 10, 10000, interval)))
plt.plot(*zip(*euler(derivative, 10, 10000, interval)))
plt.show()
