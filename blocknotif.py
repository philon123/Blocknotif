import sys
import json
import requests
import re
import time
import os

class Account(object):
	def __init__(self, name, address, soundPath):
		self.name = name
		self.address = address
		self.soundPath = soundPath
		self.numBlocks = 0

	def update(self, isStartup=False):
		newNumBlocks = self.getNumBlocks()
		if self.numBlocks < newNumBlocks and not isStartup:
			os.system('aplay ' + self.soundPath)
			print self.name + ' found block!!! New balance: ' + str(newNumBlocks)
		self.numBlocks = newNumBlocks

	def getNumBlocks(self):
		html = requests.get('http://etherchain.org/account/' + self.address).text

		#Mined Blocks: 89
		regx = re.compile('Mined Blocks: ([\d]*)')
		res = regx.search(html)
		if not res:
			raise Exception('No number of mined blocks found!')
		return res.group(1)





def getConfig():
	if len(sys.argv) == 1:
		print 'must specify a config as parameter, aborting...'
		exit()

	configUrl = sys.argv[1]
	try:
		with open(configUrl) as confFile:
			try:
				return json.loads(confFile.read())
			except ValueError:
				print 'config is not json, aborting...'
				exit()
	except IOError:
		print 'blocknotif.conf not found, aborting...'
		exit()

config = getConfig()
accts = []
for acct in config['accounts']:
	print "Adding account for " + acct['name']
	accts.append(Account(acct['name'], acct['address'], acct['wav']))

for acct in accts:
	acct.update(True)
while True:
	for acct in accts:
		acct.update()
	time.sleep(30)
