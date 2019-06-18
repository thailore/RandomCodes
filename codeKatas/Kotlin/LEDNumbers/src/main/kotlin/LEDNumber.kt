import java.lang.StringBuilder

class LEDNumber{

    private val numbers: MutableMap<Int,List<Int>> = mutableMapOf(
            0 to listOf(0,1,0,1,0,1,1,1,1),
            1 to listOf(0,0,0,0,0,1,0,0,1),
            2 to listOf(0,1,0,0,1,1,1,1,0),
            3 to listOf(0,1,0,0,1,1,0,1,1),
            4 to listOf(0,0,0,1,1,1,0,0,1),
            5 to listOf(0,1,0,1,1,0,0,1,1),
            6 to listOf(0,1,0,1,1,0,1,1,1),
            7 to listOf(0,1,0,0,0,1,0,0,1),
            8 to listOf(0,1,0,1,1,1,1,1,1),
            9 to listOf(0,1,0,1,1,1,0,1,1))

    fun getSegments(number: Int) : List<Int>?{
        return numbers[number]
    }

    fun getDisplay(segments: List<Int>) : String{

        var display = StringBuilder()
        for(index in 0..8) {

            if(segments!![index] == 0) display.append(" ")
            else {
                if(index in listOf(3,5,6,8)) display.append("|")
                if(index in listOf(1, 4, 7)) display.append("_")
            }

            if(index == 2 || index == 5){
                display.append("\n")
            }

        }
        return display.toString()
    }

}
