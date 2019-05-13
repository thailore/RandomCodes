class Triangle(side1: Number, side2: Number, side3: Number) {

    var sides = arrayOf(side1.toDouble(), side2.toDouble(), side3.toDouble())
    init {
        validate(sides)
    }
    val isEquilateral = sides.distinct().size == 1
    val isIsosceles = sides.distinct().size <= 2
    val isScalene = sides.distinct().size == 3


    fun validate(sides: Array<Double>){
        var valid = true
        if(sides.contains(0.0)) valid = false

        var sumOfSides = sides.sum()

        for(side in sides) {
            if (sumOfSides - side < side){
                valid = false
            }
        }
        if(!valid){
            throw IllegalArgumentException()
        }
    }
}