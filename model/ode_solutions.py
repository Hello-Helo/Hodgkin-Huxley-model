from matplotlib import pyplot as plt
import numpy as np

# ODE solving algorithim

def runge_kutta(f_prime, x, n, interval):
    t0 = interval[0]
    tf = interval[1]
    t = t0
    h = (tf-t0)/n
    points = [np.array([t,*x])]
    for i in range(0,n):
        k1 = np.array(f_prime(t,x))
        k2 = np.array(f_prime(t+0.5*h, x+0.5*k1*h))
        k3 = np.array(f_prime(t+0.5*h, x+0.5*k2*h))
        k4 = np.array(f_prime(t+h, x+h*k3))
        x = x + h/6*(k1+2*k2+2*k3+k4)
        t = t0 + (i + 1)*h
        points.append(np.concatenate(([t],x)))
    return np.vstack(points)

def euler(f_prime, x, n, interval):
    t0 = interval[0]
    tf = interval[1]
    t = t0
    h = (tf-t0)/n
    points = [(t,x)]
    for i in range(0,n):
        x = x + h*np.array(f_prime(t,x))
        t = (i + 1)*h
        points.append((t,x))
    return points

if __name__ == "__main__":
    def derivative(t,x):
        a = 0.3 * x * (1. - x/100.)
        return a

    interval = (0,30)
    interval1 = (0,3)
    # print(runge_kutta(derivative, 10, 100, interval))
    plt.plot(*zip(*runge_kutta(derivative, 10, 10, interval1)))
    plt.plot(*zip(*runge_kutta(derivative, 10, 100, interval)))
    # plt.plot(*zip(*euler(derivative, 10, 1, interval)))
    plt.show()
