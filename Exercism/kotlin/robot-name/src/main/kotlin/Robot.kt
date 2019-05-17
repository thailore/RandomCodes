var exisitingNames = mutableMapOf<String, Boolean>()

class Robot {
    var name: String

    init{
        name = getRobotName()
    }


    private fun getRobotName(): String {
        var proposedName = StringBuilder()

        var numbers = randomNumber()*100 + randomNumber()*10 + randomNumber()
        var firstLetter = randomLetter()
        var secondLetter = randomLetter()

        proposedName.append(firstLetter).append(secondLetter).append(numbers.toString())

        var name = proposedName.toString()

        var nameTaken = exisitingNames.get(name) ?: false


        if(nameTaken){
            name = getRobotName()
        }
        exisitingNames.put(name, true)

        return name
    }

    fun reset() {
        this.name = getRobotName()
    }

    fun randomNumber(): Int {
        return (0..9).shuffled().first()
    }

    fun randomLetter(): String {
        return ('A'..'Z').shuffled().first().toString()
    }
}