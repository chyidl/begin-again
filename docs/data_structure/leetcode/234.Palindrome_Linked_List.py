"""
Palindrome Linked List

Time O(n)
Space O(1)
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        fast = head
        slow = head

        # Reverse half the list while trying to find the end
        while fast and fast.next:
            fast = fast.next.next
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # left side
        left = prev

        # right side
        if fast:
            """
            if fast is not None, then the length of the list is odd
            and we can ignore the middle value
            """
            right = slow.next
        else:
            right = slow

        # Just need to traverse each side and check if the value equal or not.
        while left is not None and right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
