import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10000000)

c = 100
m = 0.1
n = 3

w1 = np.sqrt(c / m)
w2 = (n + 2) * np.sqrt(c / (m * n * (n - 2)))

d1 = 1
d2 = 1
d3 = 1

psi1 = 0.7
psi2 = 0.4

x0 = 0.1


def x1_points():
    x1 = d1 * np.sin(w1 * t + psi1) + d2 * (t + x0) + d3 * n * np.sin(w2 * t + psi2)
    x1_dot = d1 * w1 * np.sin(w1 * t + psi1) + d2 + d2 * n * w2 * np.sin(w2 * t + psi2)
    return x1, x1_dot


def main():
    x1_res = x1_points()

    plt.xlabel("x")
    plt.ylabel("dx/dt")

    plt.plot(x1_res[0], x1_res[1])
    plt.show()


if __name__ == '__main__':
    main()
