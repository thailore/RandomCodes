import java.util.Map;
class Darts {
    double xVal;
    double yVal;
    Map<Integer, Integer> dartBoardScores = Map.of(1, 10, 5, 5, 10, 1);
    
    Darts(double x, double y) {
        this.xVal = x;
        this.yVal = y;
    }

    int score() {
        double location = Math.sqrt(Math.pow(Math.abs(xVal), 2) + Math.pow(Math.abs(yVal), 2));
        if (location > 10){
            return 0;
        }
        int score = 0;
        for (int key : dartBoardScores.keySet()){
            if(location <= key) {
                score = (int) dartBoardScores.get(key);
            }
        }
        return score;
    }

}
 