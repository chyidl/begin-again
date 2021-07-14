# Raspberry Pi

* Raspberry Pi Ubuntu enable cgroup memory at bootstrap
```
$ sudo vim /boot/firmware/cmdline.txt
net.ifnames=0 dwc_otg.lpm_enable=0 console=serial0,115200 cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1 console=tty1 root=LABEL=writable rootfstype=ext4 elevator=deadline rootwait fixrtc

There are the settings to add:
    cgroup_enable=cpuset
    cgroup_enable=memory
    cgroup_memory=1
    swapaccount=1
```
