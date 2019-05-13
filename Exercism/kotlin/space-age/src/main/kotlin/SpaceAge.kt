val EARTH_ORBIT_IN_SECONDS = 31557600

class SpaceAge(input: Long){
    val seconds: Double
    val planetOrbitTime = mapOf(
        "Mercury" to 0.2408467,
        "Venus" to 0.61519726,
        "Mars" to 1.8808158,
        "Jupiter" to 11.862615,
        "Saturn" to 29.447498,
        "Uranus" to 84.016846,
        "Neptune" to 164.79132
    )

    init {
        seconds = input.toDouble()
    }

    private fun round(orbit: Double): Double {
        return String.format("%.2f", this.seconds / orbit).toDouble()
    }

    fun on(planet: String): Double {
        var planetsOrbit = this.planetOrbitTime.get(planet) ?: 1.0
        var percentageOfEarthsOrbit = planetsOrbit * EARTH_ORBIT_IN_SECONDS
        return round(percentageOfEarthsOrbit)
    }

}