# Project Mow ✂️ 🌱

Towards the usage of a Raspberry Pi Zero WH as an autonomous lawn mower robot.

## Hardware

- 1x Raspberry Pi Zero WH - [15.19 €](https://www.berrybase.de/raspberry-pi/raspberry-pi-computer/boards/raspberry-pi-zero-wh)
- 1x 32GB micro SD card - [8.85 €](https://www.berrybase.de/raspberry-pi/raspberry-pi-computer/speicherkarten/sandisk-extreme-micro-sdhc-a1-uhs-i-u3-speicherkarte-43-adapter-32gb?c=183)
- 1x u-blox NEO-6M GPS TTL receiver incl. antenna - [6.90 €](https://www.berrybase.de/audio-video/navigation/u-blox-neo-6m-gps-ttl-empf-228-nger-inkl.-antenne)
- 2x 12 V DC electric gear motor - [11.39 €/pc](https://www.amazon.de/gp/product/B0728HDH45)
- 1x L298N motor driver - [4.99 €](https://www.amazon.de/gp/B07DK6Q8F9)
- 1x Swivel castor Ø 75 mm - [4.99 €](https://www.amazon.de/gp/product/B078KFJF8T)

Total costs: 63.70 €

## Configuring the Raspberry Pi Zero W for Serial Interaction
In order to work, the GPS module needs a serial connection to the Pi. Follow the next steps to activate this connection.

1. Execute `sudo raspi-config` in the terminal.
2. We’re are interested in the `Interfacing` options. Select it and proceed to choosing `P6 Serial` from the list. You’ll be presented with two new prompts:
    - The first prompt will ask if you want to enable logins over the serial connection: choose **No**.
    - The next screen will ask you if you want the serial port hardware to be enabled: choose **Yes**.
3. Restart the Pi, e.g. by executing `sudo reboot`.

For more information regrading [see here](https://developer.here.com/blog/interacting-with-a-neo-6m-gps-module-using-golang-and-a-raspberry-pi-zero-w).