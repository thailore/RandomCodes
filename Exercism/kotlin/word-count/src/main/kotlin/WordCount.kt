class WordCount {

    companion object {
        fun phrase(phrase: String): Map<String, Int?>{
            var wordCount = mutableMapOf<String, Int?>()
            var words: List<String> = cleanPhrase(phrase).toLowerCase().split( ",")
            for (i in 0 until words.size){
                if(wordCount.containsKey(words[i])) {
                    wordCount.set(words[i], wordCount.get(words[i])?.plus(1))
                }else{
                    wordCount.set(words[i], 1)
                }
            }
            return wordCount
        }

        private fun cleanPhrase(phrase: String): String {
            var badCharacters = listOf("!","&", "@","%", "^", "\n", ":", ".")

            var newPhrase = phrase
            for(character in badCharacters) {
                newPhrase = newPhrase.replace(character, "")
            }
            return newPhrase.replace("\\s".toRegex(), ",")
        }
    }

}
