Blocknotif

Install this on a raspberry pi to play a sound whenever you find an ethereum block!

You can configure ethereum addresses in the config, together with a description and a wav file to play when a new block is found.
Script gets balance via etherchain.org.
On startup, raspberry will play each sound once.

Install (on raspberry):
	- apt-get update
	- apt-get install upstart python-pip
	- pip install requests
	- copy all files to /opt
	- in raspi-config -> Advances -> Audio, set to 'force 3.5mm jack'
	- plug in speaker
	- reboot