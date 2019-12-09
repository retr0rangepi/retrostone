# A20 dual core 1Gb SoC
BOARD_NAME="Retrostone 2"
BOARDFAMILY="sun7i"
BOOTCONFIG="A20-Retrostone2_defconfig"
#
MODULES="hci_uart gpio_sunxi rfcomm hidp bonding spi_sun7i 8021q a20_tp"
MODULES_NEXT="bonding brcmfmac uinput"
#
KERNEL_TARGET="default,next,dev,current"
CLI_TARGET="buster,bionic:next"
DESKTOP_TARGET="xenial:default"
#
CLI_BETA_TARGET=""
