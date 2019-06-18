class Luhn {

    companion object {
        fun isValid(input: String): Boolean {

            val numbers = convertToInteger(input).toMutableList()

            if (numbers.size <= 1) return false

            for (i in numbers.size - 2 downTo 0 step 2) {

                val doubled = numbers[i] * 2

                when (doubled > 9) {
                    true -> numbers[i] = doubled - 9
                    false -> numbers[i] = doubled
                }
            }

            return numbers.sum() % 10 == 0

        }

        fun convertToInteger(stringNumber: String): List<Int> {
            val strippedString = stringNumber.replace(" ", "")

            val listOfNumbers = mutableListOf<Int>()

            for (character in strippedString.indices) {
                try {
                    listOfNumbers.add(strippedString[character].toString().toInt())
                } catch (exception: NumberFormatException) {
                    return emptyList()
                }
            }

            return listOfNumbers
        }
    }
}
