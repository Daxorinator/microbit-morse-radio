from microbit import *
import radio

radio.on()

radio.config(length=64, queue=1, channel=5, power=7, data_rate=radio.RATE_1MBIT)

dot_image = Image("00000:"
			 	  "08880:"
			 	  "08880:"
			 	  "08880:"
			 	  "00000:")

dash_image = Image("00000:"
			  	   "00000:"
			  	   "88888:"
			  	   "00000:"
			  	   "00000:")

while True:
	if button_a.was_pressed():
		radio.send("DOT")
	elif button_b.was_pressed():
		radio.send("DASH")
	else:
		data = radio.receive()
		if data == 'DOT':
			display.show(dot_image)
			sleep(200)
			display.clear()
		elif data == 'DASH':
			display.show(dash_image)
			sleep(200)
			display.clear()