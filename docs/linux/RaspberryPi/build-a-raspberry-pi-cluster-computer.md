# Build a Raspberry Pi cluster computer


* [Build a Raspberry Pi cluster computer](https://magpi.raspberrypi.org/articles/build-a-raspberry-pi-cluster-computer)

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
