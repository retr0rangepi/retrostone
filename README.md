# Retrostone 2 - RetrOrangePi customization

* armbian-firstrun - enables Mali out-of-the-tree module and Bluetooth service : /usr/lib/armbian
*	btpatch.tar.gz - Broadcom utility to flash Bluetooth firmwares - must be extracted to /
*	e.py - Python script for controller buttons testing
*	gpio_retrostone2-production-with-brightness.py - Enables the Retrostone GPIO controls - /home/pi/RetrOrangePi/GPIO/drivers/tz_gpio_controller.py
*	joystick.rules - UDEV rule to give write privileges to input : /etc/udev/rules.d/ (not tested yet)
* kernel-sunxi-current.patch - Armbian kernel patch (v5.3.13)
*	retroarch.cfg - Retroarch configuration file: /opt/retropie/configs/all/
*	RetroStone2 Controle.cfg - Controller configuration file: /opt/retropie/configs/all/retroarch/autoconfig/
*	retrostone2.csc - Armbian Retrostone 2 configuration - adds board to Armbian building script: build/config/boards
*	ropi-rs2-final.sh - simple test script (network, bluetooth, storage, audio and controls)
*	RS2GPIO.tar.gz - GPIO sources - /home/pi/RetrOrangePi/GPIO/
*	SDL_gamecontrollerdb.h - add support to Retrostone controller in SDL2 sources
*	sun7i-a20-retrostone2.dts - adds Retrostone DTS with backlight/LCD support
*	u-boot-sunxi-current.patch - Armbian u-boot patch
