* What is Kubernetes?
> Open source container orchestration tool
> Helps you manage containeried applications in different deployment environments
```
Trend from Monolith to Microservices, Increased usage of containers

High Availability or no downtime
Scalability or high performance
Disaster recovery - backup and restore
```

* K8s Components explained
    - Pod
        > is basically an abstraction over a container
        ```
        Smallest unit of K8s
        Abstraction over container
        usually 1 application per Pod
        Each Pod gets its own IP address
        ```
    - Service
        ```
        permanent IP address
        lifecycle of Pod and Service NOT connected.
        ```
    - Ingress
        ```
        forwarding service
        communication
        route traffic into cluster
        ```
    - ConfigMap
        ```
        external configuration of your application
        ```
    - Secrets
        ```
        used to store secret data
        base64 encoded
        ```
    - Volumes
        ```
        Storage on local machine
        or remote, outside of the K8s cluster

        k8s doesn't manage data persistance!
        ```
    - Deployment
        ```

        ```
    - StatefulSet
        ```
        StatefulSet for stateful apps or databases
        take care of replicating the pods and scaling them up or scaling them down but making sure the database reads and writes are synchronized so that no database inconsistencies

        DB are often hosted outside of K8s cluster
        ```

* Kuberntes Architecture
    - Work Node
    > Each Node has multiple Pods on it
    > 3 processes must be installed on every Node
        * container runtime
        * kubelet: interact with both - the container and node; kubelet starts the pod with a container inside
        * kube-proxy:

    - Master Node
    > 4 processes run on every master node
        * Api Server: is like cluster gateway; acts as a gatekeeper for authentication
        * Scheduler: just decides on which Node new Pod should be scheduled
        * Controller manager: detect cluster state changes
        * etcd: which is a key value store of a cluster

* Minikube and kubectl - Local Setup
    - minikube
    ```
    Master and Node processes run on one machine
    1. creates Virtual Box on your laptop
    2. Node runs in that Virtual Box
    1 Node k8s cluster
    for testing purposes

        $ brew install hyperkit
        $ brew install minikube
        // Create and start the cluster
        ➜ minikube start --vm-driver=hyperkit
        😄  minikube v1.22.0 on Darwin 11.5.1
        ✨  Using the hyperkit driver based on user configuration
        ❗  Local proxy ignored: not passing HTTP_PROXY=http://localhost:8001 to docker env.
        ❗  Local proxy ignored: not passing HTTPS_PROXY=http://localhost:8001 to docker env.
        ❗  Local proxy ignored: not passing HTTP_PROXY=http://localhost:8001 to docker env.
        ❗  Local proxy ignored: not passing HTTPS_PROXY=http://localhost:8001 to docker env.
        💿  Downloading VM boot image ...
            > minikube-v1.22.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
            > minikube-v1.22.0.iso: 242.95 MiB / 242.95 MiB [ 100.00% 11.70 MiB p/s 21s
        👍  Starting control plane node minikube in cluster minikube
        💾  Downloading Kubernetes v1.21.2 preload ...
            > preloaded-images-k8s-v11-v1...: 502.14 MiB / 502.14 MiB  100.00% 12.28 Mi
        🔥  Creating hyperkit VM (CPUs=2, Memory=2200MB, Disk=20000MB) ...
        ❗  Local proxy ignored: not passing HTTP_PROXY=http://localhost:8001 to docker env.
        ❗  Local proxy ignored: not passing HTTPS_PROXY=http://localhost:8001 to docker env.
        ❗  Local proxy ignored: not passing HTTP_PROXY=http://localhost:8001 to docker env.
        ❗  Local proxy ignored: not passing HTTPS_PROXY=http://localhost:8001 to docker env.
        🌐  Found network options:
            ▪ HTTP_PROXY=http://localhost:8001
        ❗  You appear to be using a proxy, but your NO_PROXY environment does not include the minikube IP (192.168.64.2).
        📘  Please see https://minikube.sigs.k8s.io/docs/handbook/vpn_and_proxy/ for more details
            ▪ HTTPS_PROXY=http://localhost:8001
            ▪ http_proxy=http://localhost:8001
            ▪ https_proxy=http://localhost:8001
            ▪ no_proxy=localhost,127.0.0.1,localaddress,.localdomain.com
        ❗  This VM is having trouble accessing https://k8s.gcr.io
        💡  To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
        🐳  Preparing Kubernetes v1.21.2 on Docker 20.10.6 ...
            ▪ env NO_PROXY=localhost,127.0.0.1,localaddress,.localdomain.com
            ▪ Generating certificates and keys ...
            ▪ Booting up control plane ...
            ▪ Configuring RBAC rules ...
        🔎  Verifying Kubernetes components...
            ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
        🌟  Enabled addons: storage-provisioner, default-storageclass
        🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

        ➜ kubectl get nodes
        NAME       STATUS   ROLES                  AGE     VERSION
        minikube   Ready    control-plane,master   4m48s   v1.21.2

        ➜ minikube status
        minikube
        type: Control Plane
        host: Running
        kubelet: Running
        apiserver: Running
        kubeconfig: Configured

        ➜ kubectl version
        Client Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:59:11Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"darwin/amd64"}
        Server Version: version.Info{Major:"1", Minor:"21", GitVersion:"v1.21.2", GitCommit:"092fbfbf53427de67cac1e9fa54aaa09a28371d7", GitTreeState:"clean", BuildDate:"2021-06-16T12:53:14Z", GoVersion:"go1.16.5", Compiler:"gc", Platform:"linux/amd64"}
    ```
    - kubectl
    > command line tool for kubernetes cluster
    ```
    the most powerful of 3 clients
        UI
        API
        CLI: kubectl
    ```
    ```
    kubectl: for configuring the Minikube cluster

    minikube cli: for start up/deleting the cluster
    ```
