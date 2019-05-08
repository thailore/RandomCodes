import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class ResistorColor {

    int colorCode(String color) {
        if(Arrays.asList(colors()).contains(color)){
            Map colorMap = getResistorMapping();
            return (int) colorMap.get(color);
        }
        return -1;
    }
    
    String[] colors() {
        String[] colors = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
        return colors;
    }
    Map getResistorMapping() {
        Map<String, Integer> colorMap = new HashMap<String, Integer>();
        String[] colors = colors();
        for (int i=0;i<colors.length;i++) {
            colorMap.put(colors[i], i);
        }   
        return colorMap;
    }
}
