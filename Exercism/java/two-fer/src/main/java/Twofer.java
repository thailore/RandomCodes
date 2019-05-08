class Twofer {
    String twofer(String name) {
        String person = name  == null ? "you" : name;
        String answer = String.format("One for %s, one for me.", person);
        return answer;
    }
}
