object ScrabbleScore {
    var scoring = mapOf(
            listOf('A','E','I','O', 'U', 'L', 'N', 'R', 'S', 'T') to 1,
            listOf('D', 'G') to 2,
            listOf('B', 'C', 'M', 'P') to 3,
            listOf('F', 'H', 'V', 'W', 'Y') to 4,
            listOf('K') to 5,
            listOf('J', 'X') to 8,
            listOf('Q', 'Z') to 10
    )

    fun scoreWord(word: String): Int {
        var score = 0
        if(word.length > 0){

            word.forEach{ c ->
                for ((k, v) in scoring){
                    if(c.toUpperCase() in k){
                        score += v
                    }
                }
            }
        }

        return score
    }
}