try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print(
        "Error importing RPi.GPIO! "
        + "This is probably because you need superuser privileges. "
        + "You can achieve this by using 'sudo' to run your script"
    )


class L298N_1_Motor:
    """
    Interfacing for a L298N motor driver module to control one DC motor.

    Args:
        en (int): Pins to control speed of the connected motor.
        in1 (int): Pin to control spinning direction of the connected motor.
        in2 (int): Pin to control spinning direction of the connected motor.
        mode (str, optional): Pin numbering mode. Use "BOARD" to refer to the
        pin numbers on the P1 header of the Raspberry Pi board. Use "BCM" to
        refer to the channel numbers on the Broadcom SOC. Defaults to "BOARD".
        frequency (int, optional): Frequency of the Pulse-Width Modulation in
        Hz. Defaults to 1000.

        Raises:
            ValueError: Numbering mode not recognised.
    """

    def __init__(self, en: int, in1: int, in2: int, mode="BCM", frequency=1000) -> None:

        self.__speed = 0.0
        self.__in1 = in1
        self.__in2 = in2
        self.__turning = "stop"

        if GPIO.getmode() is None:
            if mode == "BOARD":
                GPIO.setmode(GPIO.BOARD)
            elif mode == "BCM":
                GPIO.setmode(GPIO.BCM)
            else:
                raise ValueError(
                    "Pin numbering mode not recognised. "
                    + "Must be either BOARD or BCM."
                )
            print(f"No numbering mode detected. Using {mode} numbering.")
        else:
            print(f"Using {GPIO.getmode()}")

        channel_list = [in1, in2]

        GPIO.setup(channel_list, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(en, GPIO.OUT)

        self.__p = GPIO.PWM(en, frequency)
        self.__p.start(0)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, dc: float):
        """Changes the duty cycle of the PWM and thus adjusts the speed of the motor.

        Args:
            dc (float): Duty cycle. Must be 0.0 <= dc <= 100.0
        """
        if dc > 100.0:
            dc = 100.0
        elif dc < 0.0:
            dc = 0.0
        self.__p.ChangeDutyCycle(dc)
        self.__speed = dc

    def forward(self):
        if self.__turning != "forward":
            GPIO.output(self.__in1, GPIO.HIGH)
            GPIO.output(self.__in2, GPIO.LOW)
            self.__turning = "forward"

    def backward(self):
        if self.__turning != "backward":
            GPIO.output(self.__in1, GPIO.LOW)
            GPIO.output(self.__in2, GPIO.HIGH)
            self.__turning = "backward"

    def stop(self):
        if self.__turning != "stop":
            GPIO.output(self.__in1, GPIO.LOW)
            GPIO.output(self.__in2, GPIO.LOW)
            self.__turning = "stop"

    def clean_up(self):
        self.stop()
        self.__p.stop()
        GPIO.cleanup()
