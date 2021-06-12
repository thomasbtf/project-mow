from actuators.motors import L298N_1_Motor


class Differenital_Drive:
    def __init__(self, left_motor, right_motor, L, R):
        # L = 10 # wheel base
        # R = 10 # radius of wheels

        # v_r # velocity of right wheel
        # v_l # velocity of left wheel
        print("hello")
        pass


class Simple_Drive:
    def __init__(self):
        ena = 21
        in1 = 20
        in2 = 16
        enb = 13
        in3 = 26
        in4 = 19

        self.left_motor = L298N_1_Motor(en=ena, in1=in1, in2=in2)
        self.right_motor = L298N_1_Motor(en=enb, in1=in3, in2=in4)

    def move(self, dx, dy):
        if dy > 0:
            self.left_motor.forward()
            self.right_motor.forward()
        else:
            self.left_motor.backward()
            self.right_motor.backward()

        self.left_motor.speed = abs(dy) - dx
        self.right_motor.speed = abs(dy) + dx
