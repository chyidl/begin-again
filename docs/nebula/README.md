# Nebula - The open source overlay Networking Tool
> Nebula is a scalable overlay networking tool with a focus on performance, simplicity and security.

* What's an overlay network?
> Put simply, an overlay network is a virtual network that runs on top of another network. A virtual Private Network (VPN) is an overlay network. A SSH tunnel is an overlay network, A SOCKS proxy is an overlay network. A Virtual Private Cloud (VPC) is an overlay network.

* Techinical Details
```
Nebula is a mutuallyi(互相) authenticated peer-to-peer software defined network based on the Noise Protocol Framework.
```

* Components of a Nebula network
    * Lighthouse
    > In Nebula, a lighthouse is a Nebula host that is responsible keeping track of all of the other Nebula hosts, and helping them find each within a Nebula network.
    * Certificate Authority
    > A Nebula Certificate Authority (CA) consists of two files, a CA certificate, and an associated private key. A CA certificate is distributed to, and trusted by, every host on the network. The CA private key should not be distributed, and can be kept offline when not being used to add hosts to a Nebula network.
    * Hosts
    > A Nebula host is simply any single node in the network, The Certificate Authority is used to sign keys for each host added to a Nebula network. A host certificate contains the name, IP address, group membership, and a number of other details about a host. 


### Quick Start
```
# How to create your first overlay network Prerequisties

```
