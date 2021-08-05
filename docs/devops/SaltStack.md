# SaltStack
> The Salt Prokect is an approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.


## Getting Started
> The backbone of Salt is the remote executing engine, which creates a high-speed, secure and bi-directional communication net for groups of systems. On top of this comminication system, Salt provides an extremely fast, flexible, and easy-to-user configuration management system called Salt States.
```
# Salt Bootstrap
> The Salt Bootstrap Script allows install the Salt Minion or Master on a variety of system distributions and versions.
$ wget -O bootstrap-salt.sh https://bootstrap.saltproject.io
➜ sudo sh bootstrap-salt.sh -M -x python3
 *  INFO: Running version: 2021.06.23
 *  INFO: Executed by: shell pipe
 *  INFO: Command line: 'bootstrap-salt.sh -M -x python3'
 *  INFO: Detected -x option. Using python3 to install Salt.

 *  INFO: System Information:
 *  INFO:   CPU:          GenuineIntel
 *  INFO:   CPU Arch:     x86_64
 *  INFO:   OS Name:      Linux
 *  INFO:   OS Version:   5.10.0-0.bpo.7-rt-amd64
 *  INFO:   Distribution: Debian 10

# Salt Master

# Salt minion (on each system that you want to manage using Salt)

```
