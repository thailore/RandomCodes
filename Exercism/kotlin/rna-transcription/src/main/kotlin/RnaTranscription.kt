val map = mapOf("G" to "C", "C" to "G", "T" to "A", "A" to "U")

fun transcribeToRna(dna: String): String? {
    val answer = StringBuilder()
    for (i in dna.indices) {
        answer.append(map.get(dna[i].toString()))
    }
    return answer.toString()
}