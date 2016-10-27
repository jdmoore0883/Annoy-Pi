#Annoy-Pi

This script, when combined with a RaspberryPi and a Pibrella, is the perfect way to make someone crazy. Unlike other Anny-a-tron's out there where the beep is the same tone after a same amount of time (usually 1 minute or so), this produces a random tone after a random amount of time, making it very difficult to identify and locate. This will continue until either the script is stopped, or the Pibrella button is pressed. Pressing the button will stop the script and shutdown the RasPi, allowing it to be unplugged and removed.

It works by using the buzzer included in the Pibrella.

What it does:
* Upon start, it waits between 2 to 5 minutes
	- (If you set it to start on boot in a cron job, this gives you time to plug it in and run off before it starts)
* Once going, it will beep a random tone, 0.25 to 1 second in length
* It will then sleep for 1 to 5 minutes before beeping again
* This will continue until one of the following:
	* The Pibrella button is pressed 
		- This will initiate a shutdown to allow the Pi to be unplugged and removed
	* The script is manually stopped
	* The Pi is shutdown or otherwise powered off

