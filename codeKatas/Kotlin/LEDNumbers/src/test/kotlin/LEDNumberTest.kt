import org.junit.Test
import kotlin.test.assertEquals

class LEDNumberTest {

    @Test
    fun test_getSegments() {
        var ledNumber = LEDNumber()
        var ledNumberSegments = listOf(0,1,0,1,1,1,1,1,1)
        assertEquals(ledNumber.getSegments(8), ledNumberSegments)
    }


    @Test
    fun test_getDisplayFor8() {
        var ledNumber = LEDNumber()
        var displayNumber = " _ \n|_|\n|_|"
        assertEquals(displayNumber, ledNumber.getDisplay(listOf(0,1,0,1,1,1,1,1,1)))
    }


    @Test
    fun test_getDisplayFor0() {
        var ledNumber = LEDNumber()
        var displayNumber = " _ \n| |\n|_|"
        assertEquals(displayNumber, ledNumber.getDisplay(listOf(0,1,0,1,0,1,1,1,1)))
    }


    @Test
    fun test_getDisplayFor1() {
        var ledNumber = LEDNumber()
        var displayNumber = "   \n  |\n  |"
        assertEquals(displayNumber, ledNumber.getDisplay(listOf(0,0,0,0,0,1,0,0,1)))
    }

    @Test
    fun test_endToEndFor2() {
        var ledNumber = LEDNumber()
        var displayNumber = " _ \n _|\n|_ "
        var segments = ledNumber.getSegments(2)
        assertEquals(displayNumber, ledNumber.getDisplay(segments!!))
    }

}
