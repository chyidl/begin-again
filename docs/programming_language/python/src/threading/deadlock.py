# Deadlock
"""
Deadlock usually happen from one of two sublet things:
    1. An implementation bug where a Lock is not released properly
    2. A design issue where a utility function needs to be called by functions that might or might not already have the Lock.

RLock: allow a thread to .acquire() an RLock multiple times before it calls.release()
"""
import threading


l = threading.RLock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")
l.release()
print("first release")
l.release()
print("second release")
