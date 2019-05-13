object Acronym {
    fun generate(phrase: String): String {
        var acronym = StringBuilder()
        val words = phrase.split(" ", "-")
        for (word in words){
            acronym.append(word[0].toUpperCase())
        }
        return acronym.toString()

    }
}