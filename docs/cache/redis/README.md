# The Amazing Redis
> Redis is an in-memory data structure store, used as a database, in-memory cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and streams.
> Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availablity via Redis Sentinel and automatic parititioning with Redis Cluster. You can run atomic operations on these types, like appending to a string; incrementing the value in a hash; pushing an element to a list; computing set intersection, union and difference; or getting the member with highest ranking in a sorted set. Redis also supports
> trivial-to-setup master-slave asynchronous replication, with very fast non-blocking first synchronization, auto-reconnection with partial resynchronization on net split. Other features include: Transactions, Pub/Sub, Lua scripting, Keys with a limited time-to-live, LRU eviction of keys.

[The Amazing Redis](https://medium.com/swlh/the-amazing-redis-620a621f3b2)

* Redis Cache Avalanche(雪崩), breakdown(击穿), and Penetration(穿透)
  - Cache Avalanche 雪崩
  ```
  发生雪崩现象是大量请求到达数据库 增加数据库的压力
    原因:
      1. 大量的数据缓存同时失效
      2. Redis Down
    解决方案:
      Q. 处理大量的数据同时在缓存中失效
      A. 避免设置相同的过期时间对大量的业务数据 + 随机时间

      Q. 发生雪崩如何降级别
      A. 非核心业务数据直接返回默认模版数据，减少非核心数据对数据库的访问

      Q. 发生Redis宕机
      A. Redis的QPS大概10000，数据库的QPS 1000. 直接返回结果不再访问数据。这样回对整个服务不可用，但是保护数据库; 限制请求数量；去除单点故障，采用主从集群部署，主节点Redis宕机，从节点转变为主节点
  ```
  - Cache Breakdown 击穿
  ```
    原因:
      1. HotSpot data: 热点数据失效，规模相对于雪崩比较小，击穿的发生条件是热点数据失效
    解决方案:
      2. 不设置热点数据过期时间
  ```
  - Cache Penetration 穿透
  ```
  缓存穿透：请求的数据既不存在缓存也不存在数据库，每次请求都直接达到数据库，当大量的这样的请求发生会对数据库产生压力
    原因:
      1. 数据本应该存在，但是错误的操作导致误删除
      2. 恶意攻击, 专门请求数据库中不存在的数据
      3. 设计上的BUG
    解决方案:
      1. 设计一个NULL，或者默认值作为缓存值
      2. 设计数据过滤规则，并不是所有的无效请求数据都能走到数据库
      3. 使用Bloom过滤器，bloom-filter
  ```
