import java.util.*;

class Solution {
    public String solution(String s) {
        int index = 0;
        String answer = "";
        String[] alphabets = s.split("");
        for (String alphabet : alphabets) {
            if (alphabet.equals(" ")) {
                index = 0;
                answer += alphabet;
            } else {
                if (index % 2 == 0) {
                    answer += alphabet.toUpperCase();
                } else {
                    answer += alphabet.toLowerCase();
                }
                index++;
            }
        }
        return answer;
        }
}