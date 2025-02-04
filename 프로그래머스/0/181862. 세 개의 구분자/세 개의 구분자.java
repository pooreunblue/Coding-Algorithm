import java.util.Arrays;

class Solution {
    public String[] solution(String myStr) {
        String[] answer = {};
        String[] splitted = myStr.split("a|b|c");
        String[] newArray = Arrays.stream(splitted).filter(s->!s.equals("")).toArray(String[]::new);
        if(Arrays.equals(answer, newArray)) {
            return new String[]{"EMPTY"};
        }
        return newArray;
    }
}