import java.util.*;

class Solution {
    public String solution(String s) {
        boolean isFirst = true;
        String answer = "";
        for (char c : s.toCharArray()) {
            if (isFirst == true) {
                c = Character.toUpperCase(c);
                isFirst = false;
            }
            else if (isFirst == false) {
                c = Character.toLowerCase(c);
                isFirst = false;
            }
            if (c == ' ') {
                isFirst = true;
            }
            answer += c;
        }
        return answer;
    }
}