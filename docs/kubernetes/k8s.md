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
        - local volumes
        - not created via PV and PVC
        - managed by Kubernetes
        ```
    - Secrets
        ```
        Secret lives in K8s, not in the repository
        used to store secret data
        base64 encoded
        - local volumes
        - not created via PV and PVC
        - managed by Kubernetes
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
    - [minikube](https://github.com/AliyunContainerService/minikube/wiki)
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

* K8s Ingress explained
    - What is Ingress?
    ```
    External Service vs. Ingress

    Host:
        - valid domain address
        - map domain name to Node's IP address, which is the entrypoint
    ```
    - How to configure Ingress in your Cluster?
    ```
    You need an implementation for Ingress!
    Which is Ingress Controller
    ```
    - Ingress YAML Configuration
    - When do you need Ingress?
    - Ingress Controller
    ```
    evaluates all the rules
    manages redirections
    entrypoint to cluster
    ```
    - Configure Ingress in Minikube
    ```
    Install Ingress Controller in Minikube
    # Automatically starts the K8s Nginx implementation of Ingress Controller
    $ minikube addons enable ingress

    ➜ kubectl get all -n kubernetes-dashboard
    NAME                                             READY   STATUS    RESTARTS   AGE
    pod/dashboard-metrics-scraper-7886f6d855-dx728   1/1     Running   0          61s
    pod/kubernetes-dashboard-66f6c8f7c5-6t42t        1/1     Running   0          61s

    NAME                                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
    service/dashboard-metrics-scraper   ClusterIP   10.97.169.116    <none>        8000/TCP   62s
    service/kubernetes-dashboard        ClusterIP   10.101.159.196   <none>        80/TCP     62s

    NAME                                        READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/dashboard-metrics-scraper   1/1     1            1           63s
    deployment.apps/kubernetes-dashboard        1/1     1            1           63s

    NAME                                                   DESIRED   CURRENT   READY   AGE
    replicaset.apps/dashboard-metrics-scraper-7886f6d855   1         1         1       62s
    replicaset.apps/kubernetes-dashboard-66f6c8f7c5        1         1         1       62s
    ```
    - Configuring TLS Certificate
    ```
    1. Data keys need to be "tls.crt" and "tls.key"
    2. Values are file contents NOT file paths/locations
    3. Secret component must be in the same namespace as the Ingress component
    ```

* Helm - Package Manager of K8s
    - What is Helm?
    ```
    Package Manager for Kubernetes.
    To package YAML Files and distribute them in public and private repositories.
    ```
    - What are Helm Charts?
    ```
    Bundle of YAML Files
    Create your own Helm Charts with Helm
    Push them to Helm Repository
    Download and use existing ones

    Templating Engine
        1. Define a common blueprint
        2. Dynamic values are replaced by placeholders

    Helm Chart Structure
        Directory structre:
            mychart/            -- name of chart
                Chart.yaml      -- meta info about chart
                values.yaml     -- values for the template files
                charts/         -- chart dependencies
                templates/      -- the actual template files
        $ helm install <chartname>  # template files will be filled with the values from values.yaml
        $ helm install --values=my-values.yaml <chartname>
        $ helm install --set version=2.0.0

    Release Management
        Helm Version 2 comes in two parts:
            CLIENT (helm CLI)
            SERVER (Tiller) -- Helm 3 Tiller got removed

        $ helm install <chartname>
        $ helm upgrade <chartname>
            - Changes are applied to existing deployment instead of creating a new one
        $ helm rollback <chartname>
            - Handling rollbacks
    ```
    - How to use them?
    ```
    Helm Hub: Discover & launch great Kubernetes-ready apps
    $ helm search <keyword>
    ```
    - When to use them?
    ```
    Same Applications across different environments
        Development
        Staging
        Production
    ```

* K8s Volumes explained
    - How to persist data in Kubernetes using volumes?
    ```
    Storage that doesn't depend on the pod lifecycle.
    Storage must be available on all nodes.
    Storage needs to survive even if cluster crashes.

    1. Persistent Volume - PV
        - a cluster resource --
        - created via YAML file
        - needs actual physical storage, like [local disk, nfs server, cloud-storage]
        - Persistent Volumes are NOT namespaced
        - Local vs. Remote Volume Types
        Each volume type has it's own use case!

    2. Persistent Volume Claim - PVC
        - Claims must be in the same namespace!

        1. Pod requests the volume through the PV claim
        2. Claim tries to find a volume in cluster
        3. Volume has the actual storage backend

    3. Storage Class
        - SC provisions Persistent Volumes dynamically.
        Storage Class create persistent volumes dynamically in the background
        1. Pod claims storage via PVC
        2. PVC requests storage from SVC
        3. SC creates PV that meets the needs of the Claim
    ```

* K8s StatefulSet
    - What is StatefulSet?
        stateful application: [deployed using StatefulSet]
            - databases
            - applications that stores data

        stateless applications: [deployed using Deployment]
            - don't keep record of state
            - each request is cimpletely new

        Stateful applications not perfect for containerized environments

    - Why StatefulSet is used?
    - How StatefulSet works and how it's different from Deployment?

* K8s Services
    - What is a Kubernetes Service and when we need it?
    ```
    Each Pod has its own IP address
        - Pods are ephemeral - are destroyed frequently!
    Service:
        - stable IP address
        - loadbalancing
        - loose coupling
        - within & outside cluster

    Service Endpoints:
        K8s creates Endpoint object
        same name as Service
        keeps track of, which Pods are the members/endpoints of the Service
    ```
    - Different Service types explained
    ```
        - ClusterIP Services
            - default type
        - Headless Services
            - Set ClusterIP to None - Returns Pod IP address instead
        - NodePort Services
            - NodePort Range: 30000 - 32767
            - NodePort Service is an extension of ClutserIP Service
        - LoadBalancer Service
            - LoadBalancer Service is an extension of NodePort Service
    ```

Appendix
-------
* Kubernetes drops Docker support?
    - Why is Docker deprecated?
    ```
    1. Kubernetes supports different container runtime
        Docker:
            just one of those container runtimes

    Docker Engine:
        CLI:
        API:
        Server:
            - container runtime: start/stop
            - Volumes: persisting data
            - Network
            - build images
    Dockershim: implements CRI support for Docker
    Containerd:
        - 2nd most popular container runtime
        - is already used in Managed K8s services

    CICD Pipeline:
        test code -> build Docker Image -> push to Docker Repo -> deploy to K8s cluster
    ```
    - OCI
    ```
    standards around container technology
    Docker, containered, CRI-O comply to these OCI standards
    ```

* Istio
> Istio is a Service Mesh
```
Service Mesh is a Pattern or Paradigm, Istio is an implementation

Service Mesh: is a popular solution for managing communication between individual microservices
    Sidecar Proxy:
        handless these networking logic
        acts as a Proxy
        third-party application
        cluster operators can configure it easyly
        Cluster operators can configure it easily
        Control Plane
    Traffic Split: - Canary金丝雀 Deployment

Challenges of a microservice architecture:
    1. Business Logic BL
    2. Communication configurations (COMM)
    3. Security Logic (SEC)
    4. retry logic (R)
    5. metrics & traning systems

Istio Architecture
    proxy: envoy
    control Plane: istiod : configuration, discovery, certificates
    Data Plane:
How to configure Istio?
```
