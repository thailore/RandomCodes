class Solution:
    def decodeString(self, s: str) -> str:
        strStack = []
        intStack = []
        ptr = 0
        curStr = ''
        
        while ptr < len(s):
            if self.checkIfInt(s[ptr]):
                count = 0
                while self.checkIfInt(s[ptr]):
                    count = 10 * count + (int(s[ptr]))
                    ptr += 1
                intStack.append(count)
            elif s[ptr] == '[':
                strStack.append(curStr)
                curStr = ""
                ptr += 1
            elif s[ptr] == ']':
                tempStr = strStack.pop()
                tempInt = intStack.pop()
                tempStr += tempInt * curStr
                curStr = tempStr
                ptr += 1
            else:
                curStr += s[ptr]
                ptr += 1
        return curStr

    def checkIfInt(self,x: int) -> bool:
        try:
            int(x)
            return True
        except ValueError:
            return False
