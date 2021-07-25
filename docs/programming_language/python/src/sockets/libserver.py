# The server's Message class
import sys
import selectors
import json
import io
import struct

request_search = {
    "morpheus": "Follow the white rabbit. \U0001f430",
    "ring": "In the caves beneath the Mistry Mountains. \U001f48d",
    "\U0001f436": "\U0001f43e Playing ball! \U0001f3d0",
}


class Message:
    def __init__(self, selectors, sock, addr):
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self._recv_buffer = b""
        self._send_buffer = b""
        self._jsonheader_len = None
        self.jsonheader = None
        self.request = None
        self.response_created = False
