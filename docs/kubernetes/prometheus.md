Prometheus
==========

* 特征
```
1. 具有metric名称和键值对标识的时间序列数据的多维数据模型
2. 灵活的查询语句
3. 不依赖分布式存储，只和本地磁盘有关
4. 通过HTTP的服务拉取时间序列数据
5. 支持推送的方式来添加时间序列数据
6. 支持通过服务发现或静态配置发现目标
7. 多种图形和仪表板支持
```

* 组件
```
Prometheus Server: 用于抓取指标，存储时间序列数据
exporter: 暴露指标 
pushgateway: push的方式将指标数据推送到该网关
alertmanager: 处理报警
adhoc: 数据查询
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
