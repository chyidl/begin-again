## How to
```markdown
$ cd recommendations

# generates several Python files from the .proto file
$ python -m grpc_tools.protoc \                                 # runs the protobuf compiler
    -I ../protobufs \
    --python_out=. \
    --grpc_python_out=. \
    ../protobufs/recommendations.proto

➜ tree -l .    
.
├── README.md
├── recommendations_pb2.py                  # the type definitions
└── recommendations_pb2_grpc.py             # the framework for a client and a server

0 directories, 3 files

# Make an RPC request
>>> import grpc
>>> from recommendations_pb2_grpc import RecommendationsStub
# insecure_channel: unauthenticated and unencrypted
>>> channel = grpc.insecure_channel("localhost:50051")
>>> client = RecommendationsStub(channel)
>>> request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
>>> client.Recommend(request)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/yogo/.pyenv/versions/begin-again-prj/lib/python3.8/site-packages/grpc/_channel.py", line 946, in __call__
    return _end_unary_response_blocking(state, call, False, None)
  File "/Users/yogo/.pyenv/versions/begin-again-prj/lib/python3.8/site-packages/grpc/_channel.py", line 849, in _end_unary_response_blocking
    raise _InactiveRpcError(state)
grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
        status = StatusCode.UNAVAILABLE
        details = "failed to connect to all addresses"
        debug_error_string = "{"created":"@1625819442.892025000","description":"Failed to pick subchannel","file":"src/core/ext/filters/client_channel/client_channel.cc","file_line":3009,"referenced_errors":[{"created":"@1625819442.892023000","description":"failed to connect to all addresses","file":"src/core/ext/filters/client_channel/lb_policy/pick_first/pick_first.cc","file_line":398,"grpc_status":14}]}"

```