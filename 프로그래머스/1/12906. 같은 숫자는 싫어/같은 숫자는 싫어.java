import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int n: arr) {
            if (stack.size() == 0 || n != stack.peekLast()) {
                stack.add(n);
            }
        }
        int[] answer = new int[stack.size()];
        int size = stack.size();
        for (int i = 0; i < size; i++) {
            answer[i] = stack.pop();
        }
        return answer;
    }
}