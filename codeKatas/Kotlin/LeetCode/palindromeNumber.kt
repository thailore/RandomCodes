class Solution {
    fun isPalindrome(x: Int): Boolean {
        var forwards = x.toString()
        var backwards = forwards.reversed()
        
        return forwards == backwards
    }
}
