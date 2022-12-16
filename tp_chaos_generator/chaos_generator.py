""" Chaos Generator """
import struct
import numpy as np

from utils import circular_bit_rotate, half_precision, triple_pendulum_ode

class ChaosGenerator:
    """ Chaos Generator """
    def __init__(
        self,
        key: list
    ) -> None:
        self.key = key
        self.fps = 10000
        self.tstart = 0
        self.tend = 6.5535
        self.delta_t = 1./self.fps
        self.num_chars = 256
        self.eta = 0.9

    @classmethod
    def generate_key(cls) -> list:
        """ Key Generation """
        m1 = 0.2944
        m2 = 0.1765
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

        key = [theta1, theta2, theta3, dtheta1, dtheta2, dtheta3, m1, m2, m3, l1, l2, l3, I1, I2, I3, k1, k2, k3, g]
        return key

    def encrypt(self, plain_text: list) -> list:
        """ Data Encryption """
        _, yy = triple_pendulum_ode.triple_pendulum_ode(
            self.tstart,
            self.tend,
            self.delta_t,
            self.key)

        Y = yy[2]
        y_min = np.min(Y)
        y_max = np.max(Y)
        epsilon = (y_max + self.delta_t - y_min)/self.num_chars
        #epsilon = 2*np.pi/num_chars

        key_len = len(self.key)

        #generate lookup table
        lookup_table: list[int] = []
        for i in range(self.num_chars):
            lookup_table.append([])

        for j, y_val in enumerate(Y):
            d = int(np.floor((y_val - y_min) / epsilon))
            lookup_values = lookup_table[d]
            lookup_values.append(j)
            lookup_table[d] = lookup_values

        # print("Lookup Table")
        # print(lookup_table)

        #Encryption
        y = []

        ### selecting f(self.key) ###
        # f = halfprecision(self.key);
        # for K in range(1, key_len):
        #     f = bitxor(f, halfprecision(self.key[K]));

        for i, p in enumerate(plain_text):
            flag = False
            index = 0
            while flag is False:
                r = np.random.rand()
                #print(f"Random num generated: {r}")
                lookup_values = lookup_table[p]
                #c = intervals{1,d+1};

                #select random between 0 to 1 and compare with eta
                if r > self.eta:
                    #print(f"Index selected: {index}, Value: {lookup_values[index]}")
                    C = lookup_values[index]

                    f = struct.unpack('H', half_precision(self.key[i % key_len]))[0]

                    #Operations
                    C = circular_bit_rotate(C, -(i % 16), 16)
                    C = C^f
                    C = circular_bit_rotate(C, -(i % 16), 16)
                    C = C^f
                    C = circular_bit_rotate(C, -(i % 16), 16)
                    C = C^f

                    y.append(C)
                    flag = True
                else:
                    index = (index + 1) % len(lookup_values)

                # ### select random index ###
                # len = len(lookup_values);
                # r2 = np.random.randint([1, len])
                # print(f"Random num generated for length {len}: {r2}")
                # C = lookup_values(r2);
                # print(f"Iteration: {index}: key: {f}");
                # yy = bitxor(C, bitror(f, k));
                # y.append(yy);
                # flag= True

        return y

    def decrypt(self, cipher_text: list) -> list:
        """ Data Decryption """
        key_len = len(self.key)

        _, yy = triple_pendulum_ode.triple_pendulum_ode(
            self.tstart,
            self.tend,
            self.delta_t,
            self.key)
        Y = yy[2]
        y_min = np.min(Y)
        y_max = np.max(Y)
        epsilon = (y_max - y_min) / self.num_chars

        y = []

        #selecting f(self.key)
        # f = halfprecision(self.key);
        # for K in range(1, key_len):
        #     f = bitxor(f, halfprecision(self.key[K]));

        for i, c in enumerate(cipher_text):
            f = struct.unpack('H', half_precision(self.key[i % key_len]))[0]

            #Operations
            C = c^f
            C = circular_bit_rotate(C, i % 16, 16)
            C = C^f
            C = circular_bit_rotate(C, i % 16, 16)
            C = C^f
            C = circular_bit_rotate(C, i % 16, 16)

            y_val =  Y[C]
            d = np.floor((y_val - y_min) / epsilon)
            y.append(d)

        return y

def main():
    """ Main """
    m1=0.2944
    m2=0.1765
    m3=0.0947
    l1=0.508
    l2=0.254
    l3=0.127
    k1=0.005
    k2=0
    k3=0.0008
    I1=9.526e-3
    I2=1.625e-3
    I3=1.848e-4
    g=9.81

    theta1 = -0.4603
    theta2 = -1.2051
    theta3 = -1.5165
    dtheta1 = 0
    dtheta2 = 0
    dtheta3 = 0

    key = [theta1, theta2, theta3, dtheta1, dtheta2, dtheta3, m1, m2, m3, l1, l2, l3, I1, I2, I3, k1, k2, k3, g]
    cg = ChaosGenerator(key)

    str = 'A course in Cryptography'
    plain_text = [ord(x) for x in str]
    print("Plain Text: ", plain_text)
    cipher_text = cg.encrypt(plain_text)
    print("Cipher Text: ", cipher_text)
    clear_text = cg.decrypt(cipher_text)

    dec_text = [chr(int(i)) for i in clear_text]
    dec_text = ''.join(dec_text)
    print("Clear Text: ", dec_text)

if __name__ == "__main__":
    main()
