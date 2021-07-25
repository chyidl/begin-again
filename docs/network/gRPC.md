# gRPC
> A high performance, open souce universal RPC framework.

gRPC Motivation and Design Principles
-------------------------------------


Core concepts, architecture and lifecycle
-----------------------------------------
* gRPC define four kinds of service method:
    * Unary RPCs [where the client sends a single request to the server and gets a single response back]
    ```
    rpc SayHello(HelloRequest) returns (HelloResponse);
    ```

    * Server streaming RPCs [where the client sends a request to the server and gets a stream to read a sequence of messages back.]
    ```
    rpc LotsOfReplies(HelloRequest) returns (stream HelloResponse);
    ```

    * Client streaming RPCs [where the client writes a sequence of messages and sends them to the server]
    ```
    rpc LotsofGreetings(stream HelloRequest) returns (HelloResponse);
    ```

    * Bidirectional streaming RPCs [where both sides send a sequence of messages using a read-write stream]
    ```
    rpc BidHello(stream HelloRequest) returns (stream HelloResponse);
    ```

* RPC life cycle
    * Unary RPC
    > the simplest type of RPC where the client sends a single request and get back a single response.
    ```
    1. Once the client calls a stub method, the server is notified that the RPC has been invoked with the client's metadata for this call, the method name, and the specified deadline if applicable.
    2. The server can then either send back its own initial metadata (which must be sent before any response) straight away, or wait for the client's request message. Which happens first, is application-specific.
    3. Once the server has the client's request message, it does whatever work is necessary to create and populate a response. The response is then returned (if successful) to the client together with status details (status code and optional status message) and optional trailing metadata.
    4. If the response status is OK, then the client gets the response, which completes the call on the client side.
    ```

    * Server streaming RPC
    >

    * Client streaming RPC
    >

    * Bidirectional streaming RPC
    >

* Deadlines/Timeouts
> gRPC allows clients to specify how long they are willing to wait for an RPC to complete before the RPC is terminated with a DEADLINE_EXCEEDED error.

* Metadata
> Metadata is opaque to gRPC itself - it lets the client provide information associated with the call to the server and vice versa.

* Channels
> A gRPC channel provides a connection to a gRPC server on a specified host and port. It is used when creating a client stub. such as switching message compression on or off.

FAQ
---

