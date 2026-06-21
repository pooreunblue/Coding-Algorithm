import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answerList = new ArrayList<>();
        int[] scoreboard = new int[3];
        int[][] math_give_up= {{1,2,3,4,5}, {2,1,2,3,2,4,2,5}, {3,3,1,1,2,2,4,4,5,5}};
        for (int i=0; i<math_give_up.length; i++) {
            int score = 0;
            for (int j=0; j<answers.length; j++) {
                if (answers[j] == math_give_up[i][j % math_give_up[i].length]) {
                    score += 1;
                }
            }
            scoreboard[i] = score;
        }
        int max = scoreboard[0];
        for (int i = 1; i < scoreboard.length; i++) {
            if (scoreboard[i] > max) {
                max = scoreboard[i];
            }
        }
        for (int i = 0; i < scoreboard.length; i++) {
            if (scoreboard[i] == max) {
                answerList.add(i+1);
            }
        }
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}