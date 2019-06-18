class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        var answer = ""
        var allEqual = true
        var endingPoint = 0
        when(strs.size) {
            0 -> return answer
            1 -> return strs[0]
        }
        
        while(allEqual){
            var lengths = strs[0].length
            when{
                lengths == 0 || lengths < endingPoint -> return answer
            }
            var test = strs[0].substring(0,endingPoint)
            for(i in 1..strs.size-1){
                
                if(strs[i].length < endingPoint || strs[i].length == 0){
                    return answer
                }
                if(strs[i].substring(0, endingPoint) != test){
                    return answer
                }
            }
            answer = test
            endingPoint+=1
        }
        return answer
        
    }
}
