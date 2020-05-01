"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
"""

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = OrderedDict() # normal stack
        self.nonunique = OrderedDict() # normal array
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if len(self.unique) > 0:
            return next(iter(self.unique.values()))
        return -1

    def add(self, value: int) -> None:
        if value in self.nonunique: return
        if value in self.unique:
            self.unique.pop(value)
            self.nonunique.update({value:value})
            return
        else:
            self.unique.update({value:value})


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
