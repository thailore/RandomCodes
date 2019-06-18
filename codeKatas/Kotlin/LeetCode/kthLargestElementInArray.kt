class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        var mapOfNumbers = mutableMapOf<Int, Int>()
        nums.forEach { number ->
            var valueOf = mapOfNumbers.get(number)
            if(valueOf != null){
                mapOfNumbers.put(number, valueOf + 1)
            }else{
                mapOfNumbers.put(number, 1)
            }
        }
        var sortedMap = mapOfNumbers.toSortedMap(reverseOrder())
        var counter = 0
        sortedMap.forEach { (key, value) -> 
            counter += value
            if(counter >= k){
                return key
            }
        }
            
        return 1
    }
    
    
    // fun findKthLargest(nums: IntArray, k:Int): Int{
    //     var sorted = nums.sortedDescending()
    //     print(sorted)
    //     return sorted[k-1]
    // }


    //    public int findKthLargest(int[] nums, int k) {
    //	    PriorityQueue priorityQ = new PriorityQueue<Integer>();
    //	    for(Integer number: nums){
    //        priorityQ.add(number);
    //        if(priorityQ.size > k){
    //            priorityQ.poll();
    //        }
    //    }
        
        
    //    return priorityQ.peek();
   // }
}
