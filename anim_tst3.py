import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=2)

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

def calc_osc(t):

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

# Функция инициализации.
def init():
    # создение пустого графа.
    line.set_data([], [])
    return line,


xdata, ydata = [], []

def x1_points(frame):

    osc_arr, dot_osc_arr = calc_osc(frame * 0.003)

    x1 = np.array([1, 1, 1]) @ osc_arr
    x1_dot = np.array([1, 1, 1]) @ dot_osc_arr

    xdata.append(x1)
    ydata.append(x1_dot)
    line.set_data(xdata, ydata)

    ax.relim()  # update axes limits
    ax.autoscale_view(True, True, True)
    return line, ax

# функция анимации
def animate(i):
    t = 0.1 * i

    # x, y данные на графике
    x = t * np.sin(t)
    y = t * np.cos(t)

    # добавление новых точек в список точек осей x, y
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,


# Заголовок анимации
plt.title('Создаем спираль в matplotlib')
# Скрываем лишние данные
plt.axis('off')

# Вызов анимации.
anim = animation.FuncAnimation(fig, x1_points, init_func=init,
                               frames=5000, interval=20, blit=True)
plt.show()
# Сохраняем анимацию как gif файл
#anim.save('x1_-1_1_1.gif', writer='imagemagick')