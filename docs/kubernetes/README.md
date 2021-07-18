# Docker & Kubernetes

## Docker 常用方法

* Docker vs. 虚拟机
```
1. 虚拟化技术依赖物理CPU和内存硬件级别的虚拟化，Docker是构建在操作系统层面，利用操作系统的容器化技术
```

* Docker Engine
> Docker Engine 是一个C/S架构的应用程序，docker 客户端和守护进程使用REST API 通过UNIX套接字或网络接口进行通信, 底层技术支持：Namespace(隔离),CGroups(资源限制),UnionFS(镜像和容器的分层)
    * dockerd常驻后台进程,用来监听Docker API 请求和管理Docker对象，比如镜像、容器、网络和Volume
    * docker remote api:
    * docker client,  命令行CLI接口(docker命令)，通过和REST API进行交互
    * docker registry: 用来存储Docker镜像的仓库
    * Images: 镜像是一个只读模版
    * Containers: 容器，容器是一个奖项的可运行的实例,容器的实质是进程,

```
# 默认用户名 library, 官方镜像
$ docker pull [选项] [Docker Registry 地址[:端口]/]仓库名[:标签]
❯ docker pull ubuntu:20.04
20.04: Pulling from library/ubuntu
c549ccf8d472: Pull complete
Digest: sha256:aba80b77e27148d99c034a987e7da3a287ed455390352663418c0f2ed40417fe
Status: Downloaded newer image for ubuntu:20.04
docker.io/library/ubuntu:20.04

# docker run 运行容器
    -i: 交互式操作
    -t: 终端
    --rm: 容器推出后删除
# docker run 创建容器时，Docker后台运行的标准操作包括:
        1. 检查本地是否存在指定的镜像，不存在就从公共仓库下载
        2. 利用镜像创建并启动一个容器
        3. 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
        4. 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中
        5. 从地址池配置一个IP地址给容器
        6. 执行用户执行的应用程序
        7. 执行完毕后容器被终止
❯ docker run -it --rm \
  ubuntu:20.04 \
  /bin/bash
root@d6fe6d1d21f3:/# cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.2 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.2 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
root@d6fe6d1d21f3:/#

# 列出镜像
❯ docker image ls
REPOSITORY                                          TAG       IMAGE ID       CREATED         SIZE
bitnami/redis-cluster                               6.2       fb7e254ca75e   7 days ago      92.9MB
<none>                                              <none>    355a832ad5f3   2 weeks ago     1.14GB
ubuntu                                              20.04     9873176a8ff5   3 weeks ago     72.7MB
mysql                                               8.0       c0cdc95609f1   2 months ago    556MB
mysql                                               8.0.25    c0cdc95609f1   2 months ago    556MB

# 查看镜像、容器、数据卷占用空间
❯ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         4         1.863GB   1.21GB (64%)
Containers      15        0         17.87MB   17.87MB (100%)
Local Volumes   8         7         383.5MB   191.7MB (49%)
Build Cache     0         0         0B        0B

# docker run -d: 后台运行
❯ docker run ubuntu:20.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
hello world
hello world
hello world
hello world
hello world
hello world

❯ docker run -d  ubuntu:20.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
c5e44c78f8aca89e3b6374a7c5a132d150f195bf0345fe332d541b5aee665bc8

# 查看容器信息
❯ docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS          PORTS     NAMES
c5e44c78f8ac   ubuntu:20.04   "/bin/sh -c 'while t…"   About a minute ago   Up 59 seconds             infallible_kare

# 获取容器输入信息
$ docker container logs [container ID or NAMES]

# 终止一个运行的容器
❯ docker container stop c5e44c78f8ac
c5e44c78f8ac

# 查看容器状态
❯ docker container ls -a
CONTAINER ID   IMAGE                                                       COMMAND                  CREATED          STATUS                       PORTS     NAMES
c5e44c78f8ac   ubuntu:20.04                                                "/bin/sh -c 'while t…"   4 minutes ago    Exited (137) 2 minutes ago             infallible_kare
6c4aa57de925   ubuntu:20.04                                                "/bin/sh -c 'while t…"   6 minutes ago    Exited (130) 5 minutes ago             jolly_elgamal
95ffbc04fc70   ubuntu:20.04                                                "/bin/echo 'Hello Wo…"   14 minutes ago   Exited (0) 7 minutes ago               stupefied_dewdney

# 重启启动容器
❯ docker container start c5e44c78f8ac
c5e44c78f8ac

# 删除容器
$ docker container rm [container_id]

# 清理掉处于终止状态的容器
❯ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
c5e44c78f8aca89e3b6374a7c5a132d150f195bf0345fe332d541b5aee665bc8
6c4aa57de925d9a808a5f99e843370c4f589e95f232f90e736a8df85c5ab2bcc
95ffbc04fc70901c902635038d0e70062e3ba7f1a29650e840c69b712c44ceb5
9344ede59213850beb32e8a2237b557e01d1b3d8ad112fcfea7df8b1ebc9ce45
6e6459c62bc823c3ed6f13586f60ea6241fe0f36c34f5596619d40a06c5d06f1
3da6970a0d6e8318e2422a458b72fe19caaf32e505cb42fcee5bdf10dd3bbe3e
78cca786566ee0e8ef8bcfa017ca2f7cf5b5658ab83ff9eb174a6e7a8d4f3391
8123dc71ffd7dbde379ffca63ce9c41ed6004b0e34dcb6d8352746f0434d487a
8b1aef6ee8700b8fd43fa491c0714b1c0a0cb46783db3ce7dadaad7fa72f3719
19bc61159ae9a46ae9ba39b63fd9c2996b54ff7aceaf16e4cc84474ae754eafc
2fdd98102c8c1d360606955b24ff7b5d33a56d5932c3fb83448cbfe1f682d564
530cdc938cd59e6b886d4fda30d3f505298ace3dd78fbf49d1a79370b5e11005
d2d21df430a8dcc09b195814319c832d6bbdad1cb7cc97222cf45cfed8a955f1
f8f5182b0536e588de060de7681b4f02b778b7db356b5083eefbfe01a038540d
e0242ef4504542f100e9fa722d57bfc59ea70231b1ca417b524bbcf6f68f609b
f440345d4c9331e54196042e4c81de64a64dd3495939cddb0a4c498269e04732
7f98fee4e0dbf49a47d1ea31e8b691dacbf17df3a71753bb7bba770a6e5a8d9f
d258e7257fc22a0d9d05b3eafb18bd41c15fdc0d98ad19837958665dc7d80a55

Total reclaimed space: 17.87MB

# 删除本地镜像
$ docker image rmi [镜像名]
❯ docker image rm fb7e254ca75e
Untagged: bitnami/redis-cluster:6.2
Untagged: bitnami/redis-cluster@sha256:7fe9f10a233fcba53783135a1aeb273dcaba61e3435cf5bd859cf541d26775a9
Deleted: sha256:fb7e254ca75e2ddc797901d261e582af449978c046c5f552ab6695e90d9dca20
Deleted: sha256:7ce8614bd328cf8992434b3ea12bd246c7ee68f86e85f3ec23078ffa8f29b7fd
Deleted: sha256:46447dd99bdbc73823cf972dd3735fcb59de4353d74003bc209f96ffab3aff9e
Deleted: sha256:7c0dbbebe11bcf5805df280e1843d92a9470478c5848915b25c53cf704d0a403
Deleted: sha256:fca2c6e88007872b857d2b26fe9454362f556cbbd5b577a72533329c96485c15
Deleted: sha256:38cc028cd8fb8379f6c1b62149d94a968aacaa643bb978c665ce82511b6bd78c
Deleted: sha256:fa2de2d4cebe07078c9ad6641ed043000e96af169afee5a147c9d4d4ddb2dcc8
Deleted: sha256:e70060dc232ad4658ff81e9e18aeed59c2bf49b46d851b2cde994e619fbacd28
Deleted: sha256:a8166bef76d7f75459125b20fc8791cc964bfefd83f90942a8b7d724987d45c1

# docker commit 定制镜像

# 定制Web服务器
❯ docker run --name webserver -d -p 9090:80 nginx
c9205e00be03835bc963fcb4e43689d378000219e90c9fd60c9139fbfcbd9ae4

# 访问Nginx欢迎页面
$ curl http://172.30.1.14:9090/

# 修改Nginx欢迎界面
❯ docker exec -it webserver bash
root@c9205e00be03:/# vim /etc/share/nginx/html/index.html
bash: vim: command not found
root@c9205e00be03:/# echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
root@c9205e00be03:/# exit
exit

# docker diff 查看容器存储层的修改
❯ docker diff webserver
C /var
C /var/cache
C /var/cache/nginx
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp
C /run
A /run/nginx.pid
C /etc
C /etc/nginx
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
C /usr
C /usr/share
C /usr/share/nginx
C /usr/share/nginx/html
C /usr/share/nginx/html/index.html
C /root
A /root/.bash_history

# 容器保存为镜像
❯ docker commit --author "learn docker" --message "modified index.html" webserver nginx:v2
sha256:22ca850c170ee04c5138f83dab8c6f3157c057efb7bf2c08fbdf6f300fd2aebb

# 查看新定制的镜像
❯ docker image ls nginx
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
nginx        v2        22ca850c170e   41 seconds ago   133MB
nginx        latest    4cdc5dd7eaad   4 days ago       133MB

# 查看镜像内的历史记录
❯ docker history nginx:v2
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
22ca850c170e   3 minutes ago   nginx -g daemon off;                            1.23kB    modified index.html
4cdc5dd7eaad   4 days ago      /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>      4 days ago      /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
<missing>      4 days ago      /bin/sh -c #(nop)  EXPOSE 80                    0B
<missing>      4 days ago      /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B
<missing>      4 days ago      /bin/sh -c #(nop) COPY file:09a214a3e07c919a…   4.61kB
<missing>      4 days ago      /bin/sh -c #(nop) COPY file:0fd5fca330dcd6a7…   1.04kB
<missing>      4 days ago      /bin/sh -c #(nop) COPY file:0b866ff3fc1ef5b0…   1.96kB
<missing>      4 days ago      /bin/sh -c #(nop) COPY file:65504f71f5855ca0…   1.2kB
<missing>      4 days ago      /bin/sh -c set -x     && addgroup --system -…   63.9MB
<missing>      4 days ago      /bin/sh -c #(nop)  ENV PKG_RELEASE=1~buster     0B
<missing>      4 days ago      /bin/sh -c #(nop)  ENV NJS_VERSION=0.6.1        0B
<missing>      4 days ago      /bin/sh -c #(nop)  ENV NGINX_VERSION=1.21.1     0B
<missing>      2 weeks ago     /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
<missing>      2 weeks ago     /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>      2 weeks ago     /bin/sh -c #(nop) ADD file:4903a19c327468b0e…   69.3MB
```

* Dockerfile 定制镜像
> Dockerfile 是一个文本文件，包含指令Instruction, 每一条指令构建一层
```
# 定制nginx镜像
$ mkdir mynginx
$ cd mynginx
$ touch Dockerfile

FROM nginx
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html

# docker build 构建镜像是在服务端Docker引擎中构建, 构架的时候，用户制定构建镜像上下文路径，docker build 命令将路径下的所有内容打包，上传给Docker引擎
❯ docker build -t nginx:v3 .
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM nginx
 ---> 4cdc5dd7eaad
 Step 2/2 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
  ---> Running in c4577827074a
  Removing intermediate container c4577827074a
   ---> 45eeb9662c35
   Successfully built 45eeb9662c35
   Successfully tagged nginx:v3


# FROM 制定基础镜像; Docker 存在一个特殊的镜像 scratch [这个镜像是虚拟概念,表示空白镜像]
# RUN 执行命令:
    shell 格式: RUN <命令>
    exec 格式: RUN ["可执行文件", "参数1"， "参数2"]
Union FS 有最大层数限制，AUFS最大不得超过127层
镜像是多层存储，每一层的东西并不会在下一层被删除，会一直跟随镜像，因此镜像构建确保每一层只添加真正需要添加的东西，任何无关的东西都应该清理掉
# COPY 指令: 源文件路径是相对路径
# ADD 指令:

.dockerignore: 剔除不需要作为上下文传递给Docker引擎

❯ docker image ls nginx
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
nginx        v3        45eeb9662c35   13 minutes ago   133MB
nginx        v2        22ca850c170e   12 hours ago     133MB
nginx        latest    4cdc5dd7eaad   5 days ago       133MB

# docker save 将镜像保存为归档文件
chyi in openmediavault in ~/download/mynginx
❯ docker save 45eeb9662c35 | gzip > nginx-v3.tar.gz

chyi in openmediavault in ~/download/mynginx took 16s
❯ ll
total 50M
-rw-r--r-- 1 chyi users  81 Jul 12 09:08 Dockerfile
-rw-r--r-- 1 chyi users 50M Jul 12 09:35 nginx-v3.tar.gz
```

* Move Docker images around
```
pv which monitor the flow of data through a pipe

# Save an image
$ docker save <image-name or image-id> -o <tarred-image-file-name>

# Load an image
$ docker load -i <tarred-image-file-name>

# Piping the image
$ docker save <image-name or image-id> | ssh user@host 'docker load'

$ docker save <image-name> | pv -N "Compressing..." | gzip | pv -N "Transfering to docker-machine..." | docker-machine ssh <target-machine-name> 'docker load'
```

* 私有镜像仓库
```
# 登陆
$ docker login

# 注销
$ docker logout

# 查找官方仓库镜像
$ docker search

# 下载本地
$ docker pull centos

# 构建本地私有仓库
# 将上传的镜像放在本地/srv/dev-disk-by-uuid目录下
❯ docker run -d \
      -p 5000:5000 \
      -v /srv/dev-disk-by-uuid-671cdfc1-9ed4-4b4b-9966-74197042607da/registry:/var/lib/registry \
      --restart=always \
      --name registry registry

Unable to find image 'registry:latest' locally
latest: Pulling from library/registry
ddad3d7c1e96: Pull complete
6eda6749503f: Pull complete
363ab70c2143: Pull complete
5b94580856e6: Pull complete
12008541203a: Pull complete
Digest: sha256:aba2bfe9f0cff1ac0618ec4a54bfefb2e685bbac67c8ebaf3b6405929b3e616f
Status: Downloaded newer image for registry:latest
367eb3880fa19300439343b9049f4bcecc5b278e1b093fda947690f82a018b57

# 在私有仓库上传、搜索、下载镜像
# docker tag IMAGE[:TAG] [REGISTRY_HOST[:REGISTRY_PORT]/]REPOSITORY[:TAG]
❯ docker tag mysql:latest 127.0.0.1:5000/mysql:lastest

# docker push 上传标记的镜像
❯ docker push 127.0.0.1:5000/mysql:lastest
The push refers to repository [127.0.0.1:5000/mysql]
03a007e88ba3: Pushed
d605c112cfab: Pushed
74634a9cf30b: Pushed
ea5fd90d1e58: Pushed
cffd1f984514: Pushed
3182d4b853f0: Pushed
ae477702a513: Pushed
570df12e998c: Pushed
b2abc2ad4a41: Pushed
e82f328cb5e6: Pushed
14be0d40572c: Pushed
02c055ef67f5: Pushed
lastest: digest: sha256:68b207d01891915410db3b5bc1f69963e3dc8f23813fd01e61e6d7e7e3a46680 size: 2828

# curl 查看仓库中的镜像
❯ curl 172.30.1.14:5000/v2/_catalog
{"repositories":["mysql"]}

# 先删除已有镜像
❯ docker image rm 127.0.0.1:5000/mysql:lastest
Untagged: 127.0.0.1:5000/mysql:lastest
Untagged: 127.0.0.1:5000/mysql@sha256:68b207d01891915410db3b5bc1f69963e3dc8f23813fd01e61e6d7e7e3a46680

chyi in openmediavault in ~ via 🐍 v3.8.6
❯ docker images
REPOSITORY                                          TAG       IMAGE ID       CREATED         SIZE
nginx                                               v3        45eeb9662c35   12 hours ago    133MB
nginx                                               v2        22ca850c170e   24 hours ago    133MB
nginx                                               latest    4cdc5dd7eaad   5 days ago      133MB
<none>                                              <none>    355a832ad5f3   2 weeks ago     1.14GB
ubuntu                                              20.04     9873176a8ff5   3 weeks ago     72.7MB
mysql                                               8.0       c0cdc95609f1   2 months ago    556MB
mysql                                               8.0.25    c0cdc95609f1   2 months ago    556MB
mysql                                               latest    c0cdc95609f1   2 months ago    556MB
registry                                            latest    1fd8e1b0bb7e   2 months ago    26.2MB
centos                                              latest    300e315adb2f   7 months ago    209MB

chyi in openmediavault in ~ via 🐍 v3.8.6
❯ docker pull 127.0.0.1:5000/mysql:lastest
lastest: Pulling from mysql
Digest: sha256:68b207d01891915410db3b5bc1f69963e3dc8f23813fd01e61e6d7e7e3a46680
Status: Downloaded newer image for 127.0.0.1:5000/mysql:lastest
127.0.0.1:5000/mysql:lastest

chyi in openmediavault in ~ via 🐍 v3.8.6
❯ docker images
REPOSITORY                                          TAG       IMAGE ID       CREATED         SIZE
nginx                                               v3        45eeb9662c35   12 hours ago    133MB
nginx                                               v2        22ca850c170e   24 hours ago    133MB
nginx                                               latest    4cdc5dd7eaad   5 days ago      133MB
<none>                                              <none>    355a832ad5f3   2 weeks ago     1.14GB
ubuntu                                              20.04     9873176a8ff5   3 weeks ago     72.7MB
127.0.0.1:5000/mysql                                lastest   c0cdc95609f1   2 months ago    556MB
mysql                                               8.0       c0cdc95609f1   2 months ago    556MB
mysql                                               8.0.25    c0cdc95609f1   2 months ago    556MB
mysql                                               latest    c0cdc95609f1   2 months ago    556MB
registry                                            latest    1fd8e1b0bb7e   2 months ago    26.2MB
centos                                              latest    300e315adb2f   7 months ago    209MB
```

* 数据共享与持久化
```
# 容器中管理数据的两种方式:
    数据卷 Data Volumes
    挂在主机目录 Bind mounts

# 数据卷: 一个可供一个或多个容器使用的特殊目录，绕过UFS
> 数据卷的使用，类似Linux下对目录或文件进行mount,镜像中被指定为挂载点的目录中文件被隐藏掉，只能看到挂载的数据卷
    1. 可以在容器之间共享和重用
    2. 对数据卷的修改会立马生效
    3. 对数据卷的更新，不会影响镜像
    4. 数据卷默认会一直存在，即使容器被删除

# 创建一个数据卷
❯ docker volume create my-vol
my-vol

# 查看所有的数据卷
❯ docker volume ls
DRIVER    VOLUME NAME
local     my-vol

# 查看指定数据卷的信息
❯ docker volume inspect my-vol
[
    {
        "CreatedAt": "2021-07-13T07:14:19+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/mnt/INNERDISK/docker/volumes/my-vol/_data",
        "Name": "my-vol",
        "Options": {},
        "Scope": "local"
    }
]

# 删除数据卷
❯ docker volume rm my-vol
my-vol

# 清理无用的数据卷
❯ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
mysql_my-db
redis_redis-cluster_data-0
redis_redis-cluster_data-3
redis_redis-cluster_data-4
a82b0ea8f07089d65e85341ce649850280288f9e0944cca79462999e6ad7d23a
redis_redis-cluster_data-1
redis_redis-cluster_data-2
redis_redis-cluster_data-5

Total reclaimed space: 383.5MB

# Docker 挂载主机目录默认权限是读写，用户可以通过增加readonly指定只读
$ docker run -d -P \
    --name web \
    --mount type=bind,source=/src/webapp,target=/opt/webapp,readonly \
    training/webapp \
    python app.py
```

* Docker 网络模式
```
# Bridge 模式
> 当Docker进程启动时，会在主机上创建docker0的虚拟网桥,此主机启动的Docker容器会连接到这个虚拟网桥上,虚拟网桥的工作方式和物理交换机类似，这样主机上的所有容器就通过交换机连在一个二层网络中，从docker0子网中分配一个IP给容器使用，并设置docker0的IP地址为容器的默认网关。主机上创建一对虚拟网卡 veth pair设备，Docker将veth
> pair设备的一端放在新创建的容器中，并命名为eth0(容器网卡),另一端放在主机中，以vethxx,并将网络设备加入到docker0网桥中

# 启动两个ubuntu 容器
    ❯ docker run -tid --net=bridge --name docker_bri1 ubuntu
    ❯ docker run -tid --net=bridge --name docker_bri2 ubuntu
#
    ❯ brctl show docker0
    bridge name     bridge id               STP enabled     interfaces
    docker0         8000.02426e1fd182       no              veth27b2afa
                                                            veth7dc5bcc
                                                            vethb98ebf2
# bridge 模式是docker默认网络模式
    ❯ docker exec -it docker_bri1 /bin/bash
    root@68f1084b3e46:/# ifconfig -a
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 172.17.0.3  netmask 255.255.0.0  broadcast 172.17.255.255
            ether 02:42:ac:11:00:03  txqueuelen 0  (Ethernet)
            RX packets 4654  bytes 18911842 (18.9 MB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 3751  bytes 255106 (255.1 KB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    root@68f1084b3e46:/# route -n
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         172.17.0.1      0.0.0.0         UG    0      0        0 eth0
    172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 eth0

# Linux系统网桥管理工具brctl
    $ apt-get install bridge-utils
    $ brctl addbr br0 # 添加网桥br0
    $ sudo ifconfig br0 192.168.100.1 netmask 255.255.255.0
    $ sudo brctl show # 现实所有的网桥信息
    $ sudo brctl show br0 # 显示某个网桥br0的信息
    $ sudo brctl delbr br0 # 删除网桥br0
    $ brctl addif br0 eth0 # 将eth0端口加入网桥br0
    $ brctl delif br0 eth0 # 从网桥br0中删除eth0端口

# 将容器加入自定义Docker网络连接多个容器
# -d: 指定Docker网络类型
    $ docker network create -d bridge my-net

# 运行容器1并连接新建的my-net网络
    ❯ docker run -it --rm --name busybox1 --network my-net busybox sh
    / # ping busybox2
    PING busybox2 (172.23.0.3): 56 data bytes
    64 bytes from 172.23.0.3: seq=0 ttl=64 time=0.268 ms
    64 bytes from 172.23.0.3: seq=1 ttl=64 time=0.269 ms

# 运行容器2并连接新建的my-net网络
    ❯ docker run -it --rm --name busybox2 --network my-net busybox sh
    / # ping busybox1
    PING busybox1 (172.23.0.2): 56 data bytes
    64 bytes from 172.23.0.2: seq=0 ttl=64 time=0.358 ms
    64 bytes from 172.23.0.2: seq=1 ttl=64 time=0.270 ms

# Host模式
> 容器将和宿主主机共用一个Network Namespace, 容器将会使用宿主主机的IP和端口

# Container 模式
> 新创建的容器和已经存在的容器共享一个Network Namespace, 新创建的容器不会创建自己的网卡，配置自己的IP，而是和一个指定的容器共享IP和端口范围

# None模式
> Docker 容器拥有自己的Network Namespace,但是并不为Docker容器进行任何网络配置，Docker容器没有网卡、IP、路由信息，需要自己为Docker容器添加网卡、配置IP
```

* Docker Compose
> Docker Compose 是Docker官方编排Orchestration项目，负责快速部署分布式应用，
> Compose 定位是定义和运行多个Docker容器的应用（Defining and running multi-container Docker applications), docker-compose.yaml 模版文件定义一组相互关联的应用容器
```
# Compose 两个重要概念
service: 服务，一个应用的容器，可以包含若干运行相同镜像的容器实例
project: 项目, 由一组关联的应用容器组成的完整业务单元

# 安装 compose
$ sudo pip install -U docker-compose

❯ docker-compose --version
docker-compose version 1.29.1, build c34c88b2

# Python 建立能够访问次数的Web网站
[web-demo](./docker-compose/web-demo)

$ docker-compose [-f=<args>...] [options] [COMMAND] [ARGS...]

$ docker-compose config # 验证Compose文件格式是否正确，若正确则现实配置，若格式错误现实错误原因
```

* Docker Machine
> 负责在多种平台快速安装Docker 环境
```
Docker Machine 是Docker官方提供的一个工具，可以帮助在远程的机器上安装Docker，
# Install Docker Machine (Linux)
$ base=https://github.com/docker/machine/releases/download/v0.16.0 \
  && curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine \
  && sudo mv /tmp/docker-machine /usr/local/bin/docker-machine \
  && chmod +x /usr/local/bin/docker-machine

# macOS install virtualbox
$ brew cask install virtualbox

# Check the installation by displaying the Machine version
❯ docker-machine -v
docker-machine version 0.16.0, build 702c267f

# Install VirtualBox
1. Add virtualbox.list to /etc/apt/sources.list.d
deb http://download.virtualbox.org/virtualbox/debian buster contrib

2. Add Oracle VirtualBox public key:
$ wget https://www.virtualbox.org/download/oracle_vbox_2016.asc2.
$ sudo apt-key add oracle_vbox_2016.asc

3. Install virtuabox-6.1
$ sudo apt-get update
$ sudo apt-get install virtualbox-6.1

# 创建本地主机实例Virtualbox驱动 创建一台Docker主机
$ docker-machine create -d virtualbox test
```

* Docker Swarm
> Swarm 是使用SwarmKit构建Docker引擎内置原生的集群管理和编排工具,提供Docker容器集群服务，是Docker官方对容器生态进行支持的核心方案
> 用户可以将多个Docker主机封装为单个大型的虚拟Docker主机，快速打造一套容器云平台，Swarm mode内置kv存储功能，提供众多的新特性，具有容错能力的去中心化设计、内置服务发现、负载均衡、路由网格、动态伸缩、滚动更新、安全传输。使得Docker原生的Swarm集群具备Mess、Kubernetes竞争能力

    * 节点
        * 管理节点 manager:
            > 用于Swarm集群的管理,一个Swarm集群可以有多个管理节点，但只有一个管理节点可以成为leader,leader通过raft协议实现
        * 工作节点 worker:
            > 任务执行节点，管理节点将服务service下发到工作节点执行，
![docker-swarm-structure](../../misc/kubenetes/docker-swarm-structrue.png)
    * Task: 任务是Swarm中最小的调度单位
    * Services: 一组任务的集合, 服务定义了任务的属性
        * replicated services: 按照规则在各个工作节点上运行指定个数的任务
        * global services: 每个工作节点上运行一个任务
![docker-swarm-task-service](../../misc/kubenetes/docker-swarm-task-service.png)

* Dockerfile 最佳实践
```
# 构建上下文
> doker build 命令会将当前工作目录被成为构建上下文,当前目录中的所有文件内容都将作为构建上下文发送到Docker守护进程中

# 使用.dockerignore 文件 - 指定忽略的文件和目录

# docker build --no-cache=true 构建过程中不使用缓存

# FROM: 尽可能使用当前官方仓库作为构建镜像的基础，推荐使用Alpine镜像，
# LABEL:
    LABEL name="chyi"
# RUN: 为了保持Dockerfile文件的可读性以及可维护性，建议将长的或复杂的RUN指令用反斜杠、分割成多行
    RUN apt-get update && apt-get install -y \
        vim
# CMD: ["executable", "param1", "param2"...]

# EXPOSE: 指定容器将要监听的端口

# ENV: 使用ENV为容器中安装的程序更新PATH环境变量

# COPY -> 支持简单的将本地文件拷贝到容器中
# ADD: 支持本地tar提取和远程URL支持

# ENTRYPOINT:

# VOLUME: 暴露任何数据库存储文件，配置文件，或容器创建的文件和目录

# USER: 如果某个服务不需要特权执行，建议使用USER指令切换到非root用户，现在Dockerfile中使用RUN groupadd -r postgres && useradd -r -g postgres postgres 指令创建用户和用户组

# WORKDIR: 在WORKDIR中使用绝对路径

# ONBUILD <其他指令>: ONBUILD是特殊指令，只有当前镜像为基础镜像，去构建下一级镜像的时候才会被执行，Dockerfile中的其他指令都是为定制当前镜像而准备，唯有ONBUILD是为帮助别人定制自己而准备
```

## kubenetes
```
# kubenetes cluster
    Master: 负责管理集群
        > master 协调集群中的所有活动，调度应用程序、维护应用程序的所需状态、扩展应用程序和滚动更新
    Node: 工作节点是Kubernetes集群中的工作机器，可以是物理机或虚拟机
        > kubelet 是管理节点并与Kubernetes Master 节点进行通信的代理
        > 节点具有处理容器操作的容器运行时 Docker或rkt

一个Kubernetes工作集群至少有三个节点，Master管理集群，Node节点用于托管正在运行的应用程序

Pod: 是一组紧密关联的容器集合，他们共享PID、IPC、Network和UTS namespace, 是kubernetes 调度的基本单位.
    Pod 的设计理念是支持多个容器在一个Pod中共享网络和文件系统,可以通过进程间通信和文件共享简单高效的方式组合完成服务.

Kubernetes 中所有对象都使用manifest（yaml或json）定义
```
[nginx.yaml](./base/nginx.yaml)

```
Master: Master节点是Kubernetes集群的控制节点, 负责整个集群的管理和控制
    Master节点包含一下组件:
        kube-apiserver: 集群控制的入口，提供HTTP REST服务
        kube-controller-manager: Kubernetes 集群中所有资源对象的自动化控制中心
        kube-scheduler: 负责Pod的调度

Node: Node节点是Kubernetes集群中的工作节点
    Node节点包含一下组件:
        kubelet: 负责Pod的创建、启动、监控、重启、销毁等工作,同时与Master节点协作，实现集群管理的基本功能
        kube-proxy: 实现Kubernetes Service的通信和负载均衡
        运行容器化(Pod)应用

Pod: Pod 是Kubernetes最基本的部署调度单元, 每个Pod可以由一个或多个业务容器和一个根容器(Pause容器)组成，一个Pod表示某个应用的一个实例

ReplicaSet: 是Pod副本的抽象，用于解决Pod的扩容和伸缩

Deployment: Deployment表示部署，在内部使用ReplicaSet实现

Service: 是Kubernetes最重要的资源对象，Kubernetes中的Service对象可以对应为服务架构中的微服务.Service定义服务的访问入口，服务的调用者通过这个地址访问Service后端的Pod副本实例。Service通过Label Selector同后端的Pod副本建立关系，Deployment保证后端Pod副本的数量，也就保证服务的伸缩性

Label: 识别Kubernetes对象的标签,以key/value 的方式附加到对象上 (key最长不能超过64bytes, value可以为空，也可以不超过253字节的字符串)

Label Selector: 筛选一组相同的Label对象
    Label Selector支持一下方式:
        1. 等式：app=nginx env!=production
        2. 集合: env in (production, qa)
        3. AND关系: app=nginx,env=test

Namespace: 是对一组资源和对象的抽象集合,常见的pods, services, deployments都是属于某一个namespace, Node, PersistenVolumes 则不属于任何namespace

Deployment: 确保任意时间都有指定数量的Pod"副本"在运行
    创建Deployment需要指定两个东西:
        Pod模板: 用来创建Pod副本的模板
        Label标签: Deployment需要监控的Pod标签

Service: 是应用服务的抽象，通过labels为应用提供负载均衡和服务发现. 匹配labels的Pod IP 和端口列表组成endpoints, 由kube-proxy负责将服务IP负载均衡到这些endpoints. 每一个service都会自动分配一个cluster IP (仅在集群内部可访问的虚拟地址) 和 DNS名，其他容器可以通过改地址或DNS来访问服务，而不需要了解后端容器的运行
```
[Kubernetes 组件](../../misc/kubenetes/k8s-basic.png)
```
Kubernetes 主要由一下几个组件组成
    etcd: 保存整个集群的状态数据库
    apiserver: 提供资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现
    controller manager: 负责维护集群的状态，故障检测、自动扩展、滚动更新
    scheduler: 负责资源的调度、按照预定的调度策略将Pod调度到相应的机器上
    kubelet: 负责维护容器的生命周期，同时负责Volume (CSI)和网络(CNI)的管理
    container runtime: 负责镜像管理以及Pod和容器的真正运行CRI
    kube-proxy: 负责Service 提供cluster内部的服务发现和负载均衡

    kube-dns: 负责为整个集群提供DNS服务
    Ingress Controller: 为服务提供外网入口
    Heapster: 提供资源监控
    Dashboard: 提供GUI

Kubernets 组件通信
    apiserver: 负责etcd存储的所有操作，且只有apiserver才直接操作etcd集群
    apiserver对内（集群中的其他组件）和对外(用户)提供统一的REST API, 其他组件均通过apiserver 进行通信
        controller manager, scheduler, kube-proxy, kubelet 通过apiserver watch API 检测资源变化情况，并对资源作相应的操作
        所有需要更新资源状态的操作均通过apiserver 的REST API 进行
    apiserver 会直接调用kubelet API (logs, exec, attach) 默认不校验kubelet证书，但可以通过--kubelet-certificate-authority 开启
```
![创建Pod流程](../../misc/kubenetes/k8s-pod-process.png)
    * 用户通过REST API创建一个Pod
    * apiserver将其写入etcd
    * scheduler 检测到未绑定Node的Pod,开始调度并更新Pod的Node绑定
    * kubelet 检测到新的Pod调度过来，通过container runtime 运行该Pod
    * kubelet 通过container runtime 取到Pod状态，并更新到apiserver中


## Kubeadm 搭建Kubernetes集群

![Kubernetes high-level component architecture](../../misc/kubenetes/k8s-structure.jpeg)
    * 核心层: Kubernetes 最核心的功能，对外提供API构建高层的应用，对内提供插件式应用执行环境
    * 应用层: 部署(无状态应用、有状态应用、批处理任务、集群应用) 和路由(服务发现、DNS解析)
    * 管理层: 系统度量 (基础设施、容器和网络的度量)，自动化(自动扩展、动态Privision) 以及策略管理(RBAC、Quota, PSP, NetworkPolicy)
    * 接口层: kubectl 命令行工具，客户端SDK以及集群
    * 生态系统:
        kubernetes 外部: 日志、监控、配置管理、CI、CD、Workflow
        Kubernetes 内部: CRI 、CNI、CVI、镜像仓库、Cloud Provider、集群自身的配置和管理

Control-plane node(s)
|Protocol | Direction | Port Range | Used By
|:--------|:----------|:-----------|:-------|
|TCP|Inbound|6443*| kubernetes API server | All|
|TCP|Inbound|2379-2380|etcd server client API| kube-apiserver, etcd|
|TCP|Inbound|10250|kubelet API| self, Control plane|
|TCP|Inbound|10251|kube-scheduler|Self|
|TCP|Inbound|10252|kube-controller-manager|Self|

Worker node(s)
|Protocol|Direction|Port Range| Purpose| Used By|
|:-------|:--------|:---------|:-------|:-------|
|TCP|Inbound|10250|kubelet API| Self, Control plane|
|TCP|Inbound|30000-32767|NodePort Services| All|

* Installing kubeadmin, kubelet and kubectl
```
kubeadm: the command to bootstrap the cluster
kubelet: the component that runs on all of machines in your cluster and does things like starting pods and containers
kubelet: the command line util to talk to your cluster
```

## Kubernetes 集群运行远离

## Kubernetes 调度策略

## Kubernetes 运维

## Helm 包管理的使用

## Kubenetes CI/CD


### FAQ:

* [12 Factor](https://12factor.net/zh_cn/)
```
12-Factor 为构建SaaS应用提供方法论
SaaS: 软件即服务
现在软件通常会作为一种服务来交付，也被称为网络应用程序
    1. 使用标准化流程自动配置，从而使新的开发者花费最少的学习成本加入这个项目
    2. 和操作系统之间尽可能的划清界限，在各个系统中提供最大的可移植性
    3. 适合部署在现代的云计算平台，从而在服务器和系统管理方面节省资源
    4. 将开发环境和生产环境的差异降至最低，并使用持续交付实施敏捷开发
    5. 可以在工具、架构和开发流程不发生明显变化的前提下实现扩展

1. 基准代码: 一份基准代码(codebase)，多份部署(deploy)
    代码库(code repository)
    基准代码和应用之间总是保持--对应的关系:
    开发人员可能有一些提交还没有同步至预发布环境，预发布环境也有一些提交没有同步至生产环境，但他们都共享一份基准代码，我们认为只是相同应用的不同部署而已.
2. 依赖: 显式声明依赖关系 (dependency)
    应用程序不会隐式依赖系统级的类库，一定通过依赖清单，确切声明所有依赖项。
    Python使用两个工具-PiP用作依赖声明，Virtualenv用作依赖隔离。
    无论用什么工具，依赖声明和依赖隔离必须一起使用，否则无法满足12-Factor规范
    如果应用必须使用到某些系统工具，那么这些工具应该被包含在应用中
3. 配置: 在环境中存储配置
    应用的配置在不同部署(预发布、生产环境、开发环境)
    判断一个应用是否正确地将配置排除在代码之外，一个简单的方法是看该应用的基准代码是否可以立刻开源，而不用担心会暴露任何敏感的信息
    12-Factor推荐将应用的配置存储于环境变量中(env vars, env). 环境变量可以非常方便地在不同的部署间做修改
4. 后端服务: 后端服务backing services当作附加资源
    后端服务是指程序运行所需要的通过网络调用的各种服务，如数据库(MySQL, PostgreSQL),消息/队列系统(RabbitMQ),缓存服务(Redis)
    12-Factor应用将这些数据库视作附加资源，这些资源和它们附属的部署保持松耦合
5. 构建、发布、运行: 严格分离构建和运行
    1. 构建阶段是指将代码仓库转化为可执行包的过程，构建时会使用制定版本的代码，获取和打包依赖项，编译成二进制文件和资源文件
    2. 发布阶段会将构建的结果和当前部署所需配置相结合，并能够立刻在运行环境中投入使用
    3. 运行阶段:针对选定的发布版本，在执行环境中启动一系列应用程序进程
6. 进程: 以一个或多个无状态进程运行应用
    12-Factor应用的进程必须无状态且无共享，任何需要持久化的数据都要存储在后端服务内
    粘性session是12-Factor反对的，Session中的数据应该保存在诸如Memcached或Redis带过期时间的缓存中
7. 端口绑定: Port binding
    12-Factor应用完全自我加载而不依赖于任何网络服务器就可以创建一个面向网络的服务，互联网应用通过端口绑定来提供服务，并监听发送至该端口的请求
8. 并发: 通过进程模型进行扩展
    进程是开发人员可以操作的最小单位
    12-Factor应用中，进程是一等公民，12-Factor应用的进程主要借鉴于unix守护进程模型。
    12-Factor应用的进程，不需要守护进程或写入PID文件，应该借助操作系统的进程管理器(systemd, 分布式进程管理云平台，或是类似Foreman的工具)
9. 易处理: 快速启动和优雅终止可最大化健壮性
    12-Factor应用的进程是易处理disposable, 可以瞬间开启或停止，有利于快速、弹性的伸缩应用，迅速部署变化的代码或配置，稳健的部署应用
    进程应当追求最小启动时间
    进程一旦接收终止信号(SIGTERM)就会优雅的终止，
    12-Factor应用都应该可以设计能够应对意外，不优雅的终结，Crash-only design将这种概念转化为呵护逻辑的理论
10. 开发环境与线上环境等价: 尽可能的保持开发、预发布、线上环境相同
    开发、预发布以及线上环境都应该使用同一个后端服务的相同版本
11. 日志: 把日志当作事件流
    12-factor应用本身从不考虑自己的输出流，不应该视图去写或者管理日志文件，相反，每个运行的进程都会直接的标准输出stdout事件流，开发环境中，开发人员可以通过这些数据流，实时在终端看到应用的活动

12. 管理进程: 后台管理任务当作一次性进程运行
    一次性管理进程应该和正常的常驻进程使用同样的环境，这些管理进程和任何其他的进程一样，使用相同的代码和配置
```
