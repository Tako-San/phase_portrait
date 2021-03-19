import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def draw(start_conds):
    plt.style.use('dark_background')

    fig = plt.figure()
    ax = plt.axes()
    line, = ax.plot([], [], lw=2)

    # Заголовок анимации
    plt.xlabel('X1')
    plt.ylabel('dX1/dt')
    plt.title('Движение первого атома')
    # Скрываем лишние данные
    plt.axis('off')

    # Функция инициализации.
    def init():
        # создение пустого графа.

        line.set_data([], [])
        
        return line,

    xdata, ydata = [], []

    def x1_points(frame, start_conds):

        osc_arr, dot_osc_arr = calc_osc(frame * 0.005, start_conds)

        x1 = np.array([1, 1, 1]) @ osc_arr
        x1_dot = np.array([1, 1, 1]) @ dot_osc_arr

        xdata.append(x1)
        ydata.append(x1_dot)
        line.set_data(xdata, ydata)

        ax.relim()  # update axes limits
        ax.autoscale_view(True, True, True)
        return line, ax

    # Вызов анимации.
    anim = animation.FuncAnimation(fig, x1_points, init_func=init, fargs=(start_conds,),
                                frames=5000, interval=10, blit=True)
    
    plt.show()
    # Сохраняем анимацию как gif файл
    #anim.save('x1_-1_1_1.gif', writer='imagemagick')

def calc_osc(t, CONDS):
    w1 = np.sqrt(CONDS['c'] / CONDS['m'])
    w2 = np.sqrt(CONDS['c'] * (CONDS['n'] + 2) / (CONDS['m'] * CONDS['n']))

    ### start conds for theta
    theta1_0 = (CONDS['x1_0'] + CONDS['n'] * CONDS['x2_0'] + CONDS['x3_0']) / (2 + CONDS['n'])
    theta2_0 = (CONDS['x1_0'] - CONDS['x3_0']) / 2
    theta3_0 = (CONDS['n'] * CONDS['x1_0'] - 2 * CONDS['n'] * CONDS['x2_0'] + CONDS['n'] * CONDS['x3_0']) / (4 + 2 * CONDS['n'])


    ### start conds for dtheta/dt
    theta1_0_dot = (CONDS['x1_0_dot'] + CONDS['n'] * CONDS['x2_0_dot'] + CONDS['x3_0_dot']) / (2 + CONDS['n'])
    theta2_0_dot = (CONDS['x1_0_dot'] - CONDS['x3_0_dot']) / 2
    theta3_0_dot = (CONDS['n'] * CONDS['x1_0_dot'] - 2 * CONDS['n'] * CONDS['x2_0_dot'] + CONDS['n'] * CONDS['x3_0_dot']) / (4 + 2 * CONDS['n'])

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