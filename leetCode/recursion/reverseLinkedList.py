# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        previous = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return previous

    
    def reverseListIteratively(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
        
