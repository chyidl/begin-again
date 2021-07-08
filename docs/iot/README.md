## Thing Model
```
满足并发写入:
    1. 批量写整体性能写/每间隔2S强制写
    2. kafka批量处理的思想借用

满足奇奇怪怪查询需求:
    1. 全文搜索/模糊搜索
    2. 范围查询
    3. 数据聚合

文档数据库: [Postgresql、MongoDB]
    MongoDB: 更新文档支持部分更新
    Postgrsql:
    ES: 比较重

    redis-search:  a.b.c -> a:{b:{c:}} HSET  QPS: 10W/s
    RediSearch - Redis Secondary Index & Query Engine
        RedisJSON + RediSearch as a real-time
    [https://redislabs.com/wp-content/uploads/2021/05/redisjson-redisearch-redisconf2021.pdf]
    Redis 高可用: 主备高可用
        sharding: 1W

时序数据库: TDEngine [查询历史数据]
    license: 云端厂商不允许那开源产品做服务
    timesacacedb: -- 自建
        缺失压缩；连续查询

    JsonPath:
    JsonSchema:

多租户场景使用:
    pass


postgresql 文档数据更新机制，属于全量更新
树节点拉平 测试性能无法满足

性能测试:
shard: 分片; 分片查询

资源/属性映射
对应的路径更新对应资源

主备切换
压力测试
fastapi: 瓶颈
```

## Dapr
```

```

## GRPC
```

```

