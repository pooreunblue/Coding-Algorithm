import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        List<Integer> list = new ArrayList<>();
        while (n != 0) {
            list.add(0, n % 3);
            n /= 3;
        }
        for (int i = 0; i < list.size(); i++) {
            answer += Math.pow(3,i) * list.get(i);
        }
        return answer;
    }
}