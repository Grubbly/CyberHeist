# CyberHeist
Grabber lab for CSC Fall 2019

[Sick AF programming mix](https://www.youtube.com/watch?v=XrisCsNzOlo)
## Description 
Individuals are tasked with breaking into some form of container said to hold something of particular value. There are four levels to this lab:

## Levels
**1. Beginner**: Simple Python script is distributed. Members must read the source code in order to figure out the flag. This flag contains login credentials, which are used for the levels below.

**2. Intermediate**: Members are given a Linux VM and must scan the network to determine a raspberry pi with SSH is running. Using the credentials obtained in the first level, they are able to login to the pi. Running ls will reveal a secret file which they will cat to reveal a clue that suggests the Pi is running a web server that controls a physical safe.

**3. Advanced**: After visiting the site, members will notice a video live stream. The camera will be facing away from another secret message. Members need to figure out how to move the camera in order to view the secret message. The message will be a path to a script for opening the physical safe.

**4. Extra**: Inside the safe will be a small box with a lockpickable lock on it. Members need to utilize a provided lock pick set to retrieve the grand prize.

## Notes
Level 1 Credentials:
* Username: Grubsy
* Password: yakisobanoodles
  * SHA256 hash
