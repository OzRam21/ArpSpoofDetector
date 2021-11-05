"""
<Function 2: Duplication Check>

Author: Osiel Ramirez
Authored on: 12/22/2020

1. Receive the dictionary from the 1st function.
2. Check if the dictionary value [Mac address] exists more than once.
3. If a duplication is found, print that machine is being ARP spoofed
4. Exit elegantly without fail.

"""
import extract
import logger
# import the other functions from the thier respective
# files.
spacer = "----------------------------------------------------------------------"
# Spacer is to clean up the look of thr output.
def spoofDetect(arpTable):
    macList = list(arpTable.values())
    # Convert the received into a list with only the mac-addresses.
    detectList = []
    # Instantiate the empty list that will be used to detect duplications.
    for item in macList:
        # Each element from macList will be iterated through.
        if item in detectList:
            # Here the item from the macList will be compared to the detectList
            # to check for duplicates
            print("Status: ATTACK DETECTED - ARP SPOOF <MAC: {}>".format(item))
            logger.logs("Status: ATTACK DETECTED - ARP SPOOF <MAC: {}>".format(item))
            break
            # Lines 29-31 print the detected attack to the console and send a copy
            # to the log file via the logger.log function.
        else:
            detectList.append(item)
            # If an item is not duplicated, it adds it to the detectList.
    if len(macList) == len(detectList):
        # If the the 2 lists are equal in length, it signals that
        # the arp table is completely scanned.
        print(spacer)
        print("Status: SYSTEM SECURE - ARP SAFE")
        print(spacer)
        logger.logs("Status: SYSTEM SECURE - ARP SAFE")
        # When there are no duplicated MACs detected after running
        # through the entire macList address, print and log that
        # the system is secure.

if __name__ == '__main__':
    spoofDetect(extract.arpExtract())
    # Magic main is used here to force the code to be executed from this file.
    # SpoofDetect function is called with the arpExtract method as an arguent.