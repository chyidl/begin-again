* Cache Strategy
| Strategy    | Eviction Policy | Use case     |
|:------------|:----------------|:-------------|
| First-In/Fist-Out(FIFO) | Evicts the oldest of the entries | Newer entries are most likely to be resued |
| Last-In/First-Out (LIFO) | Evicts the latest of the entries | Older entries are most likely to be resued |
| Least Recently Used (LRU) | Evitcs the least recently used entry | Recently used entries are most likely to be reused |
| Most Recently Used (MRU) | Evicts the most recently used entry | Least recently used entries are most likely to be reused |
| Least Frequently Used (LFU) | Evicts the least often accessed entry| Entries with a lot of hits are more likely to be reused. |
