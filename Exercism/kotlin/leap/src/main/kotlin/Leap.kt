class Year(inputYear: Int){
    var year: Int
    var isLeap: Boolean

    init {
        year = inputYear
        isLeap = this.findLeap()
    }

    fun findLeap(): Boolean {
        val year = this.year
        if ((year % 400 == 0 || year % 100 != 0) && (year % 4 == 0)){
            return true
        }
        return false
    }
}