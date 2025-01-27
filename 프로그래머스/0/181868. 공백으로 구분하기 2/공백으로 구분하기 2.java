import java.util.Arrays;

class Solution {
    public String[] solution(String myString) {
        String[] arr = myString.split(" ");
        return Arrays.stream(arr).filter(s -> !s.equals("")).toArray(String[]::new);
    }
}