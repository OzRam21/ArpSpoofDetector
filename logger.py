"""
<Function 3: Logging>

Author: Osiel Ramirez
Authored on: 12/22/2020

1. Receive a message from the 2nd function.
2. Create a log file with the message, date, and timestamp

"""

from datetime import datetime
# import datetime to make a time stamp.
import platform
# imported platform to get the name of the host.
import socket
# import socket to get the host IP address.
def logs(message):
    # Take in the status message as a string variable.
    timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Store the current timestamp in a formatted manner (2020-12-22 23:22:00),
    # into the timeStamp variable.
    host = platform.node()
    # Store the host name into the host variable.
    ip = socket.gethostbyname(host)
    # Store the host IP address in the ip variable.
    with open("SpoofLog.txt", "a") as logfile:
        logfile.write("\n{} - Hostname: {} - IP {}, {}".format(timeStamp,host,ip,message))
        # Open or create a spooflog file and append log to it.
        # The log is formatted for easy of use with a SIEM.