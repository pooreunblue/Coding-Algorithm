import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answerList = new ArrayList<>();
        for (int[] command : commands) {
            int i = command[0];
            int j = command[1];
            int k = command[2];
            List<Integer> list = new ArrayList<>();
            for (int ii = i-1; ii<j; ii++) {
                list.add(array[ii]);
            }
            list.sort(Comparator.naturalOrder());
            answerList.add(list.get(k-1));
        }
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}