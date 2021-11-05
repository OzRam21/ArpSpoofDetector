"""
<Function 1: ARP table extraction>

Author: Osiel Ramirez
Authored on: 12/22/2020

1. Detect the OS that ran the script.
2. Execute the OS specific command to display the ARP table.
3. Print each line of the ARP table

"""
import platform
import os
import re
# Import the re module to use regex expressions.
spacer = "----------------------------------------------------------------------"

def arpExtract():
    try:
        print(spacer)
        print("Welcome to the ARP Spoof Detection tool!")
        osType = platform.system()
        print("<OS Detected: {}>\nPrinting ARP Table... ".format(osType))
        print(spacer)
        arpDict = {}
        # Lines 15 - 18 print the welcome message, detect the OS, print
        # the information, then instantiate a dictionary.
        # The dictionary will store the filtered output that will be fed
        # into the 2nd function.
        if osType == "Windows":
            os.system(r"arp -a > arpFile.txt")
            with open("arpFile.txt", "r") as file:
                # Lines 23 - 25 check if the OS is windows, then execute the ARP
                # command via the cmd and store the output into a text file.
                data = file.read()
                # The data variable will receive the contents of the file created above
                # in order to be used for filtering.
                print(data)
                # Line 31 prints the raw ARP table from the command.
                for line in re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([-0-9a-f]{17})\s+(\w+)',data):
                    # Line 33 uses the findall method to filter out irrelevant lines in the
                    # raw ARP table with a regex expression on each iteration. A tuple is the output.
                    if line[1] == 'ff-ff-ff-ff-ff-ff':
                        # Line 36 filters out any broadcast address
                        continue
                        # Line 38 skips to the next iteration.
                    else:
                        arpDict[line[0]] = line[1]
                        # Line 41 adds the tuple values into the dictionary as a {IP:mac} pair.
            return arpDict
            # Line 43 returns the filtered arp table as a dictionary.
        elif osType == "Darwin":
            # Darwin is what is detected on a MAC computer.
            os.system(r"arp -a >> arpFile.txt")
            with open("arpFile.txt", "r") as file:
                data = file.read()
                print(data)
                for line in re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([:0-9a-f]{17})\s+(\w+)',data):
                    if line[1] == 'ff:ff:ff:ff:ff:ff':
                        # Both MAC and Linux output the Mac address with the : delimiter, Line 50 and 62
                        # are also changed to detect this difference from the Windows OS.
                        continue
                    else:
                        arpDict[line[0]] = line[1]
            return arpDict
        elif osType == "Linux":
            os.system(r"arp >> arpFile.txt")
            with open("arpFile.txt", "r") as file:
                data = file.read()
                print(data)
                for line in re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([:0-9a-f]{17})\s+(\w+)',data):
                    if line[1] == 'ff:ff:ff:ff:ff:ff':
                        continue
                    else:
                        arpDict[line[0]] = line[1]
            return arpDict
        else:
            print("The OS is not recognized or compatible!")
            # Line 71 will respond if the OS system is not one of the 3 OSs
    except:
        print("Error: Unexpected Error occurred!")
    # Catch any unexpected errors.