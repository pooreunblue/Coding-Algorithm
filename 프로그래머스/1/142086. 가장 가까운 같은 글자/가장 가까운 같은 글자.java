import java.util.*;

class Solution {
    public int[] solution(String s) {
        Map<String, Integer> map = new HashMap<>();
        String[] alphabets = s.split("");
        int[] answer = new int[s.length()];
        for (int i = 0; i < alphabets.length; i++) {
            if (map.containsKey(alphabets[i])) {
                answer[i] = i - map.get(alphabets[i]);
                map.put(alphabets[i], i);
            } else {
                answer[i] = -1;
                map.put(alphabets[i], i);
            }
        }
        return answer;
    }
}