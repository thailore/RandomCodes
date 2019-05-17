import org.junit.Test
import kotlin.test.assertEquals

class GameOfLifeTest {

    @Test
    fun test_canGetEmptyListOfPositions() {
        var positions: List<Position> = getPositions()
        assertEquals(emptyList(), positions)
    }

    @Test
    fun `get neighbours`() {
        var position1 = Position(0, 0)
        var position2 = Position(1, 1)

        var position = Position(3,0)
        assertEquals(listOf(position1), getNeighbours(position2,listOf(position,position1, position2)))

    }


    @Test
    fun test_dontGetSelfFromNeighbours() {
        var position1 = Position(0, 0)
        var position2 = Position(1, 1)

        var position = Position(1,1)
        assertEquals(listOf(position1), getNeighbours(position2,listOf(position,position1,position2)))

    }


    @Test
    fun test_gameOfLifeNextStep() {
        var position = Position(0, 0)
        var position1 = Position(1, 1)
        var position2 = Position(0,1)
        var position3 = Position(6,5)

        val positions = listOf(position, position1, position2, position3)

        assertEquals(listOf(Position(1, 0),Position(0,0),Position(0,1),Position(1,1)), nextStep(positions))

    }

    @Test
    fun test_2gameOfLifeNextStep() {
        var position = Position(3, 3)
        var position1 = Position(4, 3)
        var position2 = Position(2,3)

        val positions = listOf(position, position1, position2)

        assertEquals(listOf(Position(3,2), Position(3,3), Position(3,4)), nextStep(positions))

    }


}

