class ReverseString {

    String reverse(String inputString) {
        StringBuilder reversedString = new StringBuilder();
        reversedString.append(inputString);
        reversedString = reversedString.reverse();

        return reversedString.toString();
    }
  
}