Memory Management
=================
```
CPython, is actually written in the C programming language

Python is an interpreted programming language.
  Python source code -> bytecode (cached pyc file)

CPython is written in C, which does not natively support object-oriented programming

structure, in C is a custom data type that groups together different data type. To compare to object-oriented languages, its like a class with attributes and no methods

PyObject:
  ob_refcnt: reference count -- used for garbage collection
  ob_type: pointer to another type

The Global Interpreter Lock (GIL):
  The GIL is a solution to the common problem of dealing with shared resources, like memory in a computer.
  When CPython handles memory, it uses the GIL to ensure that it does so safely.

  every object in Python has a reference count and a pointer to a type
    1. assign it to another variable -> reference count will increase
    2. pass the object as an argument -> reference count will increase

    sys.getrefcount(numbers) -> getrefcount() increase the reference count by 1.


CPython's Memory Management:
  VMM: virtual memory layer
```
