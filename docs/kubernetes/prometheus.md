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

- [  ][prometheus-community/helm-charts](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus)
> This chart bootstraps a Prometheus deployment on a Kubernetes cluster using the Helm package manager.
```
# Get Repo Info
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo add kube-state-metrics https://kubernetes.github.io/kube-state-metrics
$ helm repo update

# Install Chart
$ helm install [RELEASE_NAME] prometheus-community/prometheus
```
