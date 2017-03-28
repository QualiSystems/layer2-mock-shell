# Layer 2 mock shell
Layer 2 mock shell is a CloudShell package that contains a L2 Switch and DUT resources & a L2 Driver that supports the new CloudShell 7.0 connectivity standardization. This "mock" shell simulates the behavior of an L2 within a 7.0 environment and can be used for testing and orchestration development.
Note that this shell fits the Networking Shell Standard but only the ApplyConnectivityChanges command is implemented (as a mock).

### Installation
Import the Shell into CloudShell

### what's in the shell
* L2 switch physicly connected to DUT
* L2 driver with the new connectivity interface
* Note: only the "ApplyConnectivitychanges" method is implemented as a mock connectivity service

###### L2 & DUT physical connections
![Alt text](Pics/Connection.png?raw=true)

###### Connect a DUT connected to VLAN service
![Alt text](Pics/VLANnDUT.png?raw=true)

###### L2 switch commands
![Alt text](Pics/L2.png?raw=true)

Enjoy :-)
