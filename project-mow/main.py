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
            print("Turning forward...")
            motor.forward()

        elif user_input =="b":
            print("Turning backward...")
            motor.backward()

        elif user_input =="s": 
            print("Stopping...")
            motor.clean_up()
            break

        elif user_input =="e": 
            print("Exiting...")
            motor.clean_up()
            break

        elif "speed:" in user_input:
            print(user_input)
            print(user_input.split("speed:")[-1])
            print(eval(user_input.split("speed:")[-1]))
            dc = float(user_input.split("speed:")[-1])
            print(f"Setting speed to {dc}")
            motor.change_speed(dc)


if __name__ == "__main__":
    main()
