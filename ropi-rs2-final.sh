#!/bin/bash
clear

TERM=linux toilet -f standard -F metal "RetrOrangePi"
TERM=linux toilet -f standard -F metal "Retrostone 2"

#    RetrOrangePi BashWelcomeTweak

echo -e "       \033[0;32m█              █\033[0m     "
echo -e "  \033[0;33m█\033[0m     \033[0;32m█            █\033[0m     \033[0;33m█"
echo -e "\033[0;33m  █  ████████████████████  █"
echo -e "\033[0;33m  ███████\033[1;37m██\033[0;33m████████\033[1;37m██\033[0;33m███████"
echo -e "\033[0;33m  ██████████████████████████"
echo -e "\033[0;33m    ██████████████████████ "
echo -e "\033[0;33m     ████████████████████  "
echo -e "\033[0;33m        █             █   "
echo -e "\033[0;33m       █               █  "
echo ""
echo ""
echo "*****************************************************************"
echo "*                                                               *"
echo "*                     Testing Retrostone 2                      *"
echo "*                                                               *"
echo "*****************************************************************"
echo ""
read -p "Press Enter to continue..." -e
echo ""
echo "*****************************************************************"
echo "*                                                               *"
echo "*                    Testing Wifi/Bluetooth                     *"
echo "*                                                               *"
echo "*****************************************************************"
echo ""
read -p "Press Enter to test network..." -e
ifconfig eth0
ifconfig wlan0
echo "Please check network interfaces"
echo ""
echo ""
echo "eth0 = Ethernet"
echo "wlan0 = Wifi"
echo ""
echo ""
echo "IP's assigned should be next to inet x.x.x.x"
echo ""
echo ""
read -p "Press Enter to test bluetooth..." -e
hciconfig
echo ""
echo ""
echo "You should see an hci0 interface"
echo ""
echo ""
read -p "Press Enter to test audio. Make sure to turn the sound wheel ON"
echo ""
echo "*****************************************************************"
echo "*                                                               *"
echo "*                         Testing Audio                         *"
echo "*                                                               *"
echo "*****************************************************************"
echo ""
mpv /home/pi/RetroPie/splashscreens/bootsnd.ogg
echo "*****************************************************************"
echo "*                                                               *"
echo "*                       Checking Storage                        *"
echo "*                                                               *"
echo "*****************************************************************"
echo ""
read -p "Now we'll check storage. Press Enter when ready"
lsblk
echo "Please check if all storage devices are present"
echo ""
echo ""
echo "/dev/mmcblk0p1 - eMMC"
echo "/dev/mmcblk1p1 - SD"
echo "/dev/sda - External SSD"
echo ""
read -p "Press Enter now to test buttons. Each press will return onscreen."
sudo python /home/pi/e.py

