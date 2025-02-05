import java.util.Arrays;
import java.util.ArrayList;


class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<flag.length; i++) {
            if(flag[i] == true) {
                for(int j=0; j < arr[i]; j++) {
                    answer.add(arr[i]);
                    answer.add(arr[i]);
                }
            } else if(flag[i] == false) {
                for(int j=0; j < arr[i]; j++) {
                    answer.remove(answer.size()-1);
                }
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}