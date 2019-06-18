class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var map = mutableMapOf<Int, Int>()
        
        var answer = IntArray(2)
        for(i in 0..nums.size-1){
            var secondValue = target-nums[i]
            if(map.containsKey(secondValue)){
                var secondIndex = nums.indexOf(secondValue)
                if(i != secondIndex){
                  answer = intArrayOf(i, secondIndex)    
                  break
                }
            }
            map.put(nums[i], i)
        }
        answer.sort()
        return answer
    }
}
