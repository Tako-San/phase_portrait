import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 20, 0.01)

c = 100
m = 0.1
n = 10

w1 = np.sqrt(c / m)
w2 = np.sqrt(c * (n + 2) / (m * n))

x1_0 = -1
x2_0 = 1
x3_0 = 1

x1_0_dot = 0
x2_0_dot = 0
x3_0_dot = 0

def calc_osc():

    ### start conds for theta
    theta1_0 = (x1_0 + n * x2_0 + x3_0) / (2 + n)
    theta2_0 = (x1_0 - x3_0) / 2
    theta3_0 = (n * x1_0 - 2 * n * x2_0 + n * x3_0) / (4 + 2 * n)


    ### start conds for dtheta/dt
    theta1_0_dot = (x1_0_dot + n * x2_0_dot + x3_0_dot) / (2 + n)
    theta2_0_dot = (x1_0_dot - x3_0_dot) / 2
    theta3_0_dot = (n * x1_0_dot - 2 * n * x2_0_dot + n * x3_0_dot) / (4 + 2 * n)

    osc_arr = np.array(
        [
            theta1_0 + theta1_0_dot * t,
            theta2_0 * np.cos(w1 * t) + (theta2_0_dot / w1) * np.sin(w1 * t),
            theta3_0 * np.cos(w2 * t) + (theta3_0_dot / w2) * np.sin(w2 * t)
        ]
    )

    dot_osc_arr = np.array(
        [
            theta1_0_dot,
            -theta2_0 * w1 * np.sin(w1 * t) + theta2_0_dot * np.cos(w1 * t),
            -theta3_0 * w2 * np.sin(w2 * t) + theta3_0_dot * np.cos(w2 * t)
        ]
    )

    return osc_arr, dot_osc_arr

def x1_points():
    osc_arr, dot_osc_arr = calc_osc()
    x1 = np.array([1, 1, 1]) @ osc_arr
    x1_dot = np.array([1, 1, 1]) @ dot_osc_arr
    return x1, x1_dot


def main():
    x1_res = x1_points()
    tkinter._test()
    #print(x1_res)

    plt.xlabel("x")
    plt.ylabel("dx/dt")

    plt.plot(x1_res[0], x1_res[1])
    plt.show()


if __name__ == '__main__':
    main()
