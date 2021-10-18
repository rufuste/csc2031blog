CSC2031

Open the Python Console in Pycharm.
If the Python Console is still running from a previous session it will need to be stopped and the restarted (you can use the rerun button on left side of console for this).

	At prompt enter: from models import init_db
	At Prompt enter: init_db()
	
Open Database tab on right side of PyCharm and select Refresh button.
The blog database should reload and show the newly added table posts.

Security Mechanisms
Common security mechanisms to help prevent brute force attacks are:

A strong password policy. See this (Links to an external site.) guide from the UK National Cyber Security Centre.
Notification of unrecognised login. Users are notified and asked to confirm login was genuine if a login attempt is made from an unrecognised device, location and IP address.
Comprehensive login process. We will look at adding CAPTCHA and Two Factor Authentication functionality to the user login process next.
Limiting login attempts. You will be asked to implement this functionality in the next practical session.
Biometrics. The measurement and statistical analysis of people's unique physical and behavioral characteristics. Fingerprint scanners are now common on mobile devices and some laptops.