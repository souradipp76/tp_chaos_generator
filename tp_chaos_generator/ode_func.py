"""Triple Pendulum ODE Function"""

import numpy as np


def ode_func(t, x, params) -> list:
    """ODE Function"""
    m1, m2, m3, L1, L2, L3, I1, I2, I3, k1, k2, k3, g = params
    y0 = x[3]
    y1 = x[4]
    y2 = x[5]
    y3 = -(
        2
        * (
            (
                (L3**2) * (m3**2) * np.sin(2 * x[0] - 2 * x[2]) * (4 * I2 - (L2**2) * m2)
                + (L2**2)
                * np.sin(2 * x[0] - 2 * x[1])
                * (m2 + 2 * m3)
                * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
            )
            * (L1**2)
            * (x[3] ** 2)
            + (
                L2
                * (
                    np.sin(x[0] - x[1])
                    * (
                        (
                            m2 * m3 * (m2 + 3 * m3) * (L3**2)
                            + 4 * I3 * ((m2**2) + 6 * m2 * m3 + 8 * (m3**2))
                        )
                        * (L2**2)
                        + 4 * I2 * (m3 * (m2 + m3) * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                    )
                    + (L3**2) * (m3**2) * np.sin(x[0] + x[1] - 2 * x[2]) * (4 * I2 - (L2**2) * m2)
                )
                * (x[4] ** 2)
                - 4
                * k2
                * L2
                * (
                    np.cos(x[0] - x[1]) * (m3 * (m2 + m3) * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                    - (L3**2) * (m3**2) * np.cos(x[0] + x[1] - 2 * x[2])
                )
                * (x[4] ** 2)
                + L3
                * m3
                * (
                    np.sin(x[0] - x[2])
                    * (8 * I3 * m3 * (L2**2) + 4 * I2 * m3 * (L3**2) + 16 * I2 * I3)
                    + (L2**2)
                    * np.sin(x[0] - 2 * x[1] + x[2])
                    * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                )
                * (x[5] ** 2)
                - 4
                * k3
                * L3
                * m3
                * (
                    np.cos(x[0] - x[2]) * (2 * m3 * (L2**2) + 4 * I2)
                    - (L2**2) * np.cos(x[0] - 2 * x[1] + x[2]) * (m2 + 2 * m3)
                )
                * x[5]
                - g
                * (
                    np.sin(x[0])
                    * (
                        (
                            m3 * (m1 * m2 + 2 * m1 * m3 + 3 * m2 * m3 + (m2**2)) * (L3**2)
                            + 4 * I3 * ((m2**2) + 6 * m2 * m3 + m1 * m2 + 4 * (m3**2) + 4 * m1 * m3)
                        )
                        * (L2**2)
                        + 4
                        * I2
                        * (m3 * (m1 + 2 * m2 + m3) * (L3**2) + 4 * I3 * (m1 + 2 * m2 + 2 * m3))
                    )
                    + (L3**2)
                    * (m3**2)
                    * (
                        np.sin(x[0] - 2 * x[2]) * (4 * I2 - (L2**2) * m2)
                        - 2 * (L2**2) * np.cos(2 * x[1] - 2 * x[2]) * np.sin(x[0]) * (m1 + m2)
                    )
                    + (L2**2)
                    * np.sin(x[0] - 2 * x[1])
                    * (m2 + 2 * m3)
                    * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                )
            )
            * L1
            + 2
            * k1
            * (
                4 * I2 * (m3 * (L3**2) + 4 * I3)
                + (L2**2) * (m3 * (m2 + 2 * m3) * (L3**2) + 4 * I3 * (m2 + 4 * m3))
                - 2 * (L2**2) * (L3**2) * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
            )
            * x[0]
        )
    ) / (
        64 * I1 * I2 * I3
        + 8 * I3 * (L1**2) * (L2**2) * (m2**2)
        + 8 * I1 * (L2**2) * (L3**2) * (m3**2)
        + 8 * I2 * (L1**2) * (L3**2) * (m3**2)
        + 32 * I3 * (L1**2) * (L2**2) * (m3**2)
        + 16 * I2 * I3 * (L1**2) * m1
        + 16 * I1 * I3 * (L2**2) * m2
        + 64 * I2 * I3 * (L1**2) * m2
        + 16 * I1 * I2 * (L3**2) * m3
        + 64 * I1 * I3 * (L2**2) * m3
        + 64 * I2 * I3 * (L1**2) * m3
        + 4 * I3 * (L1**2) * (L2**2) * m1 * m2
        + 4 * I2 * (L1**2) * (L3**2) * m1 * m3
        + 16 * I3 * (L1**2) * (L2**2) * m1 * m3
        + 4 * I1 * (L2**2) * (L3**2) * m2 * m3
        + 16 * I2 * (L1**2) * (L3**2) * m2 * m3
        + 48 * I3 * (L1**2) * (L2**2) * m2 * m3
        - 8 * I1 * (L2**2) * (L3**2) * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
        - 2
        * (L1**2)
        * (L2**2)
        * np.cos(2 * x[0] - 2 * x[1])
        * (m2 + 2 * m3)
        * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
        - 2 * (L1**2) * (L3**2) * (m3**2) * np.cos(2 * x[0] - 2 * x[2]) * (-m2 * (L2**2) + 4 * I2)
        + 2 * (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2)
        + 6 * (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2)
        + 2 * (L1**2) * (L2**2) * (L3**2) * (m2**2) * m3
        + (L1**2) * (L2**2) * (L3**2) * m1 * m2 * m3
        - 2 * (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
        - 4 * (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
    )

    y4 = (
        2
        * (
            (
                (L1**2)
                * np.sin(2 * x[0] - 2 * x[1])
                * (m2 + 2 * m3)
                * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                - (L3**2)
                * (m3**2)
                * np.sin(2 * x[1] - 2 * x[2])
                * ((m1 + 2 * m2) * (L1**2) + 4 * I1)
            )
            * (L2**2)
            * (x[4] ** 2)
            + L1
            * (
                np.sin(x[0] - x[1])
                * (
                    (
                        m3 * (m1 * (m2 + m3) + 2 * m2 * (2 * m2 + 3 * m3)) * (L3**2)
                        + 4 * I3 * (m2 + 2 * m3) * (m1 + 4 * m2 + 4 * m3)
                    )
                    * (L1**2)
                    + 4 * I1 * (m3 * (m2 + m3) * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                )
                - (L3**2)
                * (m3**2)
                * np.sin(x[0] + x[1] - 2 * x[2])
                * ((m1 + 2 * m2) * (L1**2) + 4 * I1)
            )
            * L2
            * (x[3] ** 2)
            + 4
            * k1
            * L1
            * (
                np.cos(x[0] - x[1]) * (m3 * (m2 + m3) * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                - (L3**2) * (m3**2) * np.cos(x[0] + x[1] - 2 * x[2])
            )
            * L2
            * x[3]
            + (
                -L3
                * m3
                * (
                    np.sin(x[1] - x[2])
                    * (
                        (m3 * (m1 + 3 * m2) * (L3**2) + 4 * I3 * (m1 + 3 * m2 + 2 * m3)) * (L1**2)
                        + 4 * I1 * (m3 * (L3**2) + 4 * I3)
                    )
                    - (L1**2)
                    * np.sin(2 * x[0] - x[1] - x[2])
                    * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                )
                * (x[5] ** 2)
                + 4
                * k3
                * L3
                * m3
                * (
                    np.cos(x[1] - x[2]) * ((m1 + 3 * m2 + 2 * m3) * (L1**2) + 4 * I1)
                    - (L1**2) * np.cos(2 * x[0] - x[1] - x[2]) * (m2 + 2 * m3)
                )
                * x[5]
                + g
                * (
                    np.sin(x[1])
                    * (
                        (
                            m2 * m3 * (2 * m2 + 3 * m3) * (L3**2)
                            + 8 * I3 * ((m2**2) + 3 * m2 * m3 + 2 * (m3**2))
                        )
                        * (L1**2)
                        + 4 * I1 * (m3 * (m2 + m3) * (L3**2) + 4 * I3 * (m2 + 2 * m3))
                    )
                    - (L1**2)
                    * np.sin(2 * x[0] - x[1])
                    * (
                        m3 * (m1 * (m2 + m3) + m2 * (2 * m2 + 3 * m3)) * (L3**2)
                        + 4 * I3 * (m2 + 2 * m3) * (m1 + 2 * m2 + 2 * m3)
                    )
                    + (L3**2)
                    * (m3**2)
                    * (
                        np.sin(x[1] - 2 * x[2]) * (m2 * (L1**2) + 4 * I1)
                        + (L1**2) * np.sin(2 * x[0] + x[1] - 2 * x[2]) * (m1 + m2)
                    )
                )
            )
            * L2
            - 2
            * k2
            * (
                4 * I1 * (m3 * (L3**2) + 4 * I3)
                + (L1**2)
                * (m3 * (m1 + 4 * m2 + 2 * m3) * (L3**2) + 4 * I3 * (m1 + 4 * m2 + 4 * m3))
                - 2 * (L1**2) * (L3**2) * (m3**2) * np.cos(2 * x[0] - 2 * x[2])
            )
            * (x[4] ** 2)
        )
    ) / (
        64 * I1 * I2 * I3
        + 8 * I3 * (L1**2) * (L2**2) * (m2**2)
        + 8 * I1 * (L2**2) * (L3**2) * (m3**2)
        + 8 * I2 * (L1**2) * (L3**2) * (m3**2)
        + 32 * I3 * (L1**2) * (L2**2) * (m3**2)
        + 16 * I2 * I3 * (L1**2) * m1
        + 16 * I1 * I3 * (L2**2) * m2
        + 64 * I2 * I3 * (L1**2) * m2
        + 16 * I1 * I2 * (L3**2) * m3
        + 64 * I1 * I3 * (L2**2) * m3
        + 64 * I2 * I3 * (L1**2) * m3
        + 4 * I3 * (L1**2) * (L2**2) * m1 * m2
        + 4 * I2 * (L1**2) * (L3**2) * m1 * m3
        + 16 * I3 * (L1**2) * (L2**2) * m1 * m3
        + 4 * I1 * (L2**2) * (L3**2) * m2 * m3
        + 16 * I2 * (L1**2) * (L3**2) * m2 * m3
        + 48 * I3 * (L1**2) * (L2**2) * m2 * m3
        - 8 * I1 * (L2**2) * (L3**2) * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
        - 2
        * (L1**2)
        * (L2**2)
        * np.cos(2 * x[0] - 2 * x[1])
        * (m2 + 2 * m3)
        * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
        - 2 * (L1**2) * (L3**2) * (m3**2) * np.cos(2 * x[0] - 2 * x[2]) * (-m2 * (L2**2) + 4 * I2)
        + 2 * (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2)
        + 6 * (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2)
        + 2 * (L1**2) * (L2**2) * (L3**2) * (m2**2) * m3
        + (L1**2) * (L2**2) * (L3**2) * m1 * m2 * m3
        - 2 * (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
        - 4 * (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
    )

    y5 = -(
        2
        * (
            32 * I1 * I2 * k3 * x[5]
            - L2
            * L3
            * m3
            * (x[4] ** 2)
            * (
                np.sin(x[1] - x[2])
                * (
                    (
                        (L2**2) * (m1 * m2 + 4 * m1 * m3 + 6 * m2 * m3 + (m2**2))
                        + 4 * I2 * (m1 + 3 * m2 + 2 * m3)
                    )
                    * (L1**2)
                    + 4 * I1 * (4 * I2 + (L2**2) * (m2 + 4 * m3))
                )
                + (L1**2) * np.sin(2 * x[0] - x[1] - x[2]) * (m2 + 2 * m3) * (4 * I2 - m2 * (L2**2))
            )
            - L1
            * L3
            * m3
            * (x[3] ** 2)
            * (
                np.sin(x[0] - x[2])
                * (
                    8 * I1 * (m3 * (L2**2) + 2 * I2)
                    + 2
                    * (L1**2)
                    * ((m1 * m3 - (m2**2)) * (L2**2) + 2 * I2 * (m1 + 4 * m2 + 4 * m3))
                )
                - (L2**2)
                * np.sin(x[0] - 2 * x[1] + x[2])
                * (m2 + 2 * m3)
                * ((m1 + 2 * m2) * (L1**2) + 4 * I1)
            )
            + 4 * k3 * (L1**2) * (L2**2) * (m2**2) * x[5]
            + 16 * k3 * (L1**2) * (L2**2) * (m3**2) * x[5]
            + 8 * I2 * k3 * (L1**2) * m1 * x[5]
            + 8 * I1 * k3 * (L2**2) * m2 * x[5]
            + 32 * I2 * k3 * (L1**2) * m2 * x[5]
            + 32 * I1 * k3 * (L2**2) * m3 * x[5]
            + 32 * I2 * k3 * (L1**2) * m3 * x[5]
            - 4
            * k1
            * L1
            * L3
            * m3
            * x[3]
            * (
                np.cos(x[0] - x[2]) * (2 * m3 * (L2**2) + 4 * I2)
                - (L2**2) * np.cos(x[0] - 2 * x[1] + x[2]) * (m2 + 2 * m3)
            )
            - 16 * I1 * I2 * g * L3 * m3 * np.sin(x[2])
            - 4 * I2 * (L1**2) * (L3**2) * (m3**2) * (x[5] ** 2) * np.sin(2 * x[0] - 2 * x[2])
            - 4 * I1 * (L2**2) * (L3**2) * (m3**2) * (x[5] ** 2) * np.sin(2 * x[1] - 2 * x[2])
            + 8 * I2 * g * (L1**2) * L3 * (m3**2) * np.sin(2 * x[0] - x[2])
            + 8 * I1 * g * (L2**2) * L3 * (m3**2) * np.sin(2 * x[1] - x[2])
            + 2 * k3 * (L1**2) * (L2**2) * m1 * m2 * x[5]
            + 8 * k3 * (L1**2) * (L2**2) * m1 * m3 * x[5]
            + 24 * k3 * (L1**2) * (L2**2) * m2 * m3 * x[5]
            - 4
            * k2
            * L2
            * L3
            * m3
            * x[4]
            * (
                np.cos(x[1] - x[2]) * ((m1 + 3 * m2 + 2 * m3) * (L1**2) + 4 * I1)
                - (L1**2) * np.cos(2 * x[0] - x[1] - x[2]) * (m2 + 2 * m3)
            )
            - 8 * I1 * g * (L2**2) * L3 * (m3**2) * np.sin(x[2])
            - 8 * I2 * g * (L1**2) * L3 * (m3**2) * np.sin(x[2])
            - 4 * k3 * (L1**2) * (L2**2) * (m2**2) * x[5] * np.cos(2 * x[0] - 2 * x[1])
            - 16 * k3 * (L1**2) * (L2**2) * (m3**2) * x[5] * np.cos(2 * x[0] - 2 * x[1])
            - 8 * I2 * g * (L1**2) * L3 * m2 * m3 * np.sin(x[2])
            - 16 * k3 * (L1**2) * (L2**2) * m2 * m3 * x[5] * np.cos(2 * x[0] - 2 * x[1])
            - (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2) * (x[5] ** 2) * np.sin(2 * x[1] - 2 * x[2])
            + (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2) * (x[5] ** 2) * np.sin(2 * x[0] - 2 * x[2])
            - 2
            * (L1**2)
            * (L2**2)
            * (L3**2)
            * m2
            * (m3**2)
            * (x[5] ** 2)
            * np.sin(2 * x[1] - 2 * x[2])
            + 2 * g * (L1**2) * (L2**2) * L3 * m1 * (m3**2) * np.sin(2 * x[0] - x[2])
            - g * (L1**2) * (L2**2) * L3 * (m2**2) * m3 * np.sin(2 * x[0] - x[2])
            + 2 * g * (L1**2) * (L2**2) * L3 * m2 * (m3**2) * np.sin(2 * x[1] - x[2])
            + g * (L1**2) * (L2**2) * L3 * (m2**2) * m3 * np.sin(2 * x[1] - x[2])
            + 4 * I2 * g * (L1**2) * L3 * m1 * m3 * np.sin(2 * x[0] - x[2])
            + 8 * I2 * g * (L1**2) * L3 * m2 * m3 * np.sin(2 * x[0] - x[2])
            + 4 * I1 * g * (L2**2) * L3 * m2 * m3 * np.sin(2 * x[1] - x[2])
            - 2 * g * (L1**2) * (L2**2) * L3 * m1 * (m3**2) * np.sin(2 * x[0] - 2 * x[1] + x[2])
            - 2 * g * (L1**2) * (L2**2) * L3 * m2 * (m3**2) * np.sin(2 * x[0] - 2 * x[1] + x[2])
            - g * (L1**2) * (L2**2) * L3 * (m2**2) * m3 * np.sin(2 * x[0] - 2 * x[1] + x[2])
            + g * (L1**2) * (L2**2) * L3 * (m2**2) * m3 * np.sin(x[2])
            - g * (L1**2) * (L2**2) * L3 * m1 * m2 * m3 * np.sin(2 * x[0] - 2 * x[1] + x[2])
        )
    ) / (
        64 * I1 * I2 * I3
        + 8 * I3 * (L1**2) * (L2**2) * (m2**2)
        + 8 * I1 * (L2**2) * (L3**2) * (m3**2) * +8 * I2 * (L1**2) * (L3**2) * (m3**2)
        + 32 * I3 * (L1**2) * (L2**2) * (m3**2)
        + 16 * I2 * I3 * (L1**2) * m1
        + 16 * I1 * I3 * (L2**2) * m2
        + 64 * I2 * I3 * (L1**2) * m2
        + 16 * I1 * I2 * (L3**2) * m3
        + 64 * I1 * I3 * (L2**2) * m3
        + 64 * I2 * I3 * (L1**2) * m3
        + 4 * I3 * (L1**2) * (L2**2) * m1 * m2
        + 4 * I2 * (L1**2) * (L3**2) * m1 * m3
        + 16 * I3 * (L1**2) * (L2**2) * m1 * m3
        + 4 * I1 * (L2**2) * (L3**2) * m2 * m3
        + 16 * I2 * (L1**2) * (L3**2) * m2 * m3
        + 48 * I3 * (L1**2) * (L2**2) * m2 * m3
        - 8 * I1 * (L2**2) * (L3**2) * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
        - 2
        * (L1**2)
        * (L2**2)
        * np.cos(2 * x[0] - 2 * x[1])
        * (m2 + 2 * m3)
        * (m2 * m3 * (L3**2) + 4 * I3 * (m2 + 2 * m3))
        - 2 * (L1**2) * (L3**2) * (m3**2) * np.cos(2 * x[0] - 2 * x[2]) * (4 * I2 - m2 * (L2**2))
        + 2 * (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2)
        + 6 * (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2)
        + 2 * (L1**2) * (L2**2) * (L3**2) * (m2**2) * m3
        + (L1**2) * (L2**2) * (L3**2) * m1 * m2 * m3
        - 2 * (L1**2) * (L2**2) * (L3**2) * m1 * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
        - 4 * (L1**2) * (L2**2) * (L3**2) * m2 * (m3**2) * np.cos(2 * x[1] - 2 * x[2])
    )

    dydt = [y0, y1, y2, y3, y4, y5]
    return dydt
