# TryHackMe [Intro to LAN](https://tryhackme.com/room/introtolan)
## Introducing LAN Topologies
### What does LAN stand for?
**Answer**: `Local Area Network`
### What is the verb given to the job that Routers perform?
* According to the information provided in the reading material:
> It's a router's job to connect networks and pass data between them. It does this by using routing (hence the name router!).

**Answer**: `Routing`
### What technology do Switches use to break large pieces of data into smaller, more manageable packets?
* According to the information provided in the reading material:
> Instead, Switches use a technology called "packet switching" to break down pieces of data into smaller, more manageable chunks of data called packets.

**Answer**: `Packet Switching`
### What topology is cost-efficient to set up?
* According to the information provided in the reading material:
> However, with this said, bus topologies are one of the easier and more cost-efficient topologies to set up because of their expenses, such as cabling or dedicated networking equipment used to connect these devices.
> ![Bus Topology](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-lan/bus.png)

**Answer**: `Bus Topology`
### What topology is expensive to set up and maintain?
* According to the information provided in the reading material:
> #### Star Topology
> Because more cabling & the purchase of dedicated networking equipment is required for this topology, it is more expensive than any of the other topologies.
> ![Star Topology](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-lan/star.png)

**Answer**: `Star Topology`
### Complete the interactive lab attached to this task. What is the flag given at the end?
**Answer**: `THM{TOPOLOGY_FLAWS}`
## A Primer on Subnetting
### What is the technical term for dividing a network up into smaller pieces?
* According to the information provided in the reading material:
> Subnetting is the term given to splitting up a network into smaller, miniature networks within itself.

**Answer**: `Subnetting`
### How many **bits** are in a subnet mask?
* According to the information provided in the reading material:
> The same goes for a subnet mask which is also represented as a number of 8 bytes (32 bits), ranging from 0 to 255 (0-255).

**Answer**: `32`
### What is the range of a section (octet) of a subnet mask?
**Answer**: `0-255`
### What address is used to identify the start of a network?
* According to the information provided in the reading material:
> Type | Purpose | Explanation | Example
> --|--|--|--
> Network Address | This address identifies the start of the actual network and is used to identify a network's existence. | For example, a device with the IP address of `192.168.1.100` will be on the network identified by `192.168.1.0`. | `192.168.1.0`

**Answer**: `Network Address`
### What address is used to identify devices within a network?
* According to the information provided in the reading material:
> Type | Purpose | Explanation | Example
> --|--|--|--
> Host Address | An IP address here is used to identify a device on the subnet. | For example, a device will have the network address of `192.168.1.10`. | `192.168.1.100`

**Answer**: `Host Address`
### What is the name used to identify the device responsible for sending data to another network?
* According to the information provided in the reading material:
> Type | Purpose | Explanation | Example
> --|--|--|--
> Default Gateway | The default gateway address is a special address assigned to a device on the network that is capable of sending information to another network. | Any data that needs to go to a device that isn't on the same network (i.e. isn't on `192.168.1.0`) will be sent to this device. These devices can use any host address but usually use either the first or last host address in a network (`.1` or `.254`) | `192.168.1.254`

**Answer**: `Default Gateway`
## The ARP Protocol
### What does ARP stand for?
* According to the information provided in the reading material:
> The **ARP** protocol or **A**ddress **R**esolution **P**rotocol for short, is the technology that is responsible for allowing devices to identify themselves on a network.

**Answer**: `Address Resolution Protocol`
### What category of ARP Packet asks a device whether or not it has a specific IP address?
* According to the information provided in the reading material:
> When an **ARP request** is sent, a message is broadcasted to every other device found on a network by the device, asking whether or not the device's MAC address matches the requested IP address.

**Answer**: `Request`
### What address is used as a physical identifier for a device on a network?
* According to the information provided in the reading material:
> Devices can use the ARP protocol to find the MAC address (and therefore the physical identifier) of a device for communication.

**Answer**: `MAC Address`
### What address is used as a logical identifier for a device on a network?
**Answer**: `IP Address`
## The DHCP Protocol
### What type of DHCP packet is used by a device to **retrieve an IP address**?
* According to the information provided in the reading material:
> When a device connects to a network, if it has not already been manually assigned an IP address, it sends out a request (DHCP Discover) to see if any DHCP servers are on the network.

**Answer**: `DHCP Discover`
### What type of DHCP packet does a device **send once it has been offered an IP address** by the DHCP server?
* According to the information provided in the reading material:
> The device then sends a reply confirming it wants the offered IP Address (DHCP Request), and then lastly, the DHCP server sends a reply acknowledging this has been completed, and the device can start using the IP Address (DHCP ACK).

**Answer**: `DHCP Request`
### Finally, **what is the last** DHCP packet that is sent to a device from a DHCP server?

**Answer**: `DHCP ACK`
