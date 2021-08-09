Prometheus
==========

* What is Prometheus?
```
Monitoring Tool:
    Highly dynamic container environments
    Traditional, bare server

```

* Where and Why is Prometheus used?
```
- constantly monitor all the services
- alert when crash
- checking memory usage:
    over for 70% one hour
- notify administrator
- monitoring network
```

* Prometheus Architecture
```
1. Prometheus Server:
    > processes and stores metrics data

    - Storage: Time Series Database
    - Retrieval: Data Retrieval Workers
    - HTTP Server: Accpets PromQL queries

2. AlertManager:
    > send alerts
    - How does Prometheus trigger the alerts?
    - Who receives the alerts?

    Email, Slack

3. Prometheus Web UI

Counter:
    How many times X happend
Gauge:
    What is the current value of x now
Histogram:
    how long or how big

Collecting Metrics Data from Targetes
    pulls over HTTP endpoints, hostaddress/metrics

Exporter:
    fetches metrics, Target some service

Monitoring your own applications?
    - How many requests?
    - How many exceptions?
    - How many server resources are used?

Pull system - more advantages:
    - multiple prometheus instances can pull metrics data

Pushgateway:


Prometheus Data Storage:
    Time Serial Database

PromQL Query Language:
    Grafana: powerful visualization tools

Prometheus Characteristics:
```

* Deploy Prometheus in Kubernetes cluster
    1. Creating all configuration YAML files yourself and execute them in right order
    2. Using an operator [kubernetes Operator]
        Manager of all Prometheus components
    3. Using Helm chart to deploy operator
        Helm: initiale setup
        Operator: manage setup

    ```
    # add the repo
    $ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

    # search charts
    $ helm search repo prometheus-community

    # stable/prometheus-operator -> rename -> kube-prometheus-stack
    begin-again/docs/kubernetes/devops on  main [!?]
    ➜ helm install prometheus prometheus-community/kube-prometheus-stack
    NAME: prometheus
    LAST DEPLOYED: Mon Aug  9 11:56:17 2021
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:
    kube-prometheus-stack has been installed. Check its status by running:
      kubectl --namespace default get pods -l "release=prometheus"

    Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.


    ```
