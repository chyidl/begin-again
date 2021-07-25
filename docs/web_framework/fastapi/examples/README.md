* fastapi
  
* uvicorn
> ASGI 服务器

* Concurrency and async / await
```buildoutcfg
using await inside of functions created with async def

using a third party library that communicates with something (a database, an API, the file system, etc) and doesn't support for using await, then declare operation function as normally with just def.

# Note: can mix def and async def in path operation function. FastAPI do right with them.
FastAPI work asynchroonously and be extremely fast.

I/O Bound:
    the data from the client to be sent through the network
    the data sent by your program to be received by the client through the network
    the contents of a file in the disk to be read by the system and given to your program
    the contents your program gave to the system to be written to disk
    a remote API operation
    a database operation to finish
    a database query to return the results
 
CPU Bound:
    Audio or image processing
    Computer vision: an image is composed of millions of pixels, each pixel has 3 values / colors, processing that normally requires computing something on those pixels, all at the same time.
    Machine Learning: it normally requires lots of "matrix" and "vector" multiplications.
    Deep Learning: This is a sub-field of Machine Learning, so. the same applies. 
```
