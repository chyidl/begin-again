# Distributed Lock Manager

* What's the problem?
    * Consistency: 一致性
    * State Machine: 状态机
    * Within Locked Transaction
    ```
    Database Lock: 数据库锁 (MySQL InnoDB Locking Solutions)
        Shared Lock: 共享锁 -- 悲观锁
            SELECT LOCK IN SHARE MODE

        Exclusive Lock: 排他锁
            SELECT FOR UPDATE

        Versioning Optimistic Lock: -- 乐观锁
            SELECT id, data, version FROM table WHERE id = $ID;
            {Business Code}
            UPDATE table SET data = $data version = version + 1 WHERE id = $ID AND version=$VER;
            if {UPDATE} Failed, go to step 1 else Done!

    Shared Application:
        Using the Shard data Solution
        Forward all of the operations to a single node
        Consistency can be easy to be guaranteed
        * The Problems of Shard:
            Hotspots: Load is not balanced
            Multiple Entities Transaction
            Node Failed:
                R + W > N --> CAP Theorem [理论]
    Centralized Distributed Lock Manager: 中心化分布式锁
        Privides a lock-leasing protocol
        Transaction Service is stateless

        Lock Manager must be designed for HA:
            No single point failure: 没有单点故障
            The lock state can be persistent : 锁状态持久化

        Dead Lock Detection: 死锁检测
            Lock expired
            Keepalive heart beats
    ```
    * Six Lock Modes
    | Mode| Requesting Process | Other Processes|
    |:----|:-------------------|:---------------|
    |NUll (NL)| No access| Read or write access|
    | Concurrent Read (CR)| Read access only| Read or write access|
    | Concurrent Write (CW) | Read or write access | Read or write access|
    | Protected Read (PR) | Read access only | Read access only |
    | Protected Write (PW) | Read or write access | Read access only|
    | Exclusive (EX)| Read or write access| No access|

* Distributed Lock Manager
    * RedLock: Distributed locks with Redis
    ```
    SET resource_name my_random_value NX PX 30000
        my_random: Unique across all clients
        NX: Not Exists
        PX: Expred of 30s

    if redis.call("get", KEYS[1]) == ARGV[1] then
        redus.call("del", KEYS[1])
    end
    ```
        * Algorithm
        ```
        1. Client get the current time in miliseconds
        2. Client tries to acquire the lock  in all the N instances sequentially, using the same key name and random value in all the instances
        3. Successfuly acquire the lock - majority Redis nodes accept && elapsed time < lock validity time.
        4. Actual lock validity time = initial validity time - elapsed time
        5. If acquire the lock failed, try to unlock all instances.

        "The Algorithm makes dangerous assumptions about timing and system clocks"

        ```

    * Google Chubby
    ```
    Two Components - Master & Client SDK
    Cluster - typically 5 nodes
    Replicas - use Paxos protocol to elect a master and replicate the logs
    Failover - Master fails, other replicas run the election
    Session & Keeplive
        Client request or end a session
        Lease Interval and Lease Timeout
    Performance is average
    ```
    * ZooKeeper
    ```
    # How to use Zookeeper as look service
    1. Create `_locknode/lock-` with Sequence & Ephemeral flag
    2. Get children to see to check if I am the lowest sequence number
        Yes. Get the Lock
        No. Set the watch
    ```

* Takeaways
```
Concurrent transaction need to be synchronized
    DB Lock is fine, but the Optimistic Lock is great
    Sharding the data cannot solve the all of problem

Distributed Lock Service need the following features
    High Availability
        Dara Replicas - Strong consistent protocol - Pasox, Raft, Zab
        Master Failover - Leader election

    Deadlock Detecttion
        Keepalive & Lease Timeout
```


## 分布式锁-Redis
```
Redis锁使用Redis setnx命令
    SETNX key value: 加锁命令,当键不存在时，对键进行设置操作并返回成功，否则返回失败，KEY时锁的唯一标识
    DEL KEY: 删除命令，通过删除键值对释放锁, 以便其他线程可以通过SETNX命令获取锁
    EXPIRE KEY TIMEOUT: 锁超时，设置KEY的超时时间，以保证即使锁没有被显式释放，锁也可以在一定时间后自动释放，避免资源被永远锁住

    # 加锁/解锁伪代码
    if (setnx(key, 1) == 1) {
        expire(key, 30)
        try {
            // TODO 业务逻辑
        } finally {
            del(key)
        }
    }

    1. SETNX 和 EXPIRE非原子性, 如果SETNX成功，在设置锁超时时间后，服务器挂掉、重启或网络问题，导致EXPIRE命令没有执行，锁没有设置超时时间编程死锁
    2. 锁误解除, 如果线程A成功获取到锁，并且设置过期时间30秒，但线程A执行时间超过30秒，锁过期自动释放，此时线程锁B获取到了锁，随后A执行完成，线程A使用DEL命令来释放锁，此时线程B加的锁还没有执行完成，线程A实际释放的线程B加的锁
    3. 超时解锁导致并发:
        3.1: 将过期时间设置足够长，确保代码逻辑在锁释放之前能够执行完成
        3.2: 为获取锁的线程增加守护线程，为将要过期但未释放的锁增加有效时间
    4. 不可重入: 当线程在持有锁的情况下再次请求加锁,如果一个锁支持一个线程多次加锁,那么这个锁就是可重入
    5. 等待锁释放:
        5.1: 通过客户端轮询的方式，当未获取到锁时，等待一段时间重新获取锁，知道成功获取锁或等待超时，这种方式比较消耗服务器资源，当并发量比较大时，会影响服务器的效率.
        5.2: 使用Redis发布订阅功能,当获取锁失败时，订阅锁释放消息，获取锁成功后释放时，发送锁释放消息
    6. 主备切换:
        6.1: 为了保证Redis可用性，一般采用主从方式部署，主从数据同步还有异步和同步两种方式，Redis将指令记录在本地内存buffer中，然后异步将buffer中指令同步到从节点，从节点一边执行同步的指令流来达到和主节点一致的状态，一边向主节点反馈同步情况.
        在包含主从模式的集群部署方式中，当主节点挂掉时，从节点会取而代之，但客户端无明显感知，当客户端A成功加锁，指令还未同步，此时主节点挂掉，从节点提升为主节点，新的主节点没有锁的数据，当客户端B加锁时就会成功
        6.2:
```

## Appendix
[How to do disribute](https://martin.kleppmann.com/)
[Is Redlock safe](http://)
