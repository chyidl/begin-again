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

* 架构
[prometheus arch](../../misc/kubenetes/prometheus-architecture.png)
```
Prometheus 直接接收或者通过中间Pushgateway网关被动获取指标数据

```

* Kubernetes安装Prometheus
```
.
├── prometheus-cm.yaml        # 使用ConfigMap 管理prometheus.yaml
├── prometheus-deploy.yaml    # 创建Prometheus Pod资源
├── prometheus-rbac.yaml      # ServiceAccount对象
├── prometheus-svc.yaml
└── prometheus-volume.yaml    # 时序数据持久化 TSDB

0 directories, 5 files
```

* 监控Kubernetes集群应用
```

```
