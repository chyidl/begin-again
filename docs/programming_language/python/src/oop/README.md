Object-oriented Programming
===========================
```
1. Planning out your software project often takes a lot longer than actually coding it.
```

Class - 类
----------
```
attribute: 属性
  instance attribute: 实例属性
  class attribute: 类属性

behavior: 行为 - 方法
```

Object - 对象
-------------
```
# Object AND Classes
  An object is a way of grouping data and methods on that data together
  Object often map to things in the real world
# A class defines how to makes an object
# Use a class to create objects
```

Inheritance - 继承
------------------
```
1. Compose a class
2. Use super() to access parent methods
3. Understand single and multiple inheritance

MRO - Method Resolution Order determines where Python looks for a method when there is hierarchy of classes.
```

* __init__  : initializer: is used to construct a new object from the class.
*

```
>>> class A:
...     pass
...
>>> class B(A):
...     pass
...
>>> dir(B)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> dir(B.__class__)
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
```

