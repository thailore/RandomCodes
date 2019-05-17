enum class Allergen(val value: Int) {
    CATS(128),
    POLLEN(64),
    CHOCOLATE(32),
    TOMATOES(16),
    STRAWBERRIES(8),
    SHELLFISH(4),
    PEANUTS(2),
    EGGS(1)
}


class Allergies(allergyScore: Int){
    var score: Int = allergyScore
    fun isAllergicTo(allergen: Allergen): Boolean{
       return allergen in this.getList()
    }

    fun getList(): List<Allergen> {
        val allergies = mutableListOf<Allergen>()

        var personScore: Int = this.score

        while (personScore > 0){
            Allergen.values().forEach {
                allergen -> if (allergen.value <= personScore && allergen !in allergies) {
                    personScore -= allergen.value
                    allergies.add(allergen)
                }
            }
            break
        }

        return allergies.reversed()
    }
}