class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        
        for i in range(1, rowIndex + 1):
            curr = [1]
            for j in range(1, i):
                curr.append(prev[j-1] + prev[j])
            curr.append(1)
            prev = curr
            
        return prev

