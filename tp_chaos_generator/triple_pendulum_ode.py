""" Triple Pendulum ODE """

import numpy as np
from scipy.integrate import solve_ivp

from tp_chaos_generator.ode_func import ode_func
from tp_chaos_generator.utils import normalize_states, state_plotter, trajectory_plotter


def triple_pendulum_ode(start, end, step, ivp) -> list:
    """Solve ODE"""
    params = ivp[6:19]
    xinit = ivp[0:6]

    tspan = np.arange(start, end, step)
    sol = solve_ivp(
        lambda t, x: ode_func(t, x, params), [start, end], xinit, t_eval=tspan, rtol=1e-5
    )

    t, y = sol.t, sol.y
    y = normalize_states(y)

    return [t, y]


def main():
    """Main"""
    m1 = 0.2944
    m2 = 0.1756
    m3 = 0.0947
    l1 = 0.508
    l2 = 0.254
    l3 = 0.127
    k1 = 0.005
    k2 = 0
    k3 = 0.0008
    I1 = 9.526e-3
    I2 = 1.625e-3
    I3 = 1.848e-4
    g = 9.81

    theta1 = -0.4603
    theta2 = -1.2051
    theta3 = -1.5165
    dtheta1 = 0
    dtheta2 = 0
    dtheta3 = 0

    key = [
        theta1,
        theta2,
        theta3,
        dtheta1,
        dtheta2,
        dtheta3,
        m1,
        m2,
        m3,
        l1,
        l2,
        l3,
        I1,
        I2,
        I3,
        k1,
        k2,
        k3,
        g,
    ]

    start = 0
    stop = 10
    fps = 10000
    delta_t = 1.0 / fps
    t, y = triple_pendulum_ode(start, stop, delta_t, key)

    state_plotter(t, y, 1)
    trajectory_plotter(y, key)


if __name__ == "__main__":
    main()
