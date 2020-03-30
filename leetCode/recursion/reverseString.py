class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def switchPointers(ptr1: int, ptr2: int):
            if ptr1 < ptr2:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                switchPointers(ptr1 + 1, ptr2 - 1)
        switchPointers(0, len(s) - 1) 
