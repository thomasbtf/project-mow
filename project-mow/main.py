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
    motor.speed = 50.0
    motor.forward()
    print("Running motor at 50%")

    while True:
        user_input = input()

        if user_input == "f":
            print("Turning forward...\n")
            motor.forward()

        elif user_input == "b":
            print("Turning backward...\n")
            motor.backward()

        elif user_input == "s":
            print("Stopping...\n")
            motor.stop()

        elif user_input == "e":
            print("Exiting...\n")
            motor.clean_up()
            break

        elif "speed:" in user_input:
            dc = float(user_input.split("speed:")[-1])
            print(f"Setting speed to {dc}\n")
            motor.set_speed = dc


if __name__ == "__main__":
    main()
