#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    """
    address family:
        socket.AF_INET IPv4
    socket type:
        socket.SOCK_STREAM
    """
    s.bind((HOST, PORT))
    """
    # backlog parameter, specifies the number of unaccpted connections that the system will allow before refusing new connections

    If your server receives a lot of connection requests simultaneously, incresing the backlog value may help by setting the maximum length of the queue for pending connections.
    ➜ cat /proc/sys/net/core/somaxconn
    4096
    """
    s.listen()
    """
    # accept() blocks and waits for an incoming connection
    IPv4: (host, port)
    IPv6: (host, port, flowinfo, scopeid)
    """
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr=}")
        while True:
            data = conn.recv(1024)
            # if conn.recv() returns an empty bytes object, b''
            if not data:
                break
            conn.sendall(data)
