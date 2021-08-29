// 哈希表支持常数时间复杂度的增删查，hashmap 不能维护有序性
// 红黑树支持有序性，并且增加删除性能很好，但是不支持范围搜索，
// 跳表利用空间换时间，性能和红黑树比肩，还支持区间搜索
// 	最底层包含所有的数据节点，每一层链表都有一个指向下一层和自己相同的节点，向后的指针指向随机的同层比自己大的数据
// https://github.com/MauriceGit/skiplist/blob/master/skiplist.go
package main

const (
	// maxLevel denotes the maximum height of the skiplist
	maxLevel = 25
	eps      = 0.00001
)

// ListElement is the interface to implement for elements that are inserted into a skiplist
type ListEment interface {
	// ExtractKey() returns a float64 representation of the key that is used for insertion/deletion/find. It needs to establish an order over all elements
	ExtractKey() float64

	// A string representation of the element. Can be used for pretty-printing the list. Otherwise just return an empty string.
	String() string
}
