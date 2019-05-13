import org.junit.Test
import org.junit.Ignore
import kotlin.test.assertEquals

class SpaceAgeTest {

    @Test
    fun ageOnEarth() {
        val age = SpaceAge(1000000000)

        assertEquals(31.69, age.on("Earth"))
    }

    @Test
    fun ageOnMercury() {
        val age = SpaceAge(2134835688)

        assertEquals(280.88, age.on("Mercury"))
    }

    @Test
    fun ageOnVenus() {
        val age = SpaceAge(189839836)

        assertEquals(9.78, age.on("Venus"))
    }

    @Test
    fun ageOnMars() {
        val age = SpaceAge(2329871239L)

        assertEquals(39.25, age.on("Mars"))
    }

    @Test
    fun ageOnJupiter() {
        val age = SpaceAge(901876382)

        assertEquals(2.41, age.on("Jupiter"))
    }

    @Test
    fun ageOnSaturn() {
        val age = SpaceAge(3000000000L)

        assertEquals(3.23, age.on("Saturn"))
    }

    @Test
    fun ageOnUranus() {
        val age = SpaceAge(3210123456L)

        assertEquals(1.21, age.on("Uranus"))
    }

    @Test
    fun ageOnNeptune() {
        val age = SpaceAge(8210123456L)

        assertEquals(1.58, age.on("Neptune"))
    }

}
