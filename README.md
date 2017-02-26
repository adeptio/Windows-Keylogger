# Educational Keylogger for Windows

## Before you proceed

This set of programs assumes the malicious actor already has direct or remote access to the target system.  Specifically the ability to manipulate the properties of a browser shortcut (usually Admin privileges).  

This repository is for whitehat education only.  Do not use this for malicious purposes, smarter people than you have been arrested for those activities.  

## Components

On target system:

- **crash_backup.exe**: The keylogger executable itself (with name disguised).  The program is converted to an .exe from .py because the  .exe includes all necesary modules and libraries (pyHook, sys, pythoncom, etc.).  This is necessary because it is highly unlikely the average user has these modules installed, or even Python.  Follow py2exe link below and complete tutorial for this.  

- **Visuals.txt**: Keylogger output (disguised).

- **launch.bat**: Batch file used to manipuate a browser shortcut to also run our keylogger.


On hacker's system:

- **keylogger_format.py**: Utility program to format and perform rough analysis on keylogger output.

- **crash_backup.pyw**: Source code for keylogger.  


## Setup

On target system:

1). Achieve administrator privileges (not covered here).  This is where the art of pentesting comes in.    

2). Upload crash_backup.exe, Visuals.txt, and launch.bat - create a folder to house these files.  Ex: C:\Config\Visuals.txt, C:\Config\crash_backup.exe, C:\Config\launch.bat.

3). Find a "high use" desktop shortcut, like a browser.  Right click the shortcut, then click properties.  Change the address in the Target field to be that of launch.bat.  When this shortcut is used, it will also start our keylogger.

Also do this for the equivalent taskbar/toolbar icon if it exists: right click the icon, then right click the application name in the jump list and click Properties.  Change the Target field in the same way as above.  

4). Exfiltrate the data (coming soon).


## To Do

- SQLite for log data.
- Exfiltration program for keylogger output.
- More ways to run the keylogger.    
- Infiltration program for keylogger code if remote access to target system is being used.  


## Known Errors

- Changing the Target of a browser shortcut also changes the thumbnail to be that of a batch file rather than the browser thumbnail.


## Future Features & Theories

Most people have important URLs saved as bookmarks in their browser.  In addition to being convenient, this also protects the user from   phishing attacks that rely on the victim clicking a spoofed URL.  Bookmarks also hinder keylogging schemes by removing context from       captured usernames and passwords.  If a user searches for "facebook" then enters credentials, the log output shows this information in     sequence - if the user clicks a bookmark then enters credentials, all we have is a click event followed by credentials.

Lucky for us, mouse events can also be tracked by pyHook.  The MouseEvent class has instance variable Position, which returns the monitor coordinates of the event.  If we combine this data with a screenshot of the target's browser, we can determine whether the click lines up with a bookmark to the autentication page of an interesting site.    


## Additional Info

pyHook
http://pyhook.sourceforge.net/doc_1.5.0/ 

py2exe
http://www.py2exe.org/index.cgi/FrontPage
