# Educational Keylogger

## Before you proceed

This set of programs assumes the malicious actor already has direct or remote access to the target system.  Specifically the ability to manipulate the properties of a browser shortcut (usually Admin privileges).  

This repository is for whitehat education only.  Do not use this for malicious purposes, smarter people than you have been arrested for those activities.  

## Components

On target system:

- **crash_backup.exe**: The keylogger executable itself (with name disguised).  The program is converted to an .exe from .py because the  .exe includes all necesary modules and libraries (pyHook, sys, pythoncom, etc.).  This is necessary because it is highly unlikely the average user has these modules installed, or even Python.  

- **Visuals.txt**: Keylogger output (disguised).

- **launch.bat**: Batch file used to manipuate a browser shortcut into also running our keylogger.


On hacker's system:

- **keylogger_format.py**: Utility program to format and analyze keylogger output.

- **crash_backup.pyw**: Source code for keylogger.  


## Setup



## To Do

- Convert crash_backup.pyw to executable file containing all necessary modules and libraries.  We do this beause the target is very      unlikely to have pyHook, etc. installed (or even Python).  
- Exfiltration program for keylogger output.  


## Known Errors

- Changing the Target of a browser shortcut also changes the thumbnail to be that of a batch file rather than the browser thumbnail.


## Future Additions & Theories

Most people have important URLs saved as bookmarks in their browser.  In addition to being convenient, this also protects the user from   phishing attacks that rely on the victim clicking a spoofed URL.  Bookmarks also hinder keylogging schemes by removing context from       captured usernames and passwords.  If a user searches for "facebook" then enters credentials, the log output shows this information in     sequence - if the user clicks a bookmark then enters credentials, all we have is a click event followed by credentials.

Lucky for us, mouse events can also be tracked by pyHook.  The MouseEvent class has instance variable Position, which returns the screen coordinates of the event.  If we combined this data with a screenshot of the target's browser, we could determine whether the click lines up with the autentication page of an interesting site.    


## Additional Info

pyHook
http://pyhook.sourceforge.net/doc_1.5.0/ 

py2exe
http://www.py2exe.org/index.cgi/FrontPage
