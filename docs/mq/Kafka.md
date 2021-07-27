```
# 查看日志
I have no name!@kafka-0:/$ ls /opt/bitnami/kafka/bin/
connect-distributed.sh        kafka-console-producer.sh    kafka-log-dirs.sh                    kafka-server-start.sh               windows
connect-mirror-maker.sh       kafka-consumer-groups.sh     kafka-metadata-shell.sh              kafka-server-stop.sh                zookeeper-security-migration.sh
connect-standalone.sh         kafka-consumer-perf-test.sh  kafka-mirror-maker.sh                kafka-storage.sh                    zookeeper-server-start.sh
kafka-acls.sh                 kafka-delegation-tokens.sh   kafka-preferred-replica-election.sh  kafka-streams-application-reset.sh  zookeeper-server-stop.sh
kafka-broker-api-versions.sh  kafka-delete-records.sh      kafka-producer-perf-test.sh          kafka-topics.sh                     zookeeper-shell.sh
kafka-cluster.sh              kafka-dump-log.sh            kafka-reassign-partitions.sh         kafka-verifiable-consumer.sh
kafka-configs.sh              kafka-features.sh            kafka-replica-verification.sh        kafka-verifiable-producer.sh
kafka-console-consumer.sh     kafka-leader-election.sh     kafka-run-class.sh                   trogdor.sh

进入Kafka pod, 查看topic list
~ on 🐳 v20.10.7 (desktop-linux) took 3s
➜ kubectl exec -it kafka-0 /bin/bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
I have no name!@kafka-0:/$
I have no name!@kafka-0:/$ JMX_PORT=22222 kafka-topics.sh --list  --zookeeper=kafka-zookeeper
__consumer_offsets
app-platform-callback-lendlease-voice
app-platform-callback-pay
app-platform-callback-wechat
ingest-events
ingest-sessions
ingest-transactions
iot-events
iot-events-v3
iot-v6-events
locker-events-v3
locker-events-v3-new
middle-system-alarm
outcomes
robot-events
robot-events-v3
robot-metrics
simcard-events
station-events-v3
unit-deploy
I have no name!@kafka-0:/$
```
