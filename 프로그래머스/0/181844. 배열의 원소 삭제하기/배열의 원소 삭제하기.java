import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> numArr = new ArrayList<>();
        for(int number : arr) {
            numArr.add(number);
        }
        for(int number : delete_list) {
            int index = numArr.indexOf(number);
            if(index != -1) {
                numArr.remove(index);
            }
        }
        int[] answer = new int[numArr.size()];
        for(int i=0; i<answer.length; i++) {
            answer[i] = numArr.get(i);
        }
        return answer;
    }
}