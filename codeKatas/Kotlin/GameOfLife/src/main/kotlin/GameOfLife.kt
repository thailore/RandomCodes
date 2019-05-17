data class Position(val x:Int, val y:Int)

inline fun getPositions(): List<Position> {
    return emptyList()
}

fun getNeighbours(position: Position, listOfOtherPositions: List<Position>): List<Position> {
    var xVal = position.x
    var yVal = position.y
    var neighbours = mutableListOf<Position>()
    for(x in xVal-1..xVal+1){
        for(y in yVal-1..yVal+1){
            if(x==xVal && y == yVal) {
                continue
            }
            if(Position(x, y) in listOfOtherPositions){
                neighbours.add(Position(x, y))
            }
        }
    }
    return neighbours
}

fun nextStep(positions: List<Position>): List<Position> {
    return listOf(Position(1, 0))

}
