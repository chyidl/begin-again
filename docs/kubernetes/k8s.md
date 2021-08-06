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
        Secret lives in K8s, not in the repository
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
        abstraction over Pods
        ```
    - Replicaset
        ```
        Replicaset is managing the replicas of a Pod
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
        * etcd: which is a key value store of a cluster; holds the current status of any K8s component

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

* Main Kubelet Commands
    - Basic kubectl commands
    ```
        $ kubectl get all
        CRUD commands
            Create deployment:  kubectl create deployment [name]
                $ kubectl create deployment nginx-depl --image=nginx
            Edit deployment:
                $ kubectl edit deployment [name]
            Delete deployment:
                $ kubectl delete deployment [name]

        Status of different K8s componenets
            kubectl get nodes | pod | services| replicaset | deployment

        Debugging pods
            Log to console: kubectl logs [pod name]
                $ kubectl logs [pod name]
            Get Interactive Terminal:
                $ kubectl exec -it [pod name] -- bin/bash
            Get Info about Pod
                $ kubectl describe pod [pod name]

        Use Configuration file for CRUD
            Apply a configuration file
                $ kubectl apply -f [file name] --namespace=[namespace]
            Delete with configuration file
                $ kubectl delete -f [file name] --namespace=[namespace]
    ```
    [nginx-deployment.yaml](./devops/nginx-deployment.yaml)
    [nginx-service.yaml](./devops/nginx-service.yaml)
    [nginx-deployment-result.yaml](./devops/nginx-deployment-result.yaml)

* K8s YAML Configuration File
    - Each configuration file has 3 parts
    ```
    1. Metadata
    2. Specification : are specfic to the kind
    3. Status: Automatically generated and added by Kubernetes
    ```
    - Format of configuration file
    ```

    ```
    - Connecting components (Labels & Selectors & Ports)
    ```

    ```

* Complete Application Setup with Kubernetes Components
> mongo-express & mongoDB
    - Overview of K8s Components
    ```
    1. 2 Deployment/Pod
    2. 2 Service
    3. 1 ConfigMap
    4. 1 Secret

    begin-again/docs/kubernetes on  main [✘!?]
    ➜ minikube service mongo-express-service
    |-----------|-----------------------|-------------|---------------------------|
    | NAMESPACE |         NAME          | TARGET PORT |            URL            |
    |-----------|-----------------------|-------------|---------------------------|
    | default   | mongo-express-service |        8081 | http://192.168.64.2:30000 |
    |-----------|-----------------------|-------------|---------------------------|
    🎉  Opening service default/mongo-express-service in default browser...
    ```

* K8s Namespaces explained
    - What is a Namespace?
    ```
    Organise resources in namespaces

    begin-again/docs/kubernetes on  main [✘!?]
    ➜ kubectl get namespace
    NAME              STATUS   AGE
    default           Active   10h
    kube-node-lease   Active   10h
    kube-public       Active   10h
    kube-system       Active   10h

    begin-again/docs/kubernetes on  main [✘!?]
    ➜ kubectl cluster-info
    Kubernetes control plane is running at https://192.168.64.2:8443
    CoreDNS is running at https://192.168.64.2:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    ```
    - What are the use cases?
    ```
    Everything in one Namespace
    Resources grouped in Namespace
    Resource Sharing:
        Staging and Development
        Blue/Green Deployment
    Access and Resource Limits on Namespaces
    Limit: CPU, RAM, Storage per NS

    1. Structure your components
    2. Avoid conflicts between teams
    3. Share services between different environments
    4. Access and Resource Limits on Namespaces Level
    ```
    - How Namespaces work and how to use it?
    ```
    Characteristics of Namespaces?
        1. You can't access most resources from another Namespace
            Each NS must define own ConfigMap, Secret
            Access Service in another Namespace [service-name].[namespace]

        2. Components, which can't be created within a Namespace
            $ kubectl api-resources --namespaced=false
            $ kubectl api-resources --namespaced=true

        By default, components are created in a default NS

    Change active namespace?
        Change the active namespace with kubens?
        $ brew install kubectx

        begin-again/docs/kubernetes on  main [✘!?] took 27s
        ➜ kubens
        default
        kube-node-lease
        kube-public
        kube-system
        my-namespace
    ```

