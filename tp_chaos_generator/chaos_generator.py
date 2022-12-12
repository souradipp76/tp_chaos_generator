import numpy as np

import utils
import triple_pendulum_ode

class ChaosGenerator: 
    def __init__(
        self,
        key: list
    ) -> None:
        self.encryption_key = key
        self.fps = 1000
        self.tstart = 0
        self.tend = 10
        self.delta_t = 1./self.fps

    @classmethod
    def generate_key(cls) -> list:
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

        key = [theta1,theta2,theta3,dtheta1,dtheta2,dtheta3,m1,m2,m3,l1,l2,l3,I1,I2,I3,k1,k2,k3,g]
        return key

    def encrypt(self, data: bytes) -> list:
        ivp = self.encryption_key

        num_chars = 256
        eta = 0.9
        
        t, yy = triple_pendulum_ode.triple_pendulum_ode(self.tstart, self.tend, self.delta_t, ivp)
        Y = yy[2]
        y_min = np.min(Y)
        y_max = np.max(Y)
        epsilon = (y_max - y_min)/num_chars
        #epsilon = 2*np.pi/num_chars
        
        intervals = []
        y = []
        
        print(y_min, y_max)
        for i in range(num_chars-1):
            possibles = []
            for j,z in enumerate(Y):
                if  (z >= y_min+i*epsilon) and (z < y_min + (i+1)*epsilon):
                    possibles.append(j)

            if len(possibles) == 0:
                print(f"{i}\n")
            intervals.append(possibles)

        plain_text_arr = data
        for k in range(len(data)):
            d = plain_text_arr[k]
            flag = False
            index = 0
            while flag is False:
                r = np.random.randn()
                c = intervals[d]
                if r > eta:
                    y.append(c[index])
                    flag = True
                    index+=1
                else:
                    index = index % len(c)

        return y

    def decrypt(
        self,
        data
    ) -> list:

        ivp = self.encryption_key
        num_chars = 256

        t, yy = triple_pendulum_ode.triple_pendulum_ode(self.tstart, self.tend, self.delta_t, ivp)
        Y = yy[2]
        y_min = np.min(Y)
        y_max = np.max(Y)
        epsilon = (y_max - y_min)/num_chars
        
        y = []
        cipher_text_arr = data
        for x in cipher_text_arr:
            y_val =  Y[x]
            d = (y_val - y_min)/epsilon;
            y.append(int(np.floor(d)));

        return y

def main():
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

    key = [theta1,theta2,theta3,dtheta1,dtheta2,dtheta3,m1,m2,m3,l1,l2,l3,I1,I2,I3,k1,k2,k3,g]
    cg = ChaosGenerator(key)

    str = 'A course in Cryptography'
    plain_text = [ord(x) for x in str]
    cipher_text = cg.encrypt(plain_text)
    clear_text = cg.decrypt(cipher_text)

    dec_text = [chr(i) for i in clear_text]
    dec_text = ''.join(dec_text)
    print(dec_text)

if __name__ == "__main__":
    main()