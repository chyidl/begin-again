# Threading

```
1. The threads may be running on different processors, but they will only be running one at a time.

2. If a program is running Threads that are not daemons, then the program will wait for those threads to complete before it terminates. Threads that daemons, however, are just killed wherever thay are when the program is existing.

➜ python3
Python 3.9.5 (default, May  4 2021, 03:36:27)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def inc(x):
...     x += 1
...
# dis - Disassembler for Python bytecode
>>> import dis
>>> dis.dis(inc)
  2           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (1)
              4 INPLACE_ADD
              6 STORE_FAST               0 (x)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>>

3. A Lock is an object that acts like a hall pass. Only one thread at a time can have the Lock. Any other thread that wants the Lock must wait until the owner of the Lock gives it up.

4. threading.Semaphore:
    The first one is that the counting is atomic. This means that there is a guarantee that the operating system will not swap out the thread in the middle of incrementing or decrementing the counter.

    The internal counter is incremented when you call .release() and decremented when you call .acquire()

    Semaphores are frequently used to protect a resource that has a limited capacity

5. threading.Timer():
    schedule a function to be called after a certain amount of time has passed.

    A Timer can be used to prompt a user for action after a specific amount of time. If the user does the action before the Timer expires, .cancel() can be called.

6. threading.Barrier:

```

