import numpy as np
import matplotlib.pyplot as plt

def state_plotter(times, states, fig_num):
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    plt.figure(fig_num)
    plt.clf()
    fig, ax = plt.subplots(num_rows, num_cols, num=fig_num, clear=True,
                         squeeze=False)
    for n in range(num_states):
        row = n // num_cols
        col = n % num_cols
        ax[row][col].plot(times, states[n], 'k.:')
        ax[row][col].set(xlabel='Time',
                         ylabel='$y_{:0.0f}(t)$'.format(n),
                         title='$y_{:0.0f}(t)$ vs. Time'.format(n))
        
    for n in range(num_states, num_rows * num_cols):
        fig.delaxes(ax[n // num_cols][n % num_cols])

    fig.tight_layout()
    plt.show()

    return fig, ax

def plot_state(times, states, state_id):
    plt.plot(times, states[state_id], '.', markersize=0.5)
    plt.show()

def plot_trajectory(times, states, params):
    l1, l2, l3 = params[3:6]
    phi1 = states[0]
    phi2 = states[1]
    phi3 = states[2]
    x1, y1 = l1*np.sin(phi1),l1*np.cos(phi1)
    x2, y2 = l1*np.sin(phi1)+l2*np.sin(phi2),l1*np.cos(phi1)+l2*np.cos(phi2)
    x3, y3 = l1*np.sin(phi1)+l2*np.sin(phi2)+l3*np.sin(phi3),l1*np.cos(phi1)+l2*np.cos(phi2)+l3*np.cos(phi3)
    plt.plot(x1, y1, '.', markersize=0.5)
    plt.plot(x2, y2, '.', markersize=0.5)
    plt.plot(x3, y3, '.', markersize=0.5)

    plt.show()