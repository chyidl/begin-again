# Connection Tracking 原理、应用
```
连接跟踪是许多网络应用的基础，kubernetes Service、Service Mesh sidecar、软件四层负载均衡器 LVS/IPVS、Docker network、OVS、iptables主机防火墙,都依赖连接跟踪功能
```

* Connection Tracking: 连接跟踪就是跟踪(并记录)连接的状态.

[connection tracking](../../misc/blog/node-conntrack.png)
```
> 连接跟踪就是发现并跟踪这些连接的状态:
    1. 从数据包中提取元组 (tuple) 信息，辨别数据流 (flow) 和对应的连接 (connection)
    2. 为所有连接维护一个状态数据库 (conntrack table)
    3. 回收过期的连接 (GC)
    4. 为更上层的功能提供服务

连接跟踪中"连接"概念和TCP/IP协议中"面向连接"连接并不完全相同
    TCP/IP 协议中，连接是四层Layer 4概念
        TCP 是有连接，面向连接 connection oriented, 发出去的包都要求对端应答ACK，并且有重传机制
        UDP 是无连接，发送的包无需对端应答，没有重传机制

    CT,一个元组tuple定义的一条数据流flow就表示一条连接 connection:
```

```
要跟踪一台机器的所有连接状态，就需要
    1. 拦截(或称过滤) 流经这台机器的每一个数据包，并进行分析
    2. 根据这些信息建立起这台机器上的连接信息数据库 (connection track table)
    3. 根据拦截到的包信息，不断更新数据库
```

[Netfilter architecture inside Linux kernel](../../misc/blog/netfilter-design.png)
> Netfilter 是Linux内核中一个对数据包进行控制、修改和过滤 (manipulation and filtering) 的框架, 在内核协议栈中设置若干hook点，以此对数据包进行拦截、过滤或其他处理
```
hook 机制就是在数据包的必经之路上设置若干检测点，所有到达这些检测点的包都必须接受检测，根据检测的结果决定
    1. 放行：不对包进行任何修改，退出检测逻辑，继续后面正常包的处理
    2. 修改: 修改IP第一进行NAT，然后
```
