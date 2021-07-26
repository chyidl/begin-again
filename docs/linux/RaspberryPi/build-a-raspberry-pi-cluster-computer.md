# Build a Raspberry Pi cluster computer

* Make sure the system time is right
```
# install the ntpdate package to periodically sync the system time in the background
$ sudo apt install ntpdate -y
```

* Shared Storage
```
In order for a cluster to work well, a job should be able to be run on any of nodes in the cluster. This means that each node needs to be able to access the same files.

NFS (Network file system)

# Installing NFS Client Packages
$ sudo apt update
$ sudo apt install nfs-common

# Create the mount folder
$ sudo mkdir /clusterfs
$ sudo chown nobody.nogroup /clusterfs
$ sudo chmod -R 777 /clusterfs

# Setup automatic mounting
$ sudo vim /etc/fstab
<master node ip>:/export/ShareNFS /clusterfs nfs defaults 0 0

$ sudo mount -a

pi in ~ at raspberrypi took 13s
➜ df -h
Filesystem                    Size  Used Avail Use% Mounted on
/dev/root                      29G  4.7G   24G  17% /
devtmpfs                      399M     0  399M   0% /dev
tmpfs                         432M   12K  432M   1% /dev/shm
tmpfs                         432M  5.9M  426M   2% /run
tmpfs                         5.0M  4.0K  5.0M   1% /run/lock
tmpfs                         432M     0  432M   0% /sys/fs/cgroup
/dev/mmcblk0p1                253M   49M  204M  20% /boot
tmpfs                          87M     0   87M   0% /run/user/1000
172.30.1.14:/export/ShareNFS  916G   67G  850G   8% /clusterfs
```

* Configure the Master Node
```
slurm: workload manager
> Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters.
  1. It allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work.
  2. It provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes.
  3. It aritrates contention for resources by managing a queue of pending work.

# Login to the Master Node
> add hostname of the nodes and their IP addresses to the /etc/hosts
  <ip addr of node02>  node02
  <ip addr of node01>  node01

# Install the SLURM Controller Packages
$ sudo apt install slurm-wlm -y

# SLURM Configuration
> Use the default SLURM configuration file as a base
$ cd /etc/slurm-llnl
$ cp /usr/share/doc/slurm-client/examples/slurm.conf.simple.gz .
$ gzip -d slurm.conf.simple.gz
$ mv slurm.conf.simple slurm.conf

$ sudo vim /etc/slurm-llnl/slurm.conf
```

[Building a Raspberry Pi Cluster](https://glmdev.medium.com/building-a-raspberry-pi-cluster-784f0df9afbd)

* MPI
> MPI (Message Passing Interface) This protocol allows multiple computers to delegate taks amongst themseleves and respond with result.
```
# On each node, run the following
ubuntu in ~ at 3BPlus took 2s
➜ sudo apt install python3-mpi4py mpich

# test MPI working on each node
pi in ~ at raspberrypi took 2m 4s
➜ mpiexec -n 1 hostname
raspberrypi
```
