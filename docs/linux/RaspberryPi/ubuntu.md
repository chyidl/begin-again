# Ubuntu


* [Bluetooth on Ubuntu 20.04](#bluetooth_ubuntu)


bluetooth_ubuntu
----------------
```
Install the pi-bluetooth package:
$ sudo apt-get install pi-bluetooth

Edit the /boot/firmware/usercfg.txt file to add the following line at the end
include btcfg.txt

Roboot
$ sudo roboot

Check that the device is detected
➜ hcitool dev
Devices:
	hci0	DC:A6:32:41:23:FB

➜ hciconfig -a
hci0:	Type: Primary  Bus: UART
	BD Address: DC:A6:32:41:23:FB  ACL MTU: 1021:8  SCO MTU: 64:1
	UP RUNNING
	RX bytes:1808 acl:0 sco:0 events:95 errors:0
	TX bytes:2570 acl:0 sco:0 commands:95 errors:0
	Features: 0xbf 0xfe 0xcf 0xfe 0xdb 0xff 0x7b 0x87
	Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3
	Link policy: RSWITCH SNIFF
	Link mode: SLAVE ACCEPT
	Name: 'RPi4B'
	Class: 0x000000
	Service Classes: Unspecified
	Device Class: Miscellaneous,
	HCI Version: 5.0 (0x9)  Revision: 0x156
	LMP Version: 5.0 (0x9)  Subversion: 0x6119
	Manufacturer: Cypress Semiconductor Corporation (305)
```
