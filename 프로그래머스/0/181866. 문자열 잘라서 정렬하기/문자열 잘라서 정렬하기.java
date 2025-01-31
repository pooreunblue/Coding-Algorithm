import java.util.Arrays;

class Solution {
    public String[] solution(String myString) {
        String[] answer = myString.split("x");
        Arrays.sort(answer);
        return Arrays.stream(answer).filter(s->!s.equals("")).toArray(String[]::new);
    }
}