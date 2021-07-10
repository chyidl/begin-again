# HAProxy Redis Sentinel
> HAProxy in front of a Redis master and slave (agent) replication to ensure that client and application connections are always redirected to the master server. High availability for Redis deployment including master and agent implementation is achieved by implementing Redis Sentinel, which continuously performs monitoring, notification, and automatic failover if a master becomes unresponsive.

## HAProxy
> HAProxy is a tool that allows you to route requests to available servers according to various rules. It supports both TCP and HTTP protocols.
> free and reliable solution provides high availability, load balancing, and proxying for TCP-or HTTP-based applications.


### FAQ
1. HAProxy vs. Nginx
```
haproxy is a "load balancer" it doesn't known to serve files or dynamic content.

nginx is a web server capable of many interesting things. 
```
