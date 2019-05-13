import kotlin.math.*

class Squares(inputValue: Int) {
    val value: Int

    init {
       value = inputValue
    }

    fun squareOfSum(): Int {
        var squareOfSum = 0
        for(number in 1..this.value){
            squareOfSum += number
        }
        return getSquaredValue(squareOfSum)
    }

    fun sumOfSquares(): Int {
        var sumOfSquares = 0
        for(number in 1..this.value){
            sumOfSquares += getSquaredValue(number)
        }
        return sumOfSquares
    }

    fun difference(): Int {
        return abs(sumOfSquares() - squareOfSum())
    }

    fun getSquaredValue(value: Int): Int {
        return value.toDouble().pow(2).toInt()
    }
}
