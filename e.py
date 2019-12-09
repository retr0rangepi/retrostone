#!/usr/bin/env python

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector



#--------------- define botoes -----------------
	# ---- PLAYER 1 ---------#
bt_up_p1 = port.PH19
bt_down_p1 = port.PH7
bt_left_p1 = port.PH4
bt_right_p1 = port.PH16

bt_l_p1 = port.PH23
bt_x_p1 = port.PH12
bt_y_p1 = port.PH20
bt_r_p1 = port.PH22
bt_b_p1 = port.PH11
bt_a_p1 = port.PH0

bt_select_p1 = port.PH15
bt_start_p1 = port.PH14

bt_left_trigger_p1 = port.PH27
bt_right_trigger_p1 = port.PH26

#optional buttons
bt_c_p1 = port.PC18
bt_z_p1 = port.PC22



#--------------------------------Initialize module. Always called first
gpio.init()

gpio.setcfg(bt_up_p1, gpio.INPUT)
gpio.pullup(bt_up_p1, gpio.PULLUP)

gpio.setcfg(bt_down_p1, gpio.INPUT)
gpio.pullup(bt_down_p1, gpio.PULLUP)

gpio.setcfg(bt_left_p1, gpio.INPUT)
gpio.pullup(bt_left_p1, gpio.PULLUP)

gpio.setcfg(bt_right_p1, gpio.INPUT)
gpio.pullup(bt_right_p1, gpio.PULLUP)


gpio.setcfg(bt_l_p1, gpio.INPUT)
gpio.pullup(bt_l_p1, gpio.PULLUP)

gpio.setcfg(bt_x_p1, gpio.INPUT)
gpio.pullup(bt_x_p1, gpio.PULLUP)

gpio.setcfg(bt_y_p1, gpio.INPUT)
gpio.pullup(bt_y_p1, gpio.PULLUP)

gpio.setcfg(bt_r_p1, gpio.INPUT)
gpio.pullup(bt_r_p1, gpio.PULLUP)

gpio.setcfg(bt_b_p1, gpio.INPUT)
gpio.pullup(bt_b_p1, gpio.PULLUP)

gpio.setcfg(bt_a_p1, gpio.INPUT)
gpio.pullup(bt_a_p1, gpio.PULLUP)

gpio.setcfg(bt_c_p1, gpio.INPUT)
gpio.pullup(bt_c_p1, gpio.PULLUP)

gpio.setcfg(bt_z_p1, gpio.INPUT)
gpio.pullup(bt_z_p1, gpio.PULLUP)

gpio.setcfg(bt_select_p1, gpio.INPUT)
gpio.pullup(bt_select_p1, gpio.PULLUP)

gpio.setcfg(bt_start_p1, gpio.INPUT)
gpio.pullup(bt_start_p1, gpio.PULLUP)

gpio.setcfg(bt_left_trigger_p1, gpio.INPUT)
gpio.pullup(bt_left_trigger_p1, gpio.PULLUP)

gpio.setcfg(bt_right_trigger_p1, gpio.INPUT)
gpio.pullup(bt_right_trigger_p1, gpio.PULLUP)

	
_bt_up_p1 = False
_bt_down_p1 = False
_bt_left_p1 = False
_bt_right_p1 = False
_bt_a_p1 = False
_bt_b_p1 = False
_bt_x_p1 = False
_bt_y_p1 = False
_bt_c_p1 = False
_bt_z_p1 = False
_bt_d_p1 = False
_bt_e_p1 = False
_bt_l_p1 = False
_bt_r_p1 = False
_bt_select_p1 = False
_bt_start_p1 = False
_bt_left_trigger_p1 = False
_bt_right_trigger_p1 = False

exit = True


while exit:
	#------ player 1 -----------#		
#bt a =====================
	if (not _bt_a_p1) and (gpio.input(bt_a_p1) == 0):
		_bt_a_p1 = True
		print("A                 (press UP+R1 to exit)")	
	if (_bt_a_p1) and (gpio.input(bt_a_p1) == 1):
		_bt_a_p1 = False
		print("A unclicked                 (press UP+R1 to exit)")
			
#bt b =====================

	if (not _bt_b_p1) and (gpio.input(bt_b_p1) == 0):
		_bt_b_p1 = True
		print("B                 press UP+R1 to exit")	
	if (_bt_b_p1) and (gpio.input(bt_b_p1) == 1):
		_bt_b_p1 = False
		print("B unclicked                 (press UP+R1 to exit)")
			

#bt X =====================

	if (not _bt_x_p1) and (gpio.input(bt_x_p1) == 0):
		_bt_x_p1 = True
		print("X                 press UP+R1 to exit")	
	if (_bt_x_p1) and (gpio.input(bt_x_p1) == 1):
		_bt_x_p1 = False
		print("X unclicked                 (press UP+R1 to exit)")	
#bt Y =====================

	if (not _bt_y_p1) and (gpio.input(bt_y_p1) == 0):
		_bt_y_p1 = True
		print("Y                 press UP+R1 to exit")	
	if (_bt_y_p1) and (gpio.input(bt_y_p1) == 1):
		_bt_y_p1 = False
		print("Y unclicked                 (press UP+R1 to exit)")	

#bt C =====================

	if (not _bt_c_p1) and (gpio.input(bt_c_p1) == 0):
		_bt_c_p1 = True
		print("PC18-BrightnessUp                 (press UP+R1 to exit)")	
	if (_bt_c_p1) and (gpio.input(bt_c_p1) == 1):
		_bt_c_p1 = False
		print("PC18-BrightnessUp unclicked                 (press UP+R1 to exit)")
		
#bt C =====================

	if (not _bt_z_p1) and (gpio.input(bt_z_p1) == 0):
		_bt_z_p1 = True
		print("PC22-BrightnessDown                 (press UP+R1 to exit)")	
	if (_bt_z_p1) and (gpio.input(bt_z_p1) == 1):
		_bt_z_p1 = False
		print("PC22-BrightnessDown unclicked                 (press UP+R1 to exit)")
		
#bt L =====================
	if (not _bt_l_p1) and (gpio.input(bt_l_p1) == 0):
		_bt_l_p1 = True
		print("L                 (press UP+R1 to exit)")
	if (_bt_l_p1) and (gpio.input(bt_l_p1) == 1):
		_bt_l_p1 = False
		print("L unclicked                 (press UP+R1 to exit)")
#bt R =====================
	if (not _bt_r_p1) and (gpio.input(bt_r_p1) == 0):
		_bt_r_p1 = True
		print("R                 (press UP+R1 to exit)")
	if (_bt_r_p1) and (gpio.input(bt_r_p1) == 1):
		_bt_r_p1 = False
		print("R unclicked                 (press UP+R1 to exit)")
#bt select =====================
	if (not _bt_select_p1) and (gpio.input(bt_select_p1) == 0):
		_bt_select_p1 = True
		print("select                 (press UP+R1 to exit)")
	if (_bt_select_p1) and (gpio.input(bt_select_p1) == 1):
		_bt_select_p1 = False
		print("select unclicked                 (press UP+R1 to exit)")
#bt start =====================
	if (not _bt_start_p1) and (gpio.input(bt_start_p1) == 0):
		_bt_start_p1 = True
		print("start                 (press UP+R1 to exit)")
	if (_bt_start_p1) and (gpio.input(bt_start_p1) == 1):
		_bt_start_p1 = False
		print("start unclicked                 (press UP+R1 to exit)")
#bt L2 =====================
	if (not _bt_left_trigger_p1) and (gpio.input(bt_left_trigger_p1) == 0):
		_bt_left_trigger_p1 = True
		print("L2                 (press UP+R1 to exit)")
	if (_bt_left_trigger_p1) and (gpio.input(bt_left_trigger_p1) == 1):
		_bt_left_trigger_p1 = False
		print("L2 unclicked                 (press UP+R1 to exit)")
#bt R2 =====================
	if (not _bt_right_trigger_p1) and (gpio.input(bt_right_trigger_p1) == 0):
		_bt_right_trigger_p1 = True
		print("R2                 (press UP+R1 to exit)")
	if (_bt_right_trigger_p1) and (gpio.input(bt_right_trigger_p1) == 1):
		_bt_right_trigger_p1 = False
		print("R2 unclicked                 (press UP+R1 to exit)")
####DIRECTIONS P1 ###########################

#bt up =====================
	if (not _bt_up_p1) and (gpio.input(bt_up_p1) == 0):
		_bt_up_p1 = True
		print("up                 (press UP+R1 to exit)")
	if (_bt_up_p1) and (gpio.input(bt_up_p1) == 1):
		_bt_up_p1 = False
		print("up unclicked                 (press UP+R1 to exit)")
#bt down =====================
	if (not _bt_down_p1) and (gpio.input(bt_down_p1) == 0):
		_bt_down_p1 = True
		print("down                 (press UP+R1 to exit)")
	if (_bt_down_p1) and (gpio.input(bt_down_p1) == 1):
		_bt_down_p1 = False
		print("down unclicked                 (press UP+R1 to exit)")
#bt left =====================
	if (not _bt_left_p1) and (gpio.input(bt_left_p1) == 0):
		_bt_left_p1 = True
		print("left                 (press UP+R1 to exit)")
	if (_bt_left_p1) and (gpio.input(bt_left_p1) == 1):
		_bt_left_p1 = False
		print("left unclicked                 (press UP+R1 to exit)")
#bt right =====================
	if (not _bt_right_p1) and (gpio.input(bt_right_p1) == 0):
		_bt_right_p1 = True
		print("right                 (press UP+R1 to exit)")
	if (_bt_right_p1) and (gpio.input(bt_right_p1) == 1):
		_bt_right_p1 = False
		print("right unclicked                 (press UP+R1 to exit)")
		
	if (_bt_right_trigger_p1) and (_bt_up_p1):
		exit = False
	
	sleep(.02)