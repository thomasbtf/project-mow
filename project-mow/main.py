import RPi.GPIO as GPIO

from drivers.l298n import L298N_1_Motor


def main():
    ena = 21
    in1 = 20
    in2 = 16
    enb = 13
    in3 = 26
    in4 = 19

    motor = L298N_1_Motor(en=ena, in1=in1, in2=in2)
    motor.change_speed(10)
    motor.forward()

    while True:
        user_input=input()

        if user_input == "f":
            motor.forward()

        elif user_input =="b":
            motor.backward()

        elif user_input =="s": 
            motor.clean_up()
            break


if __name__ == "__main__":
    main()
