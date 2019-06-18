class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        var location = mutableListOf<Int>()
        for(i in 0..nums.size - 1) {
            if(nums[i] == target){
                location.add(i as Int)
            }
        }

        return if (location.size > 0) intArrayOf(location[0], location.last()) else intArrayOf(-1,-1)
    }
}
