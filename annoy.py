#!/usr/bin/python

import pibrella
import time
import random
import thread
import threading
import sys
import os

#PAUSE=random.uniform(1, 5)#*60
#TONE=random.randint(0,256)
#LENGTH=random.uniform(0.25, 1.0)
#TIMESTAMP=time.asctime(time.localtime(time.time()))

time.sleep(random.uniform(2, 5)*60)

SCRIPTNAME=os.path.basename(__file__)
PID=str(os.getpid())
FILENAME="/tmp/" + SCRIPTNAME + "." + PID + "."
FILENAME+=''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))

def beep():
	while carry_on():
		PAUSE=random.uniform(1, 5)*60
		TONE=random.randint(0,256)
		LENGTH=random.uniform(0.25, 1.0)
		TIMESTAMP=time.asctime(time.localtime(time.time()))
		
		#pibrella.light.green.on()

		print "%s" % TIMESTAMP
		#print "%s" % time.asctime(time.localtime(time.time()))
		print "Tone: %d" % TONE
		print "Length: %f" % LENGTH
		print "Pause: %f" % PAUSE
		print ""
		
		pibrella.light.red.on()
		pibrella.buzzer.note(TONE)
		time.sleep(LENGTH)
		pibrella.buzzer.off()
		pibrella.light.red.off()
		pibrella.light.yellow.on()
		time.sleep(PAUSE)
		pibrella.light.yellow.off()


def file_check():
	#SCRIPTNAME=os.path.basename(__file__)
	#PID=str(os.getpid())
	#FILENAME="/tmp/" + SCRIPTNAME + "." + PID
	#print "%s" % FILENAME
	
	#Does the file exist?
	if not os.path.isfile(FILENAME):
		#print "File does NOT Exist!"
		file = open(FILENAME, "w")
		file.write(str(True)+"\n")
		file.close()


def carry_on():
	file_check()
	if os.path.isfile(FILENAME):
			file = open(FILENAME, "r")
			CONTENT=file.readline()
			file.close()
			#print "%s" % CONTENT
			if (CONTENT=="True\n"):
				return True
			else:
				return False

def button_changed(pin):
    if pin.read() == 1:
        #print("You pressed the button!")
		file_check()
		file = open(FILENAME, "w")
		file.write(time.asctime(time.localtime(time.time()))+"\n")
		file.close()
		pibrella.light.green.off()
		pibrella.light.red.off()
		pibrella.light.yellow.off()
		os.system("sudo shutdown now")


## MAIN START
pibrella.light.green.on()
file_check()

threads = []

t = threading.Thread(target=beep)
threads.append(t)

try:
	#thread.start_new_thread(beep,())
	#time.sleep(1)
	for t in threads:
		t.start()
except:
	#print "Error:"
	e = sys.exc_info()[0]
	print "Error: %s" % e	

pibrella.button.changed(button_changed)

for t in threads:
	t.join()

#os.remove(FILENAME)
pibrella.light.green.off()
os.system("sudo shutdown now")
