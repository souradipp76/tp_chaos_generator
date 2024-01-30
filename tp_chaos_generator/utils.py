""" Utils """

from __future__ import division

import base64
import csv
import struct
from math import copysign, frexp, isinf, isnan, trunc

import matplotlib.pyplot as plt
import numpy as np

NEGATIVE_INFINITY = b"\x00\xfc"
POSITIVE_INFINITY = b"\x00\x7c"
POSITIVE_ZERO = b"\x00\x00"
NEGATIVE_ZERO = b"\x00\x80"
# exp=2**5-1 and significand non-zero
EXAMPLE_NAN = struct.pack("<H", (0b11111 << 10) | 1)


def half_precision(f):
    """Convert Python float to IEEE 754-2008 (binary16) format."""
    if isnan(f):
        return EXAMPLE_NAN

    sign = copysign(1, f) < 0
    if isinf(f):
        return NEGATIVE_INFINITY if sign else POSITIVE_INFINITY

    #           1bit        10bits             5bits
    # f = (-1)**sign * (1 + f16 / 2**10) * 2**(e16 - 15)
    # f = (m * 2)                        * 2**(e - 1)
    m, e = frexp(f)
    assert not (isnan(m) or isinf(m))
    if e == 0 and m == 0:  # zero
        return NEGATIVE_ZERO if sign else POSITIVE_ZERO

    f16 = trunc((2 * abs(m) - 1) * 2**10)  # round toward zero
    assert 0 <= f16 < 2**10
    e16 = e + 14
    if e16 <= 0:  # subnormal
        # f = (-1)**sign * fraction / 2**10 * 2**(-14)
        f16 = int(2**14 * 2**10 * abs(f) + 0.5)  # round
        e16 = 0
    elif e16 >= 0b11111:  # infinite
        return NEGATIVE_INFINITY if sign else POSITIVE_INFINITY
    else:
        # normalized value
        assert 0b00001 <= e16 < 0b11111, (f, sign, e16, f16)

    return struct.pack("<H", (sign << 15) | (e16 << 10) | f16)


def state_plotter(times, states, fig_num):
    """Plotting states of triple pendulum"""
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    plt.figure(fig_num)
    plt.clf()
    fig, ax = plt.subplots(num_rows, num_cols, num=fig_num, clear=True, squeeze=False)
    for n in range(num_states):
        row = n // num_cols
        col = n % num_cols
        ax[row][col].plot(times, states[n], "k.:", markersize=0.5)
        ax[row][col].set(
            xlabel="Time", ylabel=f"$y_{n:0.0f}(t)$", title=f"$y_{n:0.0f}(t)$ vs. Time"
        )

    for n in range(num_states, num_rows * num_cols):
        fig.delaxes(ax[n // num_cols][n % num_cols])

    fig.tight_layout()
    plt.show()

    return fig, ax


def trajectory_plotter(states, params: list):
    """Plotting trajectory of triple pendulum"""
    L1, L2, L3 = params[3:6]
    phi1 = states[0]
    phi2 = states[1]
    phi3 = states[2]
    x1, y1 = L1 * np.sin(phi1), L1 * np.cos(phi1)
    x2, y2 = L1 * np.sin(phi1) + L2 * np.sin(phi2), L1 * np.cos(phi1) + L2 * np.cos(phi2)
    x3, y3 = L1 * np.sin(phi1) + L2 * np.sin(phi2) + L3 * np.sin(phi3), L1 * np.cos(
        phi1
    ) + L2 * np.cos(phi2) + L3 * np.cos(phi3)
    plt.plot(x1, y1, ".", markersize=0.5)
    plt.plot(x2, y2, ".", markersize=0.5)
    plt.plot(x3, y3, ".", markersize=0.5)

    plt.show()


def circular_bit_rotate(n, n_bits, bit_len):
    """Circular Bit Rotate"""
    bit_str = bin(n)[2:].zfill(bit_len)

    if n_bits > 0:
        n_rotated = bit_str[bit_len - n_bits :] + bit_str[0 : bit_len - n_bits]
    else:
        n_bits = -n_bits
        n_rotated = bit_str[n_bits:] + bit_str[0:n_bits]

    return int(n_rotated, 2)


def convert_to_bytes(data: str) -> list:
    """Convert to Bytes"""
    return [ord(x) for x in data]


def convert_to_string(data: list) -> str:
    """Convert to String"""
    return "".join(map(chr, data))


def normalize_states(y: list) -> list:
    """Normalize States"""
    y = y - np.floor(y / (2 * np.pi)) * (2 * np.pi)
    return y


def encode_keyset(file, path):
    """Encode Key Set File"""
    lines = []

    try:
        with open(file, "r", encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
            for row in reader:
                lines.append(row)

        with open(path, "wb") as f:
            for line in lines:
                line_str = ",".join(line)
                line_byte = line_str.encode("utf-8")
                enc_line = base64.b64encode(line_byte)
                f.write(enc_line)
                f.write(b"\n")
    except OSError as ex:
        print(f"Exception while encoding file: {str(ex)}")


def decode_key(enc_bytes) -> list:
    """Decode Key"""
    try:
        enc_bytes = enc_bytes.strip()
        dec_line = base64.b64decode(enc_bytes)
        dec_line_str = dec_line.decode()
        key = [float(value) for value in dec_line_str.split(",")]
        return key
    except OSError as ex:
        print(f"Exception while decoding key bytes: {str(ex)}")
        return []
