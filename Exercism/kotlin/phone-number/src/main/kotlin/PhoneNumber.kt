class PhoneNumber(input: String){
    var number: String

    init {
        this.number = convertInput(input)
    }

    private fun convertInput(input: String): String {
        var number = input.replace("[^0-9]".toRegex(), "")
        if(number[0] == 1)
    }
}