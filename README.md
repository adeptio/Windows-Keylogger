# Educational Keylogger

## Before you proceed

This set of programs assumes the malicious actor already has direct or remote access to the target system.  Specifically the ability to manipulate the properties of a browser shortcut (usually Admin privileges).  

## Components

On target system:

- crash_backup.pyw: The keylogger itself (with name disguised).

- Visuals.txt: Keylogger output (disguised).

- launch.bat: Batch file used to manipuate a browser shortcut into also running our keylogger.


On hacker's system:

- keylogger_format.py: Utility program to format and analyze keylogger output.



## Setup



## Known Errors


## Future Additions & Theories

Most people have important URLs saved as bookmarks in their browser.  In addition to being convenient, this also protects the user from   phishing attacks that rely on the victim clicking a spoofed URL.  Bookmarks also hinder keylogging schemes by removing context from       captured usernames and passwords.  If a user searches for "facebook" then enters credentials, the log output shows this information in     sequence - if the user clicks a bookmark then enters credentials, all we have is a click event followed by credentials.

Lucky for us, mouse events can also be tracked by pyHook.  The MouseEvent class has instance variable Position, which returns the screen coordinates of the event.  If we combined this data with a screenshot of the target's browser, we could determine whether the click lines up with the autentication page of an interesting site.    

pyHook documentation:
http://pyhook.sourceforge.net/doc_1.5.0/ 
