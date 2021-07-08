# Computer network programming

> Computer network programming involves writing computer programs that enable processes to communicate with each other across a computer network.

* Connection-oriented (面向连接通信)
    * TCP (Transmission Control Protocol)
    * SPX (Sequenced Packet Exchanges)

* connectionless communications (无连接通信)
    * UDP (User Datagram Protocol)
    * raw IP
    * IPX (Internetwork Packet Exchange)

| OSI/ISO Layer | Protocol | API |
|:--------------|:---------|:----|
| L3 (network)  | IP | Raw socket|
| L4 (Transport)|TCP,UDP,SCTP| Berkeley Sockets|
| L5 (session)| TLS | OpenSSL|
| L7 (application) | HTTP | Various|
