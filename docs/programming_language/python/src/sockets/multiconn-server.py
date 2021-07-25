#!/usr/bin/env python3
import sys
import socket
import selectors
import types

"""
BaseSelector
    - SelectSelector    : select.select()
    - PollSelector      : select.poll()
    - EpollSelector     : select.epoll()
    - DevpollSelector   : select.devpoll()
    - KqueueSelector    : select.kqueue()

DefaultSelector: is an alias to the most efficient implementation available on the current platform
"""
sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"accepted {conn} from {addr}")
    conn.setblocking(False)  # configure the socket in non-blocking mode.
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    # register(fileobj, events, data=None)
    sel.register(conn, events, data=data)  # registers the socket to be monitored


def service_connection(key, mask):
    sock = key.fileobj  # the socket object
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)


host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
# sock.setblocking(True) is equivalent to sock.settimeout(None)
# sock.setblocking(False) is equivalent to sock.settimeout(0.0)
lsock.setblocking(False)

# Register a file object for selection, monitoring it for I/O events
sel.register(lsock, selectors.EVENT_READ, data=None)


# the event loop
try:
    while True:
        # blocks until there are sockets ready for I/O
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
