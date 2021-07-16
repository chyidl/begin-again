# Linux

### Install a newer kernel in Debian 10 (Buster) stable
* the benefits of upgrading kernel
    * Support for previously unsupported hardware
    * Performance improvements and bug fixes
    * New kernel optoons and security fixes

[Install a newer kernel in Debian 10 (buster) stable](https://jensd.be/968/linux/install-a-newer-kernel-in-debian-10-buster-stable)

```
chyi in openmediavault in ~ via 🐍 v3.8.6
❯ cat /etc/debian_version
10.10

chyi in openmediavault in ~ via 🐍 v3.8.6
❯ uname -r
4.19.0-17-amd64

# Installing a newer kernel in Debian Buster
> The easiest way to install a newer kernel in Debian, is to install it from the backports. Backports are packages taken from the next Debian release, adjusted and recompiled for usage on the stable release.

add the backports-repository for your Debian version
$ sudo vim /etc/apt/sources.list
    deb http://deb.debian.org/debian buster-backports main
$ sudo apt-get update
$ sudo apt-get install aptitude

# search for all available
chyi in openmediavault in ~ via 🐍 v3.8.6
❯ aptitude search linux-image
p   linux-image-4.19.0-12-amd64                                                      - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-12-cloud-amd64                                                - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-12-rt-amd64                                                   - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
c   linux-image-4.19.0-14-amd64                                                      - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-14-amd64-dbg                                                  - Debug symbols for linux-image-4.19.0-14-amd64
p   linux-image-4.19.0-14-amd64-unsigned                                             - Linux 4.19 for 64-bit PCs
p   linux-image-4.19.0-14-cloud-amd64                                                - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-14-cloud-amd64-dbg                                            - Debug symbols for linux-image-4.19.0-14-cloud-amd64
p   linux-image-4.19.0-14-cloud-amd64-unsigned                                       - Linux 4.19 for x86-64 cloud
p   linux-image-4.19.0-14-rt-amd64                                                   - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-4.19.0-14-rt-amd64-dbg                                               - Debug symbols for linux-image-4.19.0-14-rt-amd64
p   linux-image-4.19.0-14-rt-amd64-unsigned                                          - Linux 4.19 for 64-bit PCs, PREEMPT_RT
i A linux-image-4.19.0-16-amd64                                                      - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-16-amd64-dbg                                                  - Debug symbols for linux-image-4.19.0-16-amd64
p   linux-image-4.19.0-16-amd64-unsigned                                             - Linux 4.19 for 64-bit PCs
p   linux-image-4.19.0-16-cloud-amd64                                                - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-16-cloud-amd64-dbg                                            - Debug symbols for linux-image-4.19.0-16-cloud-amd64
p   linux-image-4.19.0-16-cloud-amd64-unsigned                                       - Linux 4.19 for x86-64 cloud
p   linux-image-4.19.0-16-rt-amd64                                                   - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-4.19.0-16-rt-amd64-dbg                                               - Debug symbols for linux-image-4.19.0-16-rt-amd64
p   linux-image-4.19.0-16-rt-amd64-unsigned                                          - Linux 4.19 for 64-bit PCs, PREEMPT_RT
i A linux-image-4.19.0-17-amd64                                                      - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-17-amd64-dbg                                                  - Debug symbols for linux-image-4.19.0-17-amd64
p   linux-image-4.19.0-17-amd64-unsigned                                             - Linux 4.19 for 64-bit PCs
p   linux-image-4.19.0-17-cloud-amd64                                                - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-17-cloud-amd64-dbg                                            - Debug symbols for linux-image-4.19.0-17-cloud-amd64
p   linux-image-4.19.0-17-cloud-amd64-unsigned                                       - Linux 4.19 for x86-64 cloud
p   linux-image-4.19.0-17-rt-amd64                                                   - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-4.19.0-17-rt-amd64-dbg                                               - Debug symbols for linux-image-4.19.0-17-rt-amd64
p   linux-image-4.19.0-17-rt-amd64-unsigned                                          - Linux 4.19 for 64-bit PCs, PREEMPT_RT
p   linux-image-4.19.0-6-amd64                                                       - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-6-cloud-amd64                                                 - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-6-rt-amd64                                                    - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-4.19.0-8-amd64                                                       - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-8-cloud-amd64                                                 - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-8-rt-amd64                                                    - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-4.19.0-9-amd64                                                       - Linux 4.19 for 64-bit PCs (signed)
p   linux-image-4.19.0-9-cloud-amd64                                                 - Linux 4.19 for x86-64 cloud (signed)
p   linux-image-4.19.0-9-rt-amd64                                                    - Linux 4.19 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-5.10.0-0.bpo.3-amd64                                                 - Linux 5.10 for 64-bit PCs (signed)
p   linux-image-5.10.0-0.bpo.3-amd64-dbg                                             - Debug symbols for linux-image-5.10.0-0.bpo.3-amd64
p   linux-image-5.10.0-0.bpo.3-amd64-unsigned                                        - Linux 5.10 for 64-bit PCs
p   linux-image-5.10.0-0.bpo.3-cloud-amd64                                           - Linux 5.10 for x86-64 cloud (signed)
p   linux-image-5.10.0-0.bpo.3-cloud-amd64-dbg                                       - Debug symbols for linux-image-5.10.0-0.bpo.3-cloud-amd64
p   linux-image-5.10.0-0.bpo.3-cloud-amd64-unsigned                                  - Linux 5.10 for x86-64 cloud
p   linux-image-5.10.0-0.bpo.3-rt-amd64                                              - Linux 5.10 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-5.10.0-0.bpo.3-rt-amd64-dbg                                          - Debug symbols for linux-image-5.10.0-0.bpo.3-rt-amd64
p   linux-image-5.10.0-0.bpo.3-rt-amd64-unsigned                                     - Linux 5.10 for 64-bit PCs, PREEMPT_RT
p   linux-image-5.10.0-0.bpo.4-amd64                                                 - Linux 5.10 for 64-bit PCs (signed)
p   linux-image-5.10.0-0.bpo.4-amd64-dbg                                             - Debug symbols for linux-image-5.10.0-0.bpo.4-amd64
p   linux-image-5.10.0-0.bpo.4-amd64-unsigned                                        - Linux 5.10 for 64-bit PCs
p   linux-image-5.10.0-0.bpo.4-cloud-amd64                                           - Linux 5.10 for x86-64 cloud (signed)
p   linux-image-5.10.0-0.bpo.4-cloud-amd64-dbg                                       - Debug symbols for linux-image-5.10.0-0.bpo.4-cloud-amd64
p   linux-image-5.10.0-0.bpo.4-cloud-amd64-unsigned                                  - Linux 5.10 for x86-64 cloud
p   linux-image-5.10.0-0.bpo.4-rt-amd64                                              - Linux 5.10 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-5.10.0-0.bpo.4-rt-amd64-dbg                                          - Debug symbols for linux-image-5.10.0-0.bpo.4-rt-amd64
p   linux-image-5.10.0-0.bpo.4-rt-amd64-unsigned                                     - Linux 5.10 for 64-bit PCs, PREEMPT_RT
p   linux-image-5.10.0-0.bpo.5-amd64                                                 - Linux 5.10 for 64-bit PCs (signed)
p   linux-image-5.10.0-0.bpo.5-amd64-dbg                                             - Debug symbols for linux-image-5.10.0-0.bpo.5-amd64
p   linux-image-5.10.0-0.bpo.5-amd64-unsigned                                        - Linux 5.10 for 64-bit PCs
p   linux-image-5.10.0-0.bpo.5-cloud-amd64                                           - Linux 5.10 for x86-64 cloud (signed)
p   linux-image-5.10.0-0.bpo.5-cloud-amd64-dbg                                       - Debug symbols for linux-image-5.10.0-0.bpo.5-cloud-amd64
p   linux-image-5.10.0-0.bpo.5-cloud-amd64-unsigned                                  - Linux 5.10 for x86-64 cloud
p   linux-image-5.10.0-0.bpo.5-rt-amd64                                              - Linux 5.10 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-5.10.0-0.bpo.5-rt-amd64-dbg                                          - Debug symbols for linux-image-5.10.0-0.bpo.5-rt-amd64
p   linux-image-5.10.0-0.bpo.5-rt-amd64-unsigned                                     - Linux 5.10 for 64-bit PCs, PREEMPT_RT
p   linux-image-5.10.0-0.bpo.7-amd64                                                 - Linux 5.10 for 64-bit PCs (signed)
p   linux-image-5.10.0-0.bpo.7-amd64-dbg                                             - Debug symbols for linux-image-5.10.0-0.bpo.7-amd64
p   linux-image-5.10.0-0.bpo.7-amd64-unsigned                                        - Linux 5.10 for 64-bit PCs
p   linux-image-5.10.0-0.bpo.7-cloud-amd64                                           - Linux 5.10 for x86-64 cloud (signed)
p   linux-image-5.10.0-0.bpo.7-cloud-amd64-dbg                                       - Debug symbols for linux-image-5.10.0-0.bpo.7-cloud-amd64
p   linux-image-5.10.0-0.bpo.7-cloud-amd64-unsigned                                  - Linux 5.10 for x86-64 cloud
p   linux-image-5.10.0-0.bpo.7-rt-amd64                                              - Linux 5.10 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-5.10.0-0.bpo.7-rt-amd64-dbg                                          - Debug symbols for linux-image-5.10.0-0.bpo.7-rt-amd64
p   linux-image-5.10.0-0.bpo.7-rt-amd64-unsigned                                     - Linux 5.10 for 64-bit PCs, PREEMPT_RT
p   linux-image-5.10.0-8-amd64                                                       -
p   linux-image-5.10.0-8-amd64-dbg                                                   -
p   linux-image-5.10.0-8-amd64-unsigned                                              -
p   linux-image-5.10.0-8-cloud-amd64                                                 -
p   linux-image-5.10.0-8-cloud-amd64-dbg                                             -
p   linux-image-5.10.0-8-cloud-amd64-unsigned                                        -
p   linux-image-5.10.0-8-rt-amd64                                                    -
p   linux-image-5.10.0-8-rt-amd64-dbg                                                -
p   linux-image-5.10.0-8-rt-amd64-unsigned                                           -
p   linux-image-5.9.0-0.bpo.5-amd64                                                  - Linux 5.9 for 64-bit PCs (signed)
p   linux-image-5.9.0-0.bpo.5-amd64-dbg                                              - Debug symbols for linux-image-5.9.0-0.bpo.5-amd64
p   linux-image-5.9.0-0.bpo.5-amd64-unsigned                                         - Linux 5.9 for 64-bit PCs
p   linux-image-5.9.0-0.bpo.5-cloud-amd64                                            - Linux 5.9 for x86-64 cloud (signed)
p   linux-image-5.9.0-0.bpo.5-cloud-amd64-dbg                                        - Debug symbols for linux-image-5.9.0-0.bpo.5-cloud-amd64
p   linux-image-5.9.0-0.bpo.5-cloud-amd64-unsigned                                   - Linux 5.9 for x86-64 cloud
p   linux-image-5.9.0-0.bpo.5-rt-amd64                                               - Linux 5.9 for 64-bit PCs, PREEMPT_RT (signed)
p   linux-image-5.9.0-0.bpo.5-rt-amd64-dbg                                           - Debug symbols for linux-image-5.9.0-0.bpo.5-rt-amd64
p   linux-image-5.9.0-0.bpo.5-rt-amd64-unsigned                                      - Linux 5.9 for 64-bit PCs, PREEMPT_RT
i   linux-image-amd64                                                                - Linux for 64-bit PCs (meta-package)
p   linux-image-amd64-dbg                                                            - Debugging symbols for Linux amd64 configuration (meta-package)
p   linux-image-amd64-signed-template                                                - Template for signed linux-image packages for amd64
p   linux-image-cloud-amd64                                                          - Linux for x86-64 cloud (meta-package)
p   linux-image-cloud-amd64-dbg                                                      - Debugging symbols for Linux cloud-amd64 configuration (meta-package)
v   linux-image-generic                                                              -
p   linux-image-rt-amd64                                                             - Linux for 64-bit PCs (meta-package), PREEMPT_RT
p   linux-image-rt-amd64-dbg                                                         - Debugging symbols for Linux rt-amd64 configuration (meta-package)


# install a specific version manually or choose to go for the latest release.
chyi in openmediavault in ~ via 🐍 v3.8.6 took 2s
❯ sudo apt -t buster-backports upgrade

# Install a specific kernel version
❯ sudo apt install linux-image-5.10.0-0.bpo.7-rt-amd64

# After the upgrade, can simply perform a reboot and the new kernel should be activated as the new default
❯ uname -r
5.10.0-0.bpo.7-rt-amd64

# Uninstalling unused kernels in Debian
❯ dpkg --get-selections | grep linux-image
linux-image-4.19.0-14-amd64			deinstall
linux-image-4.19.0-16-amd64			deinstall
linux-image-4.19.0-17-amd64			install
linux-image-5.10.0-0.bpo.7-rt-amd64		install
linux-image-amd64				install

# Uninstall the old one:
❯ sudo apt remove linux-image-4.19.0-17-amd64
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  linux-image-4.19.0-17-amd64 linux-image-amd64
0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
After this operation, 270 MB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 215702 files and directories currently installed.)
Removing linux-image-amd64 (4.19+105+deb10u12) ...
Removing linux-image-4.19.0-17-amd64 (4.19.194-1) ...
I: /vmlinuz.old is now a symlink to boot/vmlinuz-5.10.0-0.bpo.7-rt-amd64
I: /initrd.img.old is now a symlink to boot/initrd.img-5.10.0-0.bpo.7-rt-amd64
/etc/kernel/postrm.d/initramfs-tools:
update-initramfs: Deleting /boot/initrd.img-4.19.0-17-amd64
/etc/kernel/postrm.d/zz-update-grub:
Generating grub configuration file ...
Found background image: /usr/share/images/desktop-base/desktop-grub.png
Found linux image: /boot/vmlinuz-5.10.0-0.bpo.7-rt-amd64
Found initrd image: /boot/initrd.img-5.10.0-0.bpo.7-rt-amd64
done 
```


