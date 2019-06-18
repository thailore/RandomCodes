/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var head = ListNode(0)
        var first = l1
        var second = l2
        var current = head
        var remainder = 0
        while(first != null || second != null){
            var firstValue = if(first?.`val` == null) 0 else first?.`val`
            var secondValue = if(second?.`val` == null) 0 else second?.`val`

            var sum = remainder + firstValue + secondValue
            remainder = sum / 10
            current?.next = ListNode(sum.rem(10))
            current = current?.next
            
            if (first != null) first = first?.next
            if (second != null) second = second?.next
        }
        
        if(remainder > 0){
            current?.next = ListNode(remainder)
        }
        return head?.next
            
    }
}
