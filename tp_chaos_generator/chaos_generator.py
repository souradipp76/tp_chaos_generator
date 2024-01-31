""" Chaos Generator """

import struct
import time

import numpy as np

from tp_chaos_generator.triple_pendulum_ode import triple_pendulum_ode
from tp_chaos_generator.utils import (
    circular_bit_rotate,
    convert_to_bytes,
    convert_to_string,
    decode_key,
    half_precision,
)


class ChaosGenerator:
    """Chaos Generator"""

    def __init__(
        self,
    ) -> None:
        self.fps = 10000
        self.tstart = 0
        self.tend = 6.5535
        self.delta_t = 1.0 / self.fps
        self.num_chars = 256
        self.eta = 0.9
        self.g = 9.81
        self.vault_path = "./vault/keyset.txt"
        self.rng = np.random.default_rng()

    def generate_key(self) -> list:
        """Key Generation"""
        key = self.fetch_key(self.vault_path)
        key.append(self.g)
        return key

    def encrypt(self, plain_text: list, key: list) -> list:
        """Data Encryption"""

        _, yy = triple_pendulum_ode(self.tstart, self.tend, self.delta_t, key)

        Y = yy[2]
        y_min = np.min(Y)
        y_max = np.max(Y)
        epsilon = (y_max - y_min) / self.num_chars
        # epsilon = 2 * np.pi / self.num_chars

        key_len = len(key)

        # generate lookup table
        lookup_table: list[list] = []
        for i in range(self.num_chars):
            lookup_table.append([])

        for j, y_val in enumerate(Y):
            d = int(np.floor((y_val - y_min) / epsilon)) % self.num_chars
            lookup_values = lookup_table[d]
            lookup_values.append(j)
            lookup_table[d] = lookup_values

        # print("Lookup Table")
        # print(lookup_table)

        # Encryption
        y = []

        # # selecting f(self.key)
        # f = halfprecision(self.key);
        # for K in range(1, key_len):
        #     f = bitxor(f, halfprecision(self.key[K]));

        for i, p in enumerate(plain_text):
            flag = False
            index = 0
            while flag is False:
                r = np.random.rand()
                # print(f"Random num generated: {r}")
                lookup_values = lookup_table[p]
                # c = intervals{1,d+1};

                # select random between 0 to 1 and compare with eta
                if r > self.eta:
                    # print(f"Index selected: {index}, Value: {lookup_values[index]}")
                    C = lookup_values[index]

                    f = struct.unpack("H", half_precision(key[i % key_len]))[0]

                    # Operations
                    C = circular_bit_rotate(C, -(i % 16), 16)
                    C = C ^ f
                    C = circular_bit_rotate(C, -(i % 16), 16)
                    C = C ^ f
                    C = circular_bit_rotate(C, -(i % 16), 16)
                    C = C ^ f

                    y.append(C)
                    flag = True
                else:
                    index = (index + 1) % len(lookup_values)

                # # select random index
                # len = len(lookup_values);
                # r2 = np.random.randint([1, len])
                # print(f"Random num generated for length {len}: {r2}")
                # C = lookup_values(r2);
                # print(f"Iteration: {index}: key: {f}");
                # yy = bitxor(C, bitror(f, k));
                # y.append(yy);
                # flag= True

        return y

    def decrypt(self, cipher_text: list, key: list) -> list:
        """Data Decryption"""
        key_len = len(key)

        _, yy = triple_pendulum_ode(self.tstart, self.tend, self.delta_t, key)
        Y = yy[2]
        y_min = np.min(Y)
        y_max = np.max(Y)
        epsilon = (y_max - y_min) / self.num_chars

        y = []

        # # selecting f(self.key)
        # f = halfprecision(self.key);
        # for K in range(1, key_len):
        #     f = bitxor(f, halfprecision(self.key[K]));

        for i, c in enumerate(cipher_text):
            f = struct.unpack("H", half_precision(key[i % key_len]))[0]

            # Operations
            C = c ^ f
            C = circular_bit_rotate(C, i % 16, 16)
            C = C ^ f
            C = circular_bit_rotate(C, i % 16, 16)
            C = C ^ f
            C = circular_bit_rotate(C, i % 16, 16)

            y_val = Y[C]
            d = np.floor((y_val - y_min) / epsilon) % self.num_chars
            y.append(int(d))

        return y

    def fetch_key(self, path) -> list:
        """Fetching Key from Vault"""
        try:
            with open(path, "rb") as f:
                lines = f.readlines()
            keyset_len = len(lines)
            seed = int(time.time())
            self.rng = np.random.RandomState(seed)
            index = self.rng.randint(0, keyset_len)
            key = decode_key(lines[index])
            return key
        except OSError as ex:
            print(f"Error while fetching key. {str(ex)}")
            return []


def main():
    """Main"""
    cg = ChaosGenerator()
    key = cg.generate_key()
    str = "A course in Cryptography"
    plain_text = convert_to_bytes(str)
    print("Plain Text: ", plain_text)
    cipher_text = cg.encrypt(plain_text, key)
    print("Cipher Text: ", cipher_text)
    clear_text = cg.decrypt(cipher_text, key)
    dec_text = convert_to_string(clear_text)
    print("Clear Text: ", dec_text)


if __name__ == "__main__":
    main()
