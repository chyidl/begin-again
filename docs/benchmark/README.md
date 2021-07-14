# BenchMark


## 网络测试

* Measure TCP and UDP bandwidth and latency over private network
> qperf, to check TCP and UDP bandwidth and latencies between two servers.
```
# Install QPERF
$ sudo apt install qperf

# Using Qperf
    1. first server: qperf run in a "server" mode
chyi in openmediavault in ~ via 🐍 v3.8.6 took 14s
❯ qperf

    2. second server: qperf can be invoked to run various tests
        tcp_bw and udp_bw: the rate of transfer over TCP and UDP, reported at byte-level (MB/s) and packet-level (messages/sec)
        tcp_lat and udp_lat: the average per-hop time taken for a TCP or UDP packet
ubuntu@3BPlus:~$ qperf -v 172.30.1.14 tcp_bw udp_bw tcp_lat udp_lat
tcp_bw:
    bw              =  4.19 MB/sec
    msg_rate        =  63.7 /sec
    send_cost       =   244 sec/GB
    recv_cost       =   122 sec/GB
    send_cpus_used  =   114 % cpus
    recv_cpus_used  =    51 % cpus
udp_bw:
    send_bw         =  55.7 MB/sec
    recv_bw         =  2.23 MB/sec
    msg_rate        =    68 /sec
    send_cost       =  60.9 sec/GB
    recv_cost       =  89.8 sec/GB
    send_cpus_used  =   340 % cpus
    recv_cpus_used  =    20 % cpus
tcp_lat:
    latency        =  7.39 ms
    msg_rate       =   136 /sec
    loc_cpus_used  =  12.9 % cpus
    rem_cpus_used  =    10 % cpus
udp_lat:
    latency        =   7.3 ms
    msg_rate       =   137 /sec
    loc_cpus_used  =    10 % cpus
    rem_cpus_used  =  28.9 % cpus

see even more detailed output with the -vv flag; -t NN flag run the tests for a longer time; -m 4k choose the size of the message to be used for the tests
```

## 设备硬件测试
* Linux 测试硬盘读写速度
```
# 使用dd 测试写速度
chyi in openmediavault in ~ via 🐍 v3.8.6 took 2s
❯ sudo dd if=/dev/zero of=/srv/dev-disk-by-uuid-671cdfc1-9ed4-4b4b-9966-74197042607d/tempfile bs=1M count=1024; sync
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 2.61412 s, 411 MB/s

# hdparm 对硬盘测试
$ sudo apt install hdparm
先用lsblk 或者 fdisk -l 查看设备信息
❯ sudo lsblk
NAME                  MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                     8:0    0 119.2G  0 disk
└─sda1                  8:1    0 119.2G  0 part /mnt/INNERDISK
sdb                     8:16   0 931.5G  0 disk
└─sdb1                  8:17   0 931.5G  0 part /srv/dev-disk-by-uuid-671cdfc1-9ed4-4b4b-9966-74197042607d
mmcblk1               179:0    0  58.2G  0 disk
├─mmcblk1p1           179:1    0   512M  0 part /boot/efi
├─mmcblk1p2           179:2    0   488M  0 part /boot
└─mmcblk1p3           179:3    0  57.3G  0 part
  ├─debian--vg-root   253:0    0    11G  0 lvm  /
  ├─debian--vg-swap_1 253:1    0   976M  0 lvm  [SWAP]
  ├─debian--vg-var    253:2    0     4G  0 lvm  /var
  ├─debian--vg-tmp    253:3    0   760M  0 lvm
  └─debian--vg-home   253:4    0  40.7G  0 lvm  /home
mmcblk1boot0          179:256  0     4M  1 disk
mmcblk1boot1          179:512  0     4M  1 disk

❯ sudo hdparm -Tt /dev/sdb

/dev/sdb:
 Timing cached reads:   3948 MB in  2.00 seconds = 1974.95 MB/sec
 Timing buffered disk reads: 348 MB in  3.01 seconds = 115.48 MB/sec
```

