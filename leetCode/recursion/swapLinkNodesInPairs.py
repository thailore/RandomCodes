class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        firstNode = head
        secondNode = head.next
        
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode
        
        return secondNode
