# ArpSpoofDetector - Detection Script
Python script for scanning ARP table entries to detect "Man in the middle" attacks.
## Table of Contents 
* [Introduction](#introduction)
* [Scope](#scope)
* [Technologies](#technologies)
* [Setup](#setup)
* [Launch](#launch)
* [Status](#status) 

## Introduction
MITM stands for "Man in the Middle" and is a type common type of attack used for stealing information in a network.
Arp spoofing is a MITM technique in which an attacker has poisoned the ARP table of its victim in order to redirect network traffic to themselves. An ARP table is list that computers store, and it maches IP addresses of other devices on the local network
to their respective MAC addresses. Attackers impersonate a devices MAC address to conduct this type of attack. This script is 
meant to run directly from the command line or terminal to detect duplicated MAC addresses, and then create a log file with the results of the detecion.

## Scope

Script is meant to scan ARP table only upon execution and produce a log file, along with the copy of the ARP table.
The script will not execute again unless manualy done so or set with cronjob/scheduled task. 

## Technologies

* Python 3.9

## Setup

Download all 3 files and save in a folder on your system: 
1. Detection.py
2. extract.py
3. logger.py

## Launch 

1. Execute the file from the cmd/terminal. 
2. You will have 2 files generated from running the script within the folder in which the python files were saved.
    i. arpfile - A copy of the ARP table from each interface on the device.
    ii. SpooLog - A log generated in the following format 
        Date Time Hostname: YOUR HOSTNAME - IP YOURIPADDRESS, Status: SYSTEM ARP STATUS

## Status 

Project is done within the context of the original scope.

However, project may be updated with additional functionality as time becomes available 

Possible avenues for improvement may include:
* Integration with specific SIEM environments. 
* Script may be run at predetermined or random intervals in conjunction with another script, until deactivated.