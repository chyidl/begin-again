LVM
===
> Logical Volume Management, Utilizing the device mapper Linux kernel framework


Introduction
------------
> LVM functions by layering abstractions on top of physical storage devices.

  - Physical Volumes:
    > Physical volumes are regular storage devices

  - Volume Groups:
    > LVM combines physical volumes into storage pools known as volume groups.

  - Logical Volumes:
    > A volume group can be sliced up into any number of logical voluems.
    > Logical volumes are functionally equivalent to partitions on a physical disk, but with much more flexibility.

  - Extents:
    > The extents size represents the smallest amount of space that can be allocated by LVM
    - physical extents:
    - logical extents:

Use Case
--------
  - Mark the Physical Devices as Physical Volumes
  ```
    # display all available block devices that LVM can interact with
    chyi in ~ at k8s-master
    ➜ sudo lvmdiskscan
    [sudo] password for chyi:
      /dev/mmcblk1boot0     [       4.00 MiB]
      /dev/mmcblk1boot1     [       4.00 MiB]
      /dev/debian-vg/root   [      10.96 GiB]
      /dev/sda1             [     119.24 GiB]
      /dev/mmcblk1p1        [     512.00 MiB]
      /dev/debian-vg/swap_1 [     976.00 MiB]
      /dev/mmcblk1p2        [     488.00 MiB]
      /dev/debian-vg/var    [       3.96 GiB]
      /dev/mmcblk1p3        [      57.26 GiB] LVM physical volume
      /dev/debian-vg/tmp    [     760.00 MiB]
      /dev/debian-vg/home   [      40.64 GiB]
      /dev/sdb1             [     931.51 GiB]
      4 disks
      7 partitions
      0 LVM physical volume whole disks
      1 LVM physical volume

    chyi in ~ at k8s-master took 2s

  # Using these device within LVM will overwrite the current contents.
  ```

LVM Resize
----------
```

```
