"""
Implementing a Python Stack
    list:
        > built upon blocks of contiguous memory, in the list are stored right next to each other.
        > Lits is not thread-safe
            memeory allocations
            .append() add new elements to the top of your stack
            .pop() removes the elements in the LIFO order
    collections.deque
        > built upon a double linked list
        > .append() and .pop() operartions are atomic
            .append() add new elements to the top of your stack
            .pop() removes the elements in the LIFO order
    queue.LifoQueue
        > thread-safe()
            .put() add data
            .get() remove data
"""
